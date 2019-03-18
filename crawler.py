import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    print('sample')
    page = 1
    while page < max_pages:
        print('inner')
        url = 'http://naver.com'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        page += 1
        print(soup)
    
    

spider(2)
