import requests
import re
from bs4 import BeautifulSoup as bs4

def cleanhtml(raw_html):
  cleanr =re.compile('<.*?>')
  cleantext = re.sub(cleanr,'', raw_html)
  return cleantext

url_base_1 = 'http://asheville.craigslist.org/search/tch'
url_base_2 = 'http://asheville.craigslist.org/search/sad'
rsp = requests.get(url_base_1)
rsp_2 = requests.get(url_base_2)

html = bs4(rsp.text, 'html.parser')
html_2 = bs4(rsp_2.text, 'html.parser')

jobs = html.find_all('p', attrs={'class':'row'})
jobs_2 = html_2.find_all('p', attrs={'class':'row'})

pattern = re.compile('/tch/*')
for job in jobs:
    title = job.findAll(attrs={'class': 'hdrlnk'})
    date_search = job.findAll("time")
    date = date_search[0].contents
    date = str(date)
    date = date[3:9]
    title = str(title)
    local_check = re.search('href="/tch/*', title)

    title = cleanhtml(title)

    if local_check is not None:
        print title
        print date
        print '==='

for job in jobs_2:
    title = job.findAll(attrs={'class': 'hdrlnk'})
    date_search = job.findAll("time")
    date = date_search[0].contents
    date = str(date)
    date = date[3:9]
    title = str(title)
    local_check = re.search('href="/sad/*', title)

    title = cleanhtml(title)

    if local_check is not None:
        print title
        print date
        print '==='

