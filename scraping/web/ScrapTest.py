from WebScrapper import *

# scrap = WebScrapper()
scrap = WebScrapper("http://www.dummies.com/programming/python/how-to-create-a-constructor-in-python/")
# anchors = scrap.getHtmlByTag('a')
# tables = scrap.getHtmlByTagByClass('table', 'wikitable sortable plainrowheaders')
# print len(tables)
#
# links = scrap.getAllImageLinks()
#
#
# # images=scrap.getSoup().find('img')
# # print images
# print links

# scrap.downloadImagesAtPath("https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/All_Gizah_Pyramids.jpg/300px-All_Gizah_Pyramids.jpg","/home/prembharti/images/");
# scrap.downloadAllImages("/home/prembharti/images/")

scrap.downloadAllImagesInParallel("/home/prembharti/images/")