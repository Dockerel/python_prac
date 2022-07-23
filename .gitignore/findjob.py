import requests
from bs4 import BeautifulSoup

url=requests.get("http://www.findjob.co.kr/job/category/areaJob.asp?HidArea=11&HidCate=")

soap=BeautifulSoup(url.text, 'html.parser')

job_class=soap.find("div", {"class":"paginate"})

pages=job_class.find_all('span')

job_nb=[]
for page in pages:
    job_nb.append(page.find('a'))

print(job_nb)