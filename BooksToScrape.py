from requests_html import HTMLSession, HTMLResponse
import urllib.request

session = HTMLSession()     #creates obj of htmlsession n stores into session
urls = ['http://books.toscrape.com/catalogue/page-1.html']

for i in range(1,2):
	urls.append('http://books.toscrape.com/catalogue/page-{i}.html')
for url in urls:
    response = session.get(url)
    #print(response)
    #print(response.text)

    source = response.html      #store html file in response
    #print(type(source))
    #print(source)       #gives url
    #print(source.html)

    block = source.find('ol.row',first=True)    #first=True  ==> block[0]
    #print(block)

    names = block.find('li h3 a',first=True)
    print(names.attrs['title'])
    #print(names.text)........ gives the content of <a> tag

    #names = block.find('li h3 a',first=True)
    #print(names.attrs['href'])

    titles=[]
    cost=[]

    #displays list of book title
    print('list of titles\n')
    names = block.find('li h3 a')
    for name in names:
        print(name.attrs['title'])
        titles.append(name.attrs['title'])

    #displays list of book links
    print('\nlist of links\n')
    names = block.find('li h3 a')
    for name in names:
        print(name.attrs['href'])
        


    #price = block.find('p.price_color',first=True)
    #print(price.text)

    #displays list of prices
    print('\nlist of prices\n')
    prices = block.find('p.price_color')
    for price in prices:
        #print(price.text)
        print(price.text[1:])       #removing 1st euro sign using slicing
        cost.append(price.text[1:])

    print('\n\n\nCollection of titles\n\n')
    for i in range(len(titles)):
        print(titles[i])
    print('\n\n\nTheir costs\n\n')
    for i in range(len(cost)):
        print(cost[i])

    #displays =>1000 results - showing 1 to 20. 
    x = source.find('div.row form.form-horizontal',first=True)
    print(x.text)



    #image = block.find('li div.image_container img',first=True)
    #print(image.attrs['src'])
    x = 'http://books.toscrape.com/'
    img=[]
    images = block.find('li div.image_container img')
    for image in images:
        print(image.attrs['src'])
        img.append(x+image.attrs['src'])

    print('\n\nPrints src of images\n\n')
    for i in range(len(img)):
        print(img[i])
        urllib.request.urlretrieve(img[i],titles[i])            #dwnlds the images and saves it with the title name
