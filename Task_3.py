import requests
import os
from decorator import make_way_to_log

FILE_NAME = 'log_3.txt'
FILE_LOG_DIR = 'logs'
ROOT_PATH = os.getcwd()
full_path = os.path.join(ROOT_PATH, FILE_LOG_DIR, FILE_NAME)

@make_way_to_log(path = full_path)
def the_smartest_hero():
    global name_hero
    url = "https://akabab.github.io/superhero-api/api/all.json"
    res = requests.get(url) # делаем запрос GET на указаный URL
    file = res.json() # присваемаем переменую к pесурсу в формате json
    name_hero_list = ['Hulk', 'Captain America', 'Thanos', 'Ant-Man', 'Deathstroke']
    int = 0
    for x in file:
        if x['name'] in name_hero_list:
            power = x["powerstats"]
            smart_hero = power["intelligence"]
            if smart_hero > int:
                int = smart_hero
                name_hero = x['name']
    return name_hero

if __name__ == "__main__":
    the_smartest_hero()

