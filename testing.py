import redis

def get_redis():
    return redis.Redis(host='localhost', port=6379, db=0)


def subscribe_channel(channel_name):
    return get_redis().pubsub().subscribe(channel = channel_name)


def publish_message(channel_name, message):
    return get_redis().publish(channel=channel_name, message=message)


ram = subscribe_channel(channel_name='bhajan')
hari = publish_message(channel_name='bhajan', message='hare ram hare ram!')

