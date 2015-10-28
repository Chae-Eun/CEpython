from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urljoin
import urllib
import webbrowser

html_doc= """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>"""

soup = BeautifulSoup(html_doc, "html.parser")
#print(soup.prettify())
#print(soup.a.prettify())
#print(soup.html.head.title)
#print(soup.title)
#print(soup.title.string)

#맨 처음 p태그만 나옴
#print(soup.p)
#처음 p태그의 class를 보여줌
#print(soup.p['class'])

#print(soup('a'))
#print(soup('a',{'id':'link2'}))
#print(soup('a')[0].parent)
#print(soup('a')[0].parent.name)
#print(soup('a')[0].contents)
#print(soup.find_all('p'))

#기능이 같음
#print(soup.find_all(class_='sister'))
#print(soup.findAll(class_='sister'))

url = "http://comic.naver.com/webtoon/list.nhn?titleId=650304&weekday=tue"
data = urlopen(url)
soup2 = BeautifulSoup(data, 'html.parser')
cartoons = soup2.find_all('td', {'class' : 'title'})

#for i in range(len(cartoons)):
#    title = cartoons[i].find('a').string
#    ref = cartoons[i].find('a')['href']
#    tempurl = urljoin(url, ref)
#    print(title, " ", tempurl)

#webbrowser.open_new(tempurl)

class crawler:
    def crawl(self, pages, depth=2):
        for i in range(depth):
            newpage = set()
            for page in pages:
                try:
                    c = urllib.request.urlopen(page)
                except:
                    print("Could not open %s" %page)
                    continue
                #인코딩이 안될 떄 from_encoding 사용
                soup = BeautifulSoup(c.read(), from_encoding="utf-8")
                print('Found %s' %page)
            links = soup('a')
            for link in links:
                if('href' in dict(link.attrs)):
                    url = urllib.parse.urljoin(page, link['href'])
                    if url.find("'")!=-1 : continue
                    url = url.split("#")[0]
                    if url[0:4]=='http':
                        newpage.add(url)
            pages = newpage

pagelist=['http://www.naver.com']
crawler=crawler()
crawler.crawl(pagelist)