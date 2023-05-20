import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup



def get_url(position, location):
    template = 'https://www.indeed.com/jobs?q={}&l={}'
    url = template.format(position, location)
    return url

url = get_url('technical writer', 'texas')

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

cards = soup.find_all('div', {'class':'job_seen_beacon'})

print(len(cards))