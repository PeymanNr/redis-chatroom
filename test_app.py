import subprocess
import time
import unittest
from app import RedisClient


class TestRedisClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = RedisClient()

    @classmethod
    def tearDownClass(cls):
        cls.client.r.flushdb()

    def test_publish_message(self):
        channel_id = "test_channel"
        message = "Test Message"

        self.client.subscribe_to_channel(channel_id)
        response = self.client.publish_message(channel_id, message)
        self.assertIn("Message published to channel", response)

        messages = self.client.r.xrange(channel_id)
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0][1][b'message'].decode(), message)

    def test_subscribe_to_channel(self):
        channel_id = "test_channel"
        message = "Test Message"

        process = subprocess.Popen(['python', '-c',
                                    f"from app import RedisClient; client = RedisClient(); client.subscribe_to_channel('{channel_id}')"])
        time.sleep(1) 

        self.client.publish_message(channel_id, message)
        time.sleep(1)

        process.terminate() 

        # Check the log file for the message
        with open(f"{channel_id}_messages.log", "r") as log_file:
            log_content = log_file.read()
            self.assertIn(f"Received message: {message}", log_content)


if __name__ == '__main__':
    unittest.main()
