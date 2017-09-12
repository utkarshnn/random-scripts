from multiprocessing.pool import ThreadPool
from time import time as timer,clock
from urllib2 import urlopen

urls = ["https://www.raptorsupplies.com/c/%s" % page for page in xrange(2200,2222)]

def fetch_url(url):
    try:
        response = urlopen(url)
        return url, response.read(), None
    except Exception as e:
        return url, None, e
starttime = clock()
start = timer()
results = ThreadPool(100).imap_unordered(fetch_url, urls)
for url, html, error in results:
    if error is None:
        print("%r fetched in %ss" % (url, timer() - start))
        print("Start Time %s" % (starttime))
    else:
        print("error fetching %r: %s" % (url, error))
print("Elapsed Time: %s" % (timer() - start,))

