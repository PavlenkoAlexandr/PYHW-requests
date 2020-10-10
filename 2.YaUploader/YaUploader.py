import requests
import urllib.parse
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        HEADERS = {'Authorization': f'OAuth {self.token}'}
        path = urllib.parse.quote(os.path.basename(file_path))
        response = requests.get(
            'https://cloud-api.yandex.net/v1/disk/resources/upload',
            params={'path': path, 'overwrite': 'true'},
            headers=HEADERS,
        )
        URL = response.json()['href']
        upload = requests.put(URL, headers={'url': urllib.parse.quote(file_path)})
        return print(f'Файл {path} успешно загружен! {upload.status_code}')
