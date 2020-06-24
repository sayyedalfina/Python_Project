import requests
from bs4 import BeautifulSoup       #bs is a class
import csv

csv_file = open('imdb.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title','Time','Genre','Rating','Description','Director/s','Stars'])

source = requests.get("https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs").text
soup = BeautifulSoup(source,'lxml')         #creating object of Class BeautifulSoup, lxml is a parser that parses the html file
#print(soup.prettify())          #makes the format of text proper

movies = soup.findAll(class_="nm-title-overview-widget-layout")
#print(type(movies))

#prints movie titles
for movie in movies:
    #title = movie.find(class_="overview-top")
    #title = movie.h4
    #print(title.text)
    title = movie.h4.text
    print(title)
    try:
        time = movie.time.text
        print(time)
    except:
        print('None')           #if any movie does not contain time
    #genre = movie.span.text
    #print(genre)
 
    genre = []
    for genres in movie.p.findAll("span"):
        #print(genre.text)
        genre.append(genres.text)
    #print(genre)

#ratings
    try:
        rating = movie.find(class_='rating_txt').span.text       # .find mthd rets a string
        print(rating)
    except:
        rating='None'
        print(rating)

#description 
    try:
        #desc = movie.find(class_='outline')
        #print(desc.text)
        desc = movie.find(class_='outline').text
        print(desc)
    except:
        print('No desc')

#directors

    x=[]
    cast = movie.findAll('div',class_='txt-block')      #we cant use .text with findAll()
    for elmt in cast:
        print(elmt.text)
        x.append(elmt.text)
    #print(x)

    dir=[]
    dir=x[0]

    stars=[]
    stars=x[1]

    print(dir)
    print(stars)
    csv_writer.writerow([title,time,genre,rating,desc,dir,stars])
csv_file.close()
