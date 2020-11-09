import redis
from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt


r = redis.Redis(host='localhost', port=6379, db=0)
p = r.pubsub()
p.subscribe('channel')
    
        
while(True):
    message = p.get_message()
    if message:
        if message['data'] !=1:
            data = (message['data'])
            nparr = np.frombuffer(data, np.uint8)
            data = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            cv2.imshow('receiving', data)
            print(data)
    
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

#when everything done
cv2.destroyAllWindows()