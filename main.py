import BeautifulSoup
import urllib2

url = 'https://scrapebook22.appspot.com/'

response = urllib2.urlopen(url).read()

soup = BeautifulSoup.BeautifulSoup(response)

print soup.html.head.title.string  # should be: Scrapebook | by SmartNinja

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        person_html = urllib2.urlopen(person_url).read()
        person_soup = BeautifulSoup.BeautifulSoup(person_html)
        print person_soup.find("span", attrs={"class": "email"}).string
