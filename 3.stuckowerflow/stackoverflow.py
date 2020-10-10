import requests
import time

def get_questions():
    date = int(time.time())
    PARAMS ={
        'order': 'desc',
        'sort': 'activity',
        'site': 'stackoverflow',
        'tagged': 'python'
         }
    response = requests.get('https://api.stackexchange.com/2.2/questions', params=PARAMS)
    for item in response.json()['items']:
        creation_date = item['creation_date']
        if creation_date < date - 172800:
            continue
        else:
            print(item['title'] + '\n' + item['link']+ '\n')

get_questions()
