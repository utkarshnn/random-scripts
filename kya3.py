import threading
import urllib2
import time
from datetime import datetime



start = time.time()
urls = ["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1200,1206)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1206,1210)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1210,1214)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1214,1218)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1218,1222)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1222,1226)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1226,1230)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1230,1234)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1234,1238)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1238,1242)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1242,1246)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1246,1250)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1250,1254)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1254,1258)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1258,1262)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1262,1266)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1266,1270)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1270,1274)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1274,1278)] + \
["https://www.raptorsupplies.com/c/%s" % page for page in xrange(1278,1282)]


left_to_fetch = len(urls)

class FetchUrl(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.setDaemon = True
        self.url = url
        print "Time: %s" % datetime.now() 

    def run(self):
        urlHandler = urllib2.urlopen(self.url)
        html = urlHandler.read()
        finished_fetch_url(self.url)
        print "Time: %s" % datetime.now() 

def finished_fetch_url(url):
    "callback function called when a FetchUrl thread ends"
    print "\"%s\" fetched in %ss" % (url,(time.time() - start))
    global left_to_fetch
    left_to_fetch-=1
    if left_to_fetch==0:
        "all urls have been fetched"
        print "Elapsed Time: %ss" % (time.time() - start)


for url in urls:
    "spawning a FetchUrl thread for each url to fetch"
    FetchUrl(url).start()
