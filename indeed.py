#python3 -m pip install [module_name]
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/취업?q=python&limit={LIMIT}"

def extract_indeed_pages():

    result=requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class":"pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    return pages[-1]

def extract_indeed_jobs(last_page):
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"job_seen_beacon"})

        for result in results:
            print(extract_job(result, page))
            
        
        
def extract_job(html, num):
    title = html.find('a')["aria-label"]
    comp_loc = html.find("div", {"class":"companyInfo"})
    companyName = comp_loc.find("span", {"class" : "companyName"}).string
    companyLocation = comp_loc.find("div", {"class" : "companyLocation"}).string


    job_id = html.find('a')["data-jk"]
    job_link = f"https://kr.indeed.com/viewjob?jk={job_id}"
    info_result = requests.get(job_link)
    jb_soup = BeautifulSoup(info_result.text, "html.parser")
    jb_info = jb_soup.find("div", {"class" : "jobsearch-jobDescriptionText"}).text


    return {'title' : title, 'company' : companyName, 'location' : companyLocation, 'job_info' : jb_info, 'job_link' : job_link}