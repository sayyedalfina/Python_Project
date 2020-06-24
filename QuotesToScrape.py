import requests_html
from requests_html import HTMLSession, HTMLResponse, HTML
from bs4 import BeautifulSoup

import csv
import urllib

urls=[]
for i in range(1,11):
	urls.append(f'http://quotes.toscrape.com/page/{i}/')
c=1

csv_file = open('quotesnew.csv','w')
csv_writer = csv.writer(csv_file, lineterminator='\n')
csv_writer.writerow(['Quotes','Authors','Tags'])

for url in urls:

	session = HTMLSession()
	response = session.get(url).html
	source=response.html

	soup = BeautifulSoup(source,'lxml')

	block = soup.find('div')

	elements = block.find_all('div', class_='quote')
	# print(element.text)

	quotes=[]
	authors=[]
	tags=[]

	for element in elements:

		quote = element.find('span', class_='text').text
		quotes.append(quote)
		#print(quote.text)

		author = element.find('small').text
		authors.append(author)
		#print(author.text)

		tagbox = element.find('div', class_='tags')
		tag = tagbox.find_all('a', class_='tag')
		tags_text = []
		for t in tag:
			#print(t.text, end=',')
			tags_text.append(t.text)
		tags.append(tags_text)
		print(c,end=' ')
		c=c+1
		
		csv_writer.writerow([quote,author,tags_text])

# print(quotes)
# print(authors)
# print(tags)