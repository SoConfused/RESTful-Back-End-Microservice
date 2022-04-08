import sqlite3
import random

# this function selects a random word from answers.db
def get_wotd():
    wotd_key = random.randrange(1,2309) 
    database_file = 'answers.db'
    database = sqlite3.connect(database_file)
    cur = database.cursor()
    cur.execute("SELECT answer FROM answers WHERE answerID = ?", [wotd_key])
    wotd = cur.fetchone()
    #str = ''.join(wotd)
    #st = ''.join(map(str, wotd))
    database.close()
    return wotd

# this function creates wotd.db (word of the day database)
#   and inserts wotd from get_wotd() function
def createDB(wotd):
    connection = sqlite3.connect("wotd.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE answers (answer)")
    cursor.execute("INSERT INTO answers VALUES (?)",wotd) 
    connection.commit()
    connection.close()

# WORK IN PROGRESS
# this function is to load wotd.db with multiple game words
#   so players can play multiple words a day instead of just one.
# def make_list():
#     wotd_list = []
#     gameID = 1     #counter
#     while gameID <= 2309:
#         word = get_wotd()
#         word = (gameID, *word)
#         wotd_list.append(word)
#         gameID += 1
#     return wotd_list

# USE FOLLOWING FOR TESTING wotd.py
# if __name__ == '__main__':
#     wotd = get_wotd()
#     print(wotd_list)
#     createDB (wotd)

