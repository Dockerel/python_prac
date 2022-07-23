#python3 -m pip install [module_name]
import requests
from bs4 import BeautifulSoup
from indeed import extract_indeed_jobs, extract_indeed_pages #한글 검색어를 컴퓨터 언어로 변환å
from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_page = extract_indeed_pages()

indeed_jobs = extract_indeed_jobs(last_indeed_page)