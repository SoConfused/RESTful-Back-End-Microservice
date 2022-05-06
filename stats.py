#!/usr/bin/env python3

import contextlib
import datetime
import random
import sqlite3
from faker import Faker
from typing import Optional
from fastapi import Depends, FastAPI
import uuid


# instruction: Once the API for your service is working correctly, 
# replace the single SQLite database configuration with four SQLite databases,
# 3 for games and 1 for users

SCHEMA = './share/stats.sql'
DATABASE = './var/stats.db'     # primary db

NUM_STATS = 1_000_000
NUM_USERS = 100_000
YEAR = 2022

random.seed(YEAR)
fake = Faker()
fake.seed(YEAR)

with contextlib.closing(sqlite3.connect(DATABASE)) as db: #db = connection object
    cursor = db.cursor()    # cursor object

    # read stats.sql file
    with open(SCHEMA) as f:
        db.executescript(f.read())
        #cursor.executescript(f.read())

    # Attach stats#.db. (Note: When referencing tables in QUERY, please use stats_db#.table_name)
    # Create games table in stats#.db
    cursor.execute('ATTACH DATABASE "./var/users.db" AS users_db')
    cursor.execute("CREATE TABLE users_db.users(user_id INTEGER PRIMARY KEY, username VARCHAR UNIQUE)")

    cursor.execute('ATTACH DATABASE "./var/stats1.db" AS stats_db1')
    #cursor.execute("CREATE TABLE stats_db2.games(user_id int, game_id int, finished date, guesses int, won boolean)")
    cursor.execute("CREATE TABLE stats_db1.games( \
        user_id INTEGER NOT NULL, \
        game_id NOT NULL, \
        finished DATE DEFAULT CURRENT_TIMESTAMP, \
        guesses INTEGER, \
        won BOOLEAN, \
        PRIMARY KEY(user_id, game_id) \
    )")

    cursor.execute('ATTACH DATABASE "./var/stats2.db" AS stats_db2')
    #cursor.execute("CREATE TABLE stats_db2.games(user_id int, game_id int, finished date, guesses int, won boolean)")
    cursor.execute("CREATE TABLE stats_db2.games( \
        user_id INTEGER NOT NULL, \
        game_id NOT NULL, \
        finished DATE DEFAULT CURRENT_TIMESTAMP, \
        guesses INTEGER, \
        won BOOLEAN, \
        PRIMARY KEY(user_id, game_id) \
    )")

    cursor.execute('ATTACH DATABASE "./var/stats3.db" AS stats_db3')
    #cursor.execute("CREATE TABLE stats_db3.games(user_id int, game_id int, finished date, guesses int, won boolean)")
    cursor.execute("CREATE TABLE stats_db3.games( \
        user_id INTEGER NOT NULL, \
        game_id NOT NULL, \
        finished DATE DEFAULT CURRENT_TIMESTAMP, \
        guesses INTEGER, \
        won BOOLEAN, \
        PRIMARY KEY(user_id, game_id) \
    )")






    for _ in range(NUM_USERS):
        while True:
            try:
                profile = fake.simple_profile()
                # insert into primary db for testing. Comment out when done.
                db.execute('INSERT INTO users(username) VALUES(:username)', profile)
                # insert into users db
                cursor.execute('INSERT INTO users_db.users(username) VALUES(:username)', profile)
            except sqlite3.IntegrityError:
                continue
            break
    
    db.commit()
    
    jan_1 = datetime.date(YEAR, 1, 1)
    today = datetime.date.today()
    num_days = (today - jan_1).days
    
    i = 0
    while i < NUM_STATS: #num stats is number of games
        while True:
            try:
                user_id = random.randint(1, NUM_USERS)
                game_id = random.randint(1, num_days)
                finished = jan_1 + datetime.timedelta(random.randint(0, num_days))
                # N.B. real game scores aren't uniformly distributed...
                guesses = random.randint(1, 6)
                # ... and people mostly play to win
                won = random.choice([False, True, True, True])
                # hash uuid(?) here then determine which of the 3 db to insert to
                # Example of horizontal partitioning

                # use user_id as shard key
                hash_value = user_id % 3
                
                # insert into primary db for testing. Comment out when done.
                db.execute("""INSERT INTO games(user_id, game_id, finished, guesses, won)
                VALUES(?, ?, ?, ?, ?)""", [user_id, game_id, finished, guesses, won])

                # insert into sharded db
                if (hash_value == 0):
                    cursor.execute("""INSERT INTO stats_db1.games(user_id, game_id, finished, guesses, won)
                VALUES(?, ?, ?, ?, ?)""", [user_id, game_id, finished, guesses, won])
                elif (hash_value == 1):
                    cursor.execute("""INSERT INTO stats_db2.games(user_id, game_id, finished, guesses, won)
                VALUES(?, ?, ?, ?, ?)""", [user_id, game_id, finished, guesses, won])
                else:
                    cursor.execute("""INSERT INTO stats_db3.games(user_id, game_id, finished, guesses, won)
                VALUES(?, ?, ?, ?, ?)""", [user_id, game_id, finished, guesses, won])

            except sqlite3.IntegrityError:
                continue
            i += 1
            break
    db.commit()

