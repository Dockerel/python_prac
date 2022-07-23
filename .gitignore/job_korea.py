import requests
from bs4 import BeautifulSoup

job_kr = requests.get("https://www.jobkorea.co.kr/Search/?stext=python&tabType=recruit")

job_kr_soup = BeautifulSoup(job_kr.text, 'html.parser')

jk_pagination = job_kr_soup.find("div", {"class":"tplPagination newVer wide"})
#soup.find(id="link3")

jk_li = jk_pagination.find_all('li')

jk_pages = []

for page in jk_li:
    jk_pages.append(page.find('a'))

print(jk_pages[1:])