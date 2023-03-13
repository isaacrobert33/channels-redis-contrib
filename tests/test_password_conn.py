from channels_redis_contrib.core import RedisChannelLayer
from dotenv import load_dotenv
import pytest, os

load_dotenv()

TEST_HOSTS = ["redis://{os.getenv('REDIS_HOST)}:6379"]
PASSWORD = os.getenv("REDIS_PASSWORD")


@pytest.fixture()
async def password_channel_layer():
    """
    Channel layer fixture that flushes automatically.
    """
    channel_layer = RedisChannelLayer(
        hosts=TEST_HOSTS, capacity=3, channel_capacity={"tiny": 1}, password=PASSWORD
    )
    yield channel_layer
    await channel_layer.flush()
