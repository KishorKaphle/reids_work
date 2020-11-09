import redis
import numpy as np


# https://stackoverflow.com/questions/48700275/imdecode-returns-none-python-opencv2


r = redis.Redis(host='localhost', port=6379, db=0)
p = r.pubsub()
p.subscribe('channel')
#r.publish('channel', 'go!')



while True:
    message = p.get_message()
    if message:
        if message['data'] !=1:
            a = (message['data'])
            #a = a.decode('utf-8')
            a = np.fromstrin(a, dtype=np.int)
            #a = a.reshape(3, 3)
            #print (a)
            
            #data = data.decode('utf-8')
            #data = message['data'].decode()
            #message = str(message['data']).decode()
            #data = str(message['data'])
            #data = np.frombuffer(base64.binascii.a2b_base64(data.encode('utf-8')))
            #data = data.reshape(384, 100)
            #message = message.decode('utf-8')
            #message = np.frombuffer(base64.binascii.a2b_base64(message.encode('ascii')))
            display_image(data)
            
            print(a.shape)
            print(len(a))
            #print (data)
    #time.sleep(1)



