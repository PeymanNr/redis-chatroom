import json
import logging
import redis
from models import User, Channel
from redis_config import REDIS_HOST, REDIS_PORT, REDIS_DB


class RedisClient:
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB):
        self.r = redis.Redis(host=host, port=port, db=db)
        logging.debug('Redis client initialized')
        # self.r.flushdb()
        # logging.warning("Redis client flushed")

    def save_user(self, user):
        self.r.hset("users", user.id, json.dumps(user.__dict__))

    def get_user(self, user_id):
        user_data = self.r.hget("users", user_id)
        if user_data:
            user_dict = json.loads(user_data)
            return User(**user_dict)
        return None

    def save_channel(self, channel):
        self.r.hset("channels", channel.id, json.dumps(channel.__dict__))

    def get_channel(self, channel_id):
        channel_data = self.r.hget("channels", channel_id)
        if channel_data:
            channel_dict = json.loads(channel_data)
            return Channel(**channel_dict)
        return None

    def list_channels(self):
        channels = self.r.hgetall('channels')
        print(channels)

    def publish_message(self, channel_id, message):
        self.r.publish(channel_id, message)
        print(message)

    def subscribe_to_channel(self, channel_id):
        pubsub = self.r.pubsub()
        pubsub.subscribe(channel_id)
        print(f"Subscribed to channel '{channel_id}'")

        for message in pubsub.listen():
            if message['type'] == 'message':
                print(f"Received message: {message['data'].decode('utf-8')}")


