#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import codecs
import urllib2
import unicodedata as ud
import pprint


# pagecontent = urllib2.urlopen('http://www.college.columbia.edu/bulletin')
# soup = BeautifulSoup(pagecontent.read().decode("utf8"))

# for d in soup.find_all('div', style='margin-left: 50%;'):
# 	print d.get_text()


query_params = { 'word' : 'finder'} # 3200 is maximum

r = requests.get(url='http://rhymebrain.com/talk?function=getRhymes', params = query_params)
results = r.json()

i = 0

# for res in results:
for n in range(0, 5):
	# print i, res['word']
	print i, results[n]['word']
	i += 1