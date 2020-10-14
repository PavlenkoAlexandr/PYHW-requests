import requests
from urllib.parse import urljoin

BASE_URL = 'https://api.vk.com/method/'
TOKEN = ''
V = '5.21'


class User:

    def __init__(self,id, token=TOKEN, version=V):
        self.id = id
        self.token = token
        self.version = version

    def __str__(self):
        return self.get_user_url()

    def get_user_url(self):
        method = 'users.get'
        users_get_url = urljoin(BASE_URL, method)
        response = requests.get(users_get_url, params={
            'access_token': self.token,
            'v': self.version,
            'user_id': self.id,
            'fields': 'domain'
        })
        domain = response.json()['response'][0]['domain']
        user_url = urljoin('https://vk.com/', domain)
        return user_url

    def get_friends(self):
        method = 'friends.get'
        get_friends_url = urljoin(BASE_URL, method)
        response = requests.get(get_friends_url, params={
            'access_token': self.token,
            'v': self.version,
            'user_id': self.id,
            'fields': 'domain'
        })
        for friend in response.json()['response']['items']:
            print(urljoin('https://vk.com/', friend['domain']))

    def __and__(self, other):
        mutual_friends = list()
        method = 'friends.getMutual'
        friends_get_mutual_url = urljoin(BASE_URL, method)
        response = requests.get(friends_get_mutual_url, params={
            'access_token': self.token,
            'v': self.version,
            'source_uid': self.id,
            'target_uid': other.id,
        })
        print(response.json())
        friend=dict()
        for id in response.json()['response']:
            friend[id] = User(str(id))
            mutual_friends.append(friend[id])
        return mutual_friends
