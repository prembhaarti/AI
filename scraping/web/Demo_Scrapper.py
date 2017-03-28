#import the library used to query a website
import urllib2

# import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

# specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

# Query the website and return the html to the variable 'page'
page = urllib2.urlopen(wiki)

# Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, "lxml")

webPageSource = soup.prettify()

# print soup.title
# print soup.title.name
# print soup.title.string
#
# print soup.title.parent.name
#
# print soup.a
#
# anchorList = soup.find_all('a')
#
# for anchor in anchorList:
#     print anchor.get('href')
#

# print soup.get_text()
# tables=soup.find_all('table')

tables=soup.find_all('table',class_='wikitable sortable plainrowheaders')
print len(tables)
print tables