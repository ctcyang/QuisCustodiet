#!/usr/bin/env python
'''
  @author: Josh Snider
  Various filters for TvTropes pages.
'''
import httplib
from urlparse import urlparse
import pdb

cats = []
name = {}

def get_category(url):
  if 'pmwiki.php/' not in url or 'com/' not in url:
    return None
  else:
    #pdb.set_trace()
    url = url[url.index('pmwiki.php/') + 11:]
    url = url[:url.index('/')]
    return url.lower().strip().strip('.')

def get_name(url):
	index = url.rfind('/')
	#print url[index+1:]
	return url[index+1:] 

def is_work(url):
  cat = get_category(url)
  #if cat not in cats:
  #	print url, cat
  return cat in cats

def redirects(host, path):
  try:
    con = httplib.HTTPConnection(host)
    con.request("HEAD", path)
    stat = con.getresponse().status
    return stat == 301 or stat == 302 or stat == 303
  except:
    return False


def setup():
  with open('cats.txt') as catsfile:
    global cats
    cats = catsfile.readlines()
    cats = [cat.strip() for cat in cats]

def main():
	assert(not redirects("tvtropes.org", "/"))
	assert(not redirects("tvtropes.org", "/asdfsadf"))
	assert(not redirects("tvtropes.org","/pmwiki/pmwiki.php/WesternAnimation/SamuraiJack"))
 	assert(redirects("tvtropes.org", "/pmwiki/pmwiki.php/Main/SamuraiJack"))
  #assert(redirects("tvtropes.org", "/pmwiki/pmwiki.php/Main/MurderOne"))
	with open('filteredworks4.txt') as f:
		pages = f.readlines()
		pages = [page.strip() for page in pages]
		#works = set(page for page in pages)
		#cats = list(works)
		#works = [work for work in works]
		#for work in works:
		#	print(get_name(work))
		for page in pages:
			name[get_name(page)] = page
			#print(get_name(page))
	count = 0;
	with open('filteredworks.txt') as g:
		pages = g.readlines()
		pages = [page.strip() for page in pages]
		for page in pages:
			if get_name(page) not in name:
				count += 1;
				print page
	print count
    #  if not redirects(url.netloc, url.path):
	#	if redirects(url.netloc, url.path):
	#	print(page)

setup()
if __name__ == "__main__":
  main()
