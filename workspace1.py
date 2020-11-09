from numpy import array
import numpy as np
import redis
import random
from cv2 import cv2
import matplotlib.pyplot as plt

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


#gray = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 8]])

img = cv2.imread('pic.png', 0)
plt.imshow(img)
plt.show()
to_sent = img
to_sent = to_sent.tostring()
    
    #print(to_sent.shape)
    
   

    #a_str = base64.binascii.b2a_base64(to_sent).decode('ascii')
    
    # get time stamp for the getting the individual image in the process 2
    #frame = str(datetime.datetime.now())
r = RedisWork(channel_name = 'channel', message = to_sent)
    #r.get_redis().set('frame', frame)
r.publish_message()
    #r.set('channel', a_str)
    
