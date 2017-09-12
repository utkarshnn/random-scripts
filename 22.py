from multiprocessing.pool import ThreadPool
from time import time as timer,time
from urllib2 import urlopen
from datetime import datetime

urls = ['https://www.mrosupply.com/v-belts/urethane-open-end-v-belting/154957_4912066_fenner-drives/',
'https://www.mrosupply.com/v-belts/2385583_21c4140_gates-rubber/',
'https://www.mrosupply.com/v-belts/linked-open-end-v-belting/817585_0408501_fenner-drives/',
'https://www.mrosupply.com/v-belts/178175_a51_gates-rubber/',
'https://www.mrosupply.com/v-belts/linked-open-end-v-belting/155124_0408010_fenner-drives/',


]

def fetch_url(url):
    try:
        response = urlopen(url)
        return url, response.read(), None
    except Exception as e:
        return url, None, e
starttime = time()
start = timer()
results = ThreadPool(100).imap_unordered(fetch_url, urls)
for url, html, error in results:
    if error is None:
        print("%r fetched in %ss" % (url, timer() - start))
        print("Start Time %s" % (datetime.now()))
    else:
        print("error fetching %r: %s" % (url, error))
print("Elapsed Time: %s" % (timer() - start,))

