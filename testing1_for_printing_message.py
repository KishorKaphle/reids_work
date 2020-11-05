import redis
import threading


class RedisWork:

    def __init__ (self, channel_name, message):
        self.channel_name = channel_name
        self.message = message

    def get_redis(self):
        
        return redis.Redis(host='localhost', port=6379, db=0)


    def subscribe_channel(self):
        
        return self.get_redis().pubsub().subscribe(self.channel_name)


    def publish_message(self):
        
        return self.get_redis().publish(self.channel_name, self.message)


r = RedisWork('channel', 'hello!')
r.publish_message()
data = []
with r.get_redis().monitor() as m:
    for command in m.listen():
        print(command['command'])
        data.append(command['command'])
        break
print(data)