import json
import redis
from models import User, Channel
from redis_config import REDIS_HOST, REDIS_PORT, REDIS_DB


def connect():
    try:
        client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB
        )

        return client

    except Exception as e:
        print("Error connecting to Redis server:", e)


def save_user(user):
    client = connect()
    client.hset("users", user.id, json.dumps(user.__dict__))


def get_user(user_id):
    client = connect()
    user_data = client.hget("users", user_id)
    if user_data:
        user_dict = json.loads(user_data)
        return User(**user_dict)
    return None


def save_channel(channel):
    client = connect()
    client.hset("channels", channel.id, json.dumps(channel.__dict__))


def get_channel(channel_id):
    client = connect()
    channel_data = client.hget("channels", channel_id)
    if channel_data:
        channel_dict = json.loads(channel_data)
        return Channel(**channel_dict)
    return None


def publish_message(channel_id, message):
    client = connect()

    client.publish(channel_id, message)
    print(message)


def subscribe_to_channel(channel_id):
    client = connect()
    pubsub = client.pubsub()
    pubsub.subscribe(channel_id)
    print(f"Subscribed to channel '{channel_id}'")

    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Received message: {message['data'].decode('utf-8')}")


if __name__ == "__main__":
    while True:
        commands = ["send", 'leave',
                    'join', 'channels', 'quit']
        command = input("what are you command: ")
        if command not in commands:
            print('command you entered is wrong')

        if command == 'send':
            user_id = input("Enter your user ID: ")
            user = get_user(user_id)
            if not user:
                print("User not found")
                continue

            channel_id = input("Enter the channel ID: ")
            channel = get_channel(channel_id)
            if not channel:
                print('Channel not found')
                continue

            message = input("Type the message to publish in channel: ")
            publish_message(channel_id=channel_id, message=message)

        elif command == 'join':
            user_id = input("Enter your user ID: ")
            username = input("Enter your username: ")
            user = User(id=user_id, username=username)
            save_user(user)
            channel_id = input("Enter the channel ID: ")
            channel_name = input("Enter the channel name: ")
            channel = Channel(id=channel_id, name=channel_name)
            save_channel(channel)
            subscribe_to_channel(channel_id=channel_id)

        elif command == 'quit':
            print("Exiting chat room.")
            break
