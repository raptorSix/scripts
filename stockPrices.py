import urllib2
import json


stock_symbols = ['vti','vnq','veu','vxf','bnd','FKINX']

try:
    for symbol in stock_symbols:
        url = 'http://www.google.com/finance/info?q=%s' % symbol
        lines = urllib2.urlopen(url).read().splitlines()
        quote = json.loads(''.join([x for x in lines if x not in ('// [', ']')]))

        print 'ticker: %s \t price: %s \t change: %s' %  (quote['t'], quote['l_cur'], quote['c'])
except urllib2.HTTPError:
    print'error getting quote for: %s' % symbol
