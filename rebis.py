#!/usr/bin/env python3

#from watchgod import watch
import redis
import sqlite3

# changed port to 6379 to reflect the redis server we are connected to
connection1 = sqlite3.connect("./var/stats1.db")
current1 = connection1.cursor()

connection2 = sqlite3.connect("./var/stats2.db")
current2 = connection2.cursor()

connection3 = sqlite3.connect("./var/stats3.db")
current3 = connection3.cursor()

r = redis.Redis()

temp1 = current1.execute("SELECT finished, guesses, won FROM games")
temp1 = current1.fetchmany()
#temp1 = current1.fetchone() // returns only 1 date // fetchall will return all 1 mil(its 10k) dates

temp2 = current2.execute("SELECT finished, guesses, won FROM games")
temp2 = current2.fetchall()

temp3 = current3.execute("SELECT finished, guesses, won FROM games")
temp3 = current3.fetchall()
#list = current.fetchall()

# print (r.set('stats1', str(temp1)))
# print(r.get('stats1')) 

# print()

# print (r.set('stats2', str(temp2)))
# print(r.get('stats2')) 

# print()

# print (r.set('stats3', str(temp3)))
# print(r.get('stats3')) 

# print()

#grabbing top 10 from shard 1
temp1 = current1.execute("SELECT user_id, won FROM games Order by won Desc Limit 10")
temp1 = current1.fetchall()
#print(temp1)

#grabbing top 10 from shard 2
temp2 = current2.execute("SELECT user_id, won FROM games Order by won Desc Limit 10")
temp2 = current2.fetchall()
#print(temp2)

#grabbing top 10 from shard 3
temp3 = current3.execute("SELECT user_id, won FROM games Order by won Desc Limit 10")
temp3 = current3.fetchall()
#print(temp3)

with r.pipeline() as pipe:
    #desc=True -> Least to greatest, doesn't work
    #might need to call key (user_id) and designate that to be the desc and to format after. 
    # pipe.sort(str(temp1), desc=True)
    # pipe.sort(str(temp2), desc=True)
    # pipe.sort(str(temp3), desc=True)

    pipe.set('stats1' , str(temp1))
    pipe.set('stats2', str(temp2))
    pipe.set('stats3', str(temp3))

    pipe.get('stats1')
    pipe.get('stats2')
    pipe.get('stats3')

    print(pipe.execute())


r.save()

#Can we try running this?

# r = redis.StrictRedis(host='localhost', port=6379, db=hello)
# print ("set key1 123")
# temp = "SELECT * FROM word_id"
# print (r.set('key1', temp))
# print ("get key1")
# print(r.get('key1')) 
