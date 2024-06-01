from app import RedisClient
from models import Channel, User

redis_client = RedisClient()


if __name__ == "__main__":
    while True:
        commands = ["send", 'leave',
                    'join', 'channels', 'quit']
        command = input("what are you command: ")
        if command not in commands:
            print('command you entered is wrong')

        if command == 'send':
            user_id = input("Enter your user ID: ")
            user = redis_client.get_user(user_id)
            if not user:
                print("User not found")
                continue

            channel_id = input("Enter the channel ID: ")
            channel = redis_client.get_channel(channel_id)
            if not channel:
                print('Channel not found')
                continue

            message = input("Type the message to publish in channel: ")
            redis_client.publish_message(channel_id=channel_id, message=message)

        elif command == 'join':
            user_id = input("Enter your user ID: ")
            username = input("Enter your username: ")
            user = User(id=user_id, username=username)
            redis_client.save_user(user)
            channel_id = input("Enter the channel ID: ")
            channel_name = input("Enter the channel name: ")
            channel = Channel(id=channel_id, name=channel_name)
            redis_client.save_channel(channel)
            redis_client.subscribe_to_channel(channel_id=channel_id)

        elif command == 'channels':
            redis_client.list_channels()

        elif command == 'quit':
            print("Exiting chat room.")
            break
