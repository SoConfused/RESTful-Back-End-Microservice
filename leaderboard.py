import redis

r = redis.Redis(host='localhost', port=6379, db=0)
def get_values():
    #r = redis.Redis(host='localhost', port=6379, db=0)
    keys = r.keys('*')
    for key in keys:
        value = r.get(key)
        display_board(key, value)

# r = redis.Redis(host='localhost', port=6379, db=0)
# keys = r.keys('*')
# for key in keys:
#     value = r.get(key)
#     print(','.join(str(keys) for keys in value)) 



def display_board(key, value):
    print(value)

get_values()
