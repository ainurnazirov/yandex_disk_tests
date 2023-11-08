import requests


class YandexDiskClient:
    BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources'

    def __init__(self, token):
        self.token = token

    def get_contents(self, path='/', depth=0):
        headers = {'Authorization': f'OAuth {self.token}'}
        url = f'{self.BASE_URL}?path={path}'

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            items = response.json().get('_embedded').get('items', [])

            indent = '\t' * depth

            for item in items:
                print(f"{indent}{item['name']}")

                if item['type'] == 'dir':
                    subpath = item['path']
                    self.get_contents(path=subpath, depth=depth + 1)
            return items
        else:
            return []
