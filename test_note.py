from numpy import array
import numpy as np 
from cv2 import cv2
import redis
import base64
import datetime


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
    gray = np.array(gray)
    print(gray)
    to_sent = gray.flatten()
    
    #print(to_sent.shape)
   

    a_str = base64.binascii.b2a_base64(to_sent).decode('ascii')
    
    # get time stamp for the getting the individual image in the process 2
    #frame = str(datetime.datetime.now())
    r = RedisWork(channel_name = 'channel', message = a_str)
    #r.get_redis().set('frame', frame)
    r.publish_message()
    #r.set('channel', a_str)
    

    #Display the resulting frame
    cv2.imshow('frame', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#when everything done, release the capture
cap.release()
cv2.destroyAllWindows()