import os
import pytest
from dotenv import load_dotenv
from api_tests.clients.yandex_disk_client import YandexDiskClient


@pytest.fixture
def yandex_disk_client():
    load_dotenv()
    token = os.environ.get('YANDEX_API_TOKEN')
    return YandexDiskClient(token)


class TestAPI:
    def test_get_yandex_disk_contents(self, yandex_disk_client):
        contents = yandex_disk_client.get_contents()
        assert len(contents) > 0, 'Content list is empty'