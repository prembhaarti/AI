import urllib2
import urllib
import threading

from bs4 import BeautifulSoup

class WebScrapper:

    # def __init__(self): pass

    def __init__(self, url):
        self.url = url
        self.source = urllib2.urlopen(url)
        self.soup = BeautifulSoup(self.source, "lxml")


    def getSoup(self):
        return self.soup

    def getHtmlByTag(self, tagName):
        return self.soup.find_all(tagName)

    def getHtmlByTagByClass(self, tagName, className):
        return self.soup.find_all(tagName, class_=className)

    def getHtmlByTagById(self, tagName, id):
        return self.soup.find_all(tagName, id=id)

    def getAllLinks(self):
        anchors=self.getHtmlByTag('a')
        links =[]
        for anchor in anchors:
            links.append(anchor.get('href'))
        return links

    def getAllImageLinks(self):
        images = self.getHtmlByTag('img')
        links = []
        for image in images:
            links.append(image.get('src'))
        return links

    def downloadImagesAtPath(self, url, path):
        try:
            print "Downloading image: ", url
            if url.startswith("//"):
                print "url starts with // <- hence aborting download from :", url
            else:
                urllib.urlretrieve(url, path+url.split('/')[-1])
        except Exception:
            print "Unable to download image with url:",url

    def downloadAllImages(self, path):
        imageUrls = self.getAllImageLinks()
        for imageUrl in imageUrls:
            self.downloadImagesAtPath(imageUrl, path)

    def downloadAllImagesInParallel(self, path):
        imageUrls = self.getAllImageLinks()
        threads = []
        for imageUrl in imageUrls:
            thread = threading.Thread(target=self.downloadImagesAtPath, args=(imageUrl, path,))
            threads.append(thread)
            thread.start()