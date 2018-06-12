import re
import os
import codecs
import wget
from datetime import datetime
from core import to_utf8 as fix_str
from core import Actor

NOW = datetime.now()
TODAY = str(NOW.day).zfill(2) + '-' + str(NOW.month).zfill(2) + '-' + str(NOW.year)

CSV_ACTORS_PATH = './resources/csv/' + TODAY + '/data/' 
DATA_PATH = './src/'

def actor_from_url(url):
    actor_url = exists_url(url)
    delete_all_html()
    html = download_html(url, actor_url)
    result = parser(html, actor_url)
    return result

def exists_url(url):
    try:
        return re.findall(r'\.com\/(.*)\/', url)[0]
    except:
        return False

def download_html(url, actor):
    try:
        html = open(wget.download(url=url, out=actor+".html"), 'r').read()
        return html
    except:
        with open(DATA_PATH + 'actores_removidos', 'a') as rmv_actors_file:
            rmv_actors_file.write(url+'\n')
            followers = 0
            posts = 0
            following = 0
            fullname = actor
        return Actor(actor, posts, followers, following, fullname)

def parser(html, actor):
    followers = int(re.findall(r'edge_followed_by":\{"count":(\d+)', html)[0])
    posts = int(re.findall(r'"edge_owner_to_timeline_media":\{"count":(\d+)', html)[0])
    following = int(re.findall(r'"edge_follow":\{"count":(\d+)', html)[0])
    fullname = re.findall(r'"full_name":"(.*?")', html)[0][:-1]
    return Actor(actor, fullname, posts, followers, following)

def delete_all_html():
    try:
        os.system("rm *.html")
    except:
        pass

def create_folder():
    if not os.path.exists(CSV_ACTORS_PATH):
        os.makedirs(CSV_ACTORS_PATH)

def return_list_of_actors():
    actors = []
    with open(DATA_PATH + 'atores_lista', 'r') as list_file:
        for line in list_file:
            actors.append(line[:-1])

    return actors

def write_in_file(filename, data):
    with codecs.open(CSV_ACTORS_PATH + filename + '.csv', 'w', "utf-8") as file:
        file.write('Nome real da conta,Conta,Seguidores,Seguindo,Postagens\n')
        if data.followers != 0:
            string = (fix_str(data.fullname) + ',' + 'https://www.instagram.com/' +
                    fix_str(data.name) + '/,' + str(data.followers) + ',' + str(data.following) + ',' +
                    str(data.posts) + '\n')
        file.write(string)
        file.close()

def collect_data():
    delete_all_html()
    create_folder()
    
    actors = return_list_of_actors()

    for actor in actors:
        actor_data = actor_from_url(actor)
        write_in_file(actor_data.name, actor_data)

    delete_all_html()
