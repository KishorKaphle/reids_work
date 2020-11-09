''' When channel is later on subscribed, published messages of previous time get lost! 
Can we get it back by any means? 
Don't know but it's a good question!'''


import redis
import time

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
    time.sleep(2)
    r = RedisWork('channel', i)  
    r.publish_message()
    print(i)



