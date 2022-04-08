import sqlite3
import random

# this function returns a random word from answers.db
def get_wotd():
    wotd_key = random.randrange(1,2309) 
    database_file = 'answers.db'
    database = sqlite3.connect(database_file)
    cur = database.cursor()
    cur.execute("SELECT answer FROM answers WHERE answerID = ?", [wotd_key])
    #print(cur.fetchall())
    wotd = cur.fetchone()
    #str = ''.join(wotd)
    #st = ''.join(map(str, wotd))
    return wotd

# def make_list():
#     wotd_list = []
#     gameID = 1     #counter
#     while gameID <= 2309:
#         word = get_wotd()
#         word = (gameID, *word)
#         wotd_list.append(word)
#         gameID += 1
#     return wotd_list

# this function creates wotd.db (word of the day database) 
def createDB(wotd):
    connection = sqlite3.connect("wotd.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE answers (answer)")
    cursor.execute("INSERT INTO answers VALUES (?)",wotd) 
    connection.commit()

if __name__ == '__main__':
    wotd = get_wotd()
    #print(wotd_list)
    createDB (wotd)

#database.close()

# 1 GameID wotd
# 2 Game wotd
# 3 Game wotd
# json.load ()
# for i, wotd in enumerate("answers.db"):
        # print(answer)
        #eachAnswer = (answerID, answer)
        #listAnswers.append(eachAnswer) # adds each answer to array
        #answerID += 1

