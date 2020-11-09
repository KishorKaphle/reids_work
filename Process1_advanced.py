from numpy import array
import numpy as np 
from cv2 import cv2
import redis



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


cap = cv2.VideoCapture(0)

while(True):
    #capture frame-by-frame
    ret, frame = cap.read()

    #our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    #arr = cv2.bitwise_not(gray) #equivalent to 255-gray
    
    a_str = cv2.imencode('.jpg', gray)[1]
    a_str = a_str.tostring()

    
    r = RedisWork(channel_name = 'channel', message = a_str)
    r.publish_message()

    print(gray)
    
    cv2.imshow('Sending', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#when everything done, release the capture
cap.release()
cv2.destroyAllWindows()