import uuid
from datetime import datetime
import json
import logging
import redis
from models import User, Channel, Stream
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

    def produce_message(self, channel_id, message):
        message_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()
        message_data = {
            'id': message_id,
            'channel_id': channel_id,
            'message': message,
            'timestamp': timestamp

        }
        self.r.xadd(channel_id, message_data)
        return f"Message produced to stream {channel_id}"

    def list_channels(self):
        channels = self.r.hgetall('channels')
        for channel_id, channel_data in channels.items():
            channel_dict = json.loads(channel_data)
            print(f"Channel ID: {channel_id}, Name: {channel_dict['name']}")

    def publish_message(self, channel_id, message):
        self.r.publish(channel_id, message)
        self.produce_message(channel_id, message)
        print(message)

    def consume_message(self, channel_id):
        messages = self.r.xrange(channel_id)
        stream_messages = []
        for message in messages:
            message_id, message_data = message
            stream_message = Stream(
                id=message_data[b'id'].decode(),
                channel_id=message_data[b'channel_id'].decode(),
                message=message_data[b'message'].decode(),
                timestamp=datetime.fromisoformat(
                    message_data[b'timestamp'].decode())
            )
            stream_messages.append(stream_message)
            self.r.hset(f"stream:{stream_message.id}", mapping=message_data)

        return f"Consumed {len(stream_messages)} messages from stream {channel_id}"

    def subscribe_to_channel(self, channel_id):
        pubsub = self.r.pubsub()
        pubsub.subscribe(channel_id)
        self.consume_message(channel_id)
        print(f"Subscribed to channel '{channel_id}'")

        with open(f"{channel_id}_messages.log", "w") as log_file:
            for message in pubsub.listen():
                if message['type'] == 'message':
                    log_file.write(
                        f"Received message: {message['data'].decode('utf-8')}\n")
                    log_file.flush()

    # This function is for sending messages to all channel users
    def broadcast_message(self, channel_id, message):
        self.publish_message(channel_id, message)
        pubsub = self.r.pubsub()
        pubsub.subscribe(channel_id)
        pubsub.publish(channel_id, message)
        return f"Message broadcasted to channel {channel_id}"



