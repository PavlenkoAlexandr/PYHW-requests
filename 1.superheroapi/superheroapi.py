import requests

def find_hero(name, search):
    hero=[]
    try:
        response = requests.get('https://www.superheroapi.com/api/2619421814940190/search/' + search)
        for data in (response.json()['results']):
            if data['name'] == name:
                hero.append(name)
                hero.append(data['powerstats'])
                return hero
            else:
                print(f'oops! {name} not found!')
    except KeyError:
        print('Неверный поисковый запрос!')


captain_america = find_hero('Captain America', 'america')
hulk = find_hero('Hulk', 'hulk')
thanos = find_hero('Thanos', 'thanos')


def max_stats(*args, stat):
    compair_dict = dict()
    for arg in args:
        if type(arg) == list:
            compair_dict[arg[0]] = arg[1][stat]
    max_stat = sorted(compair_dict.items(), key=lambda x: x[1])[0]
    return max_stat

max_intelligence = max_stats(hulk, thanos, captain_america, stat='intelligence')

print(max_intelligence)
