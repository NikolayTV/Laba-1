import datetime
import time
from queue import Queue
from threading import Thread
import requests
from bs4 import BeautifulSoup


def get_posts(link, o4ered):
    while True:
        PageHTML = requests.get(link).text
        Soup = BeautifulSoup(PageHTML, "html.parser")
        bomb = []
        for i in Soup.find_all("div", "post-details"):
            title = []
            annotation = []

            for titles in i.find_all("a", "title"):
                title = titles.get_text()
            for subtitle in i.find_all("p", "subtitle"):
                annotation = subtitle.get_text()
            category = i.a.get_text()
            if title:
                bomb.append({"Title:": title[5:-3], "Annotation:": annotation, "Category:": category[4:-2]})
                if title not in all_titles:
                    all_titles.add(title)

                    o4ered.put({'Category:': category[4:-2],
                                'Title:': title[5:-3],
                                'Annotation:': annotation})
    time.sleep(300)  # каждые 5 минут проверяет новые новости


o4ered = Queue()
link = 'https://futurism.com/'
thread = Thread(target=get_posts, args=(link, o4ered))
thread.start()
all_titles = set()
while True:
    if o4ered.empty():
        time.sleep(300)  # проверяет очередь на новости каждые 5 минут
        print("Новых новостей нет! Проверьте чуть позже" + "\n\n\t\t\t\t\t *******")

    else:
        while not o4ered.empty():
            print(o4ered.get())
            print(datetime.datetime.now())
