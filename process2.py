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

    def read_message(self):
        return self.subscribe_channel().get_message()


r = RedisWork('channel', 'Hello there!')
r.publish_message()
r.read_message()