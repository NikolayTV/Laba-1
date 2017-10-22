import requests
import re

def get_emails_from(site): #выгружает сайт
    global found
    found = []
    for line in requests.get(site).text.split(' '):
        found += re.findall(re.compile(r'[\w.][\w.]+@[\w][\w\.]+[a-zA-Z]{1,4}'), line)
    print(set(found))
    print(len(set(found)))

def put_emails_to(email_base):
    file_email = open(email_base + '.txt', 'w', encoding='utf-8') #создает и выгружает емайлы в файл
    file_email.write('\n'.join(found))
    file_email.close()

get_emails_from(site = 'http://mosigra.ru/')
put_emails_to('emails_base.txt')
