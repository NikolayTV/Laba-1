import requests                   #выполняет HTTP-запросы
from bs4 import BeautifulSoup     #работа с HTML
import csv
import re
#работа с форматом данных CSV
from multiprocessing import Pool  #предоставляет возможность параллельных процессов

links = []
html_page = requests.get('http://www.mosigra.ru/').text
soup = BeautifulSoup(html_page, 'lxml')
href = soup.find_all('a', {'href': re.compile('.+')})
for tag in href:
    link = tag['href']
    links.append(link)
print(links)

found = []
found1 = []
found2 = []
found3 = []

mailsrch = re.compile(r'[\w.][\w.]+@[\w][\w\.]+[a-zA-Z]{1,4}')

for link in links:
    if link[0:3] == '//w':
        site = requests.get('http:' + link).text.split(' ')
        for line in site:
            found1 += re.findall(mailsrch, line)

    elif link[0:2] == '//':
        site = requests.get('http:' + link).text.split(' ')
        for line in site:
            found2 += re.findall(mailsrch, line)

    elif link[0] == '/':
        site = requests.get('http://mosigra.ru'+link).text.split(' ')
        for line in site:
            found3 += re.findall(mailsrch, line)
    else:
        pass

    found = found1 + found2 + found3
    found = set(found)
    print(len(found))
    print(found)


