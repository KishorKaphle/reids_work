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




def publish_send(channel, message):
    
    r = redis.Redis(host = 'localhost', port = 6379)
    r.set(channel, np.array(message).tostring())
    #time.sleep(2)

import numpy as np 
from cv2 import cv2

cap = cv2.VideoCapture(0)
while(True):
    #capture frame-by-frame
    ret, frame = cap.read()

    #our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #print(gray)
    #supply = gray.flatten()
    #supply = supply.tostring()
    #print(supply)

    #for chunck in gray:
        #publish_send('channel', chunck)

    #Display the resulting frame
    cv2.imshow('frame', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#when everything done, release the capture
cap.release()
cv2.destroyAllWindows()

