from bs4 import BeautifulSoup
import requests
import time

# finds all news headings from BBC news.
print("")
print("*** Presenting news headings from BBC news. ***")
print('************************************************')
print("")
source_code = requests.get('http://www.bbc.com/news')
html_code = source_code.text
soup = BeautifulSoup(html_code, 'lxml')

headings = soup.find_all('h3')

for i in headings:
    time.sleep(1.5)
    print(i.text)
    print('----------------------------------')
    
