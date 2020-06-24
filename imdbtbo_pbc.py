import requests_html
from requests_html import HTMLSession, HTMLResponse, HTML
from bs4 import BeautifulSoup

session = HTMLSession()
response = session.get('https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht').html
source=response.html
soup = BeautifulSoup(source,'lxml')

import csv
import urllib

csv_file = open('imdbtbo_pbc.csv','w')
csv_writer = csv.writer(csv_file, lineterminator='\n')
csv_writer.writerow(['Title','Weekend','Gross','Week'])

block = soup.find('tbody')

titles=[]
weekends=[]
gros=[]
weeks=[]

elements = block.find_all('tr')
for element in elements:

	title = element.find('td', class_='titleColumn')
	titles.append(title.text.strip())		#strip() removes extra spaces
	t=title.text.strip()
	
	weekend = element.find('td', class_='ratingColumn')
	# print(weekend.text)
	weekends.append(weekend.text.strip())
	wk=weekend.text.strip()

	gross = element.find('span', class_='secondaryInfo')
	# print(gross.text)
	gros.append(gross.text.strip())
	g=gross.text.strip()

	week = element.find('td', class_='weeksColumn')
	# print(week.text)
	weeks.append(week.text.strip())
	w=week.text.strip()

	csv_writer.writerow([t,wk,g,w])

print(titles)
print(weekends)
print(gros)
print(weeks)