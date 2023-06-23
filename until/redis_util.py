import redis as redis


def get_redis(host='localhost', port=6379, password=None, db=0, decode_responses=True):
    return redis.Redis(host=host, port=port, password=password, db=db, decode_responses=decode_responses)


data = {
    'host': '192.168.50.128',
    'port': 6379,
    'password': 'nature',
    'db': 0
}
# r = redis.Redis(host='192.168.50.128', port=6379, password='nature', decode_responses=True)
r = get_redis(**data)
print(r.mget('name','name1'))
print(r.setrange('name',3,'自然'))
print(r.getrange('name',0,2))
print(r.strlen('name'))
print(r.incrbyfloat('age',2.2))