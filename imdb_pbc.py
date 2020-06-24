import requests_html
from requests_html import HTMLSession, HTMLResponse, HTML

session = HTMLSession()
source = session.get('https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm').html

block = source.find('tbody.lister-list')[0]
#find() returns a list, but it cant be applied to a list
tit=[]
titles = block.find('tr td.titleColumn a')
for title in titles:
	#print(title.text)
	tit.append(title.text)

rating = []
#ratings = block.find('tr td.ratingColumn.imdbRating strong')
ratings = block.find('tr td.ratingColumn.imdbRating')
for r in ratings:
	rating.append(r.text)
	#print(r.text)

years = []
year = block.find('tr td.titleColumn span.secondaryInfo')
for y in year:
	#print(year.text)
	years.append(y.text)

for i in range(len(tit)):
	print(tit[i])
	print(rating[i])
	print()

# for i in rating:
# 	print(i)
