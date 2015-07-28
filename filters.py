#!/usr/bin/env python
'''
  @author: Josh Snider
  Various filters for TvTropes pages.
'''
import httplib
from urlparse import urlparse
import pdb

cats = []

def get_category(url):
  if 'pmwiki.php/' not in url or 'com/' not in url:
    return None
  else:
    #pdb.set_trace()
    url = url[url.index('pmwiki.php/') + 11:]
    url = url[:url.index('/')]
    return url.lower().strip().strip('.')

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
  with open('works2.txt') as f:
    pages = f.readlines()
    pages = [page.strip() for page in pages]
    works = set(page for page in pages if is_work(page))
    cats = list(works)
    works = [work for work in works]
    for work in works:
      print(work)
    #pages = pages[pages.index("http://tvtropes.org/pmwiki/pmwiki.php/Recap/NarutoHuntForUchihaArc") + 1:]
    for page in pages:
      url = urlparse(page)
    #  if not redirects(url.netloc, url.path):
	#	if redirects(url.netloc, url.path):
	#	print(page)

setup()
if __name__ == "__main__":
  main()
