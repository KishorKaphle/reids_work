''' When channel is already subscribed, publishing even at random 
provides all messages'''


import redis
import random

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




for i in range (10):
    if random.choice([0,1]) == 1:
        r = RedisWork('channel', i)
        r.publish_message()
        print(i)



