import requests
from bs4 import BeautifulSoup as BS
import re

def get_links(stock):
    write_links = open('ALL_LINKS.txt', 'a', encoding='utf-8')
    for x in stock:
        new_links = []
        text = requests.get(x).text
        href = BS(text, 'lxml').find_all('a', {'href': re.compile('.+')})

        for tag in href:
            link = tag['href']
            if link[0:13] == '//www.mosigra' and link[-1] == '/' and link[-8:0] != '2017/04/':
                #первое условие чтобы ссылка была с головой
                #второе условия нужно чтобы отсечь ссылки типа //ufa.mosigra.ru/?local где сайт копируется на другой город
                #третье условие для отсечения бесконечного календаря
                new_links.append('http:' + link)
            elif link[0] == '/' and link[-1] == '/' and link[-8:0] != '2017/04/':
                new_links.append('http://mosigra.ru' + link)
        new_adr = []
        for new_link in new_links:
            if new_link not in stock:
                new_adr.append(new_link)
                write_links.write(new_link + '\n')
                stock.append(new_link)
                new_adr.append(new_link)
        print('len(stock)', len(stock))            #количество общего списка ссылок
        print('len(new_links)', len(new_links))    #количество ссылок на странице
        print('len(new_adr)', len(new_adr))        #количество уникальных ссылок на странице

    write_links.close()
    get_links(stock)

def get_emails(file_name):
    read_file = open(file_name, 'r', encoding='utf-8')
    temp = read_file.read().splitlines()
    emails = []
    i = 0
    for x in temp:
        i += 1
        print(i)
        for line in requests.get(x).text.split(' '):
            emails += re.findall(re.compile(r'[\w.][\w.]+@[\w][\w\.]+[a-zA-Z]{1,4}'), line)

        unic_emails = set(emails[:])
        print('len(unic_emails)', len(unic_emails)) #количество уникальных емайлов
        print('len(emails)', len(emails))           #количество всего емайлов

    file_email = open('ALL_emails.txt', 'w', encoding='utf-8')  # создает и выгружает емайлы в файл
    file_email.write('\n'.join(unic_emails))
    file_email.close()
    print('Файл с емайлами успешно создан')
    read_file.close()

get_links(['http://www.mosigra.ru/'])
get_emails('ALL_LINKS.txt')

