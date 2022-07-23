from email.mime import base
from email.quoprimime import quote
from urllib.parse import quote_plus #한글 검색어를 컴퓨터 언어로 변환
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = baseurl = 'https://www.google.com/search?q=naver'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #사용할 web이 chrome이라는 뜻
driver.get(url) #request.get

html=driver.page_source #http parser
soup=BeautifulSoup(html, "html.parser")

r = soup.select('.AaVjTc')

for elements in r:
    print(elements.find_element(By.TAG_NAME, 'a'))