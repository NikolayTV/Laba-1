import requests
import re

class Laba1:
    found = []
    def get_emails_from(self, site, html_file): #выгружает сайт
        site = requests.get(site).text
        create_file = open(html_file, 'w', encoding='utf-8') #открываю файл
        create_file.write(site) #загружаю текст в файл
        create_file.close() #закрываю файл
        mailsrch = re.compile(r'[\w.][\w.]+@[\w][\w\.]+[a-zA-Z]{1,4}') #регулярка для поиска емайлов
        with open(html_file, encoding='utf-8') as site: #находит емайлы
            for line in site:
                self.found += (re.findall(mailsrch, line))
        self.found = set(self.found) #Удаляет лишние емайлы
        print(self.found)
    def put_emails_to(self, emails_base1):
        file_email = open(emails_base1, 'w', encoding='utf-8') #создает и выгружает емайлы в файл
        file_email.write('\n'.join(self.found))
        file_email.close()

laba1 = Laba1()

laba1.get_emails_from('http://www.mosigra.ru/', 'mosigra_html.txt')
laba1.put_emails_to('emails_base.txt')
