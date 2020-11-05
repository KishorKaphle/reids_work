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


class Listener(threading.Thread):
    def __init__(self, channel_name, message):
        threading.Thread.__init__(self)
        self.channel_name = channel_name
        self.message = message
        r = RedisWork(self.channel_name, self.message)
        r.subscribe_channel()
        

    def get_redis(self):
        return redis.Redis(host='localhost', port=6379, db=0)   

    def work(self, item):
        print (item['channel'], ":", item['data'])

    def run(self):
        for item in self.subscribe_channel().listen():
            if item['data'] == "KILL":
                self.pubsub.unsubscribe()
                print (self, "unsubscribed and finished")
                break
            else:
                self.work(item)

if __name__ == '__main__':
    client = Listener('channel', 'hello!')
    client.start()

 