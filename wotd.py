import sqlite3
import random

# this function returns a random word from answers.db
def get_wotd():
    wotd_key = random.randrange(1,2309) 
    database_file = 'answers.db'
    database = sqlite3.connect(database_file)
    cur = database.cursor()
    cur.execute("SELECT * FROM answers WHERE answerID = ?", [wotd_key])
    #print(cur.fetchall())
    wotd = cur.fetchall()
    return wotd

# this function creates wotd.db (word of the day database) 
def createDB(wotd):
    connection = sqlite3.connect("wotd.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE answers (answerID PRIMARY KEY, answer)")
    cursor.executemany("INSERT INTO answers VALUES (?, ?)",wotd) 
    connection.commit()  # adds all of answers.json into answers.db


if __name__ == '__main__':
    wotd = get_wotd()
    createDB (wotd)


# '''wotd_key = random.randrange(1,2309) 
# database_file = 'answers.db'
# database = sqlite3.connect(database_file)
# cur = database.cursor()
# cur.execute("SELECT * FROM answers WHERE answerID = ?", [wotd_key])
# print(cur.fetchall())'''

# if __name__ == '__main__':
#     #answer = get_db()
#     # test = get_wotd()
#     #print(answer)
#     database_file = 'answers.db'
#     database = sqlite3.connect(database_file)

#     cur.execute("select * from answers where answer=:answerID", {"answerID": 1})
#     print(cur.fetchall())


#database.close()
