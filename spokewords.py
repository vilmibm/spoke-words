#!/usr/bin/python
# usage: spokewords.py <search query>

from yahoo.search.web import *
from urllib2 import *
from random import randint
from strip_html import strip_html
import sys
import re

js   = re.compile(r"<script.*?>.*</script>", re.DOTALL)
css  = re.compile(r"<style.*?>.*</style>", re.DOTALL)  
tags = re.compile(r"<.*?>", re.DOTALL)
ws   = re.compile(r"\s\s+", re.DOTALL)
char = re.compile(r"&.*?;", re.DOTALL)

def cleanUp( data ):
  data = js.sub('', data)
  data = css.sub('', data)
  data = strip_html(data)
  data = ws.sub(' ', data)
  return data

num_src = 20
query   = 'william s burroughs'
final = ''
min_len = 100
max_len = 350

if len(sys.argv) > 1:
  query = sys.argv[1]

search = WebSearch('xfVvWAzV34EPucXC8AWocPsC_qJ93o_ntZ7OdbvlPXRCXvvG6RDqvg3nTLOc.qlN')
search.query = query
search.results = 50 

results = search.parse_results(search.get_results())

urls = []
sources = []

for r in results:
  urls += [r.Url]

while len(sources) < num_src and len(urls) > 1:
  index = randint(0,len(urls)-1)
  url = urls[index]
  urls.remove(url)
  try:
    f = urlopen(url)
    data = f.readlines()
    sources.append( cleanUp(reduce(lambda x,y:x+y, data)) )
  except UnicodeDecodeError:
    continue
  except HTTPError:
    continue
  except URLError:
    continue

# We now have sources, a list of num_src pieces of text
# for us to cut up and rearrange.

lines = []
for src in sources:
  start = randint(0, abs(len(src)-max_len))
  end = randint(start+min_len, start+max_len) 

  sample = src[start:end]

  lines += sample.split('. ')

# now have lines, a list of "sentences" from the samples
# of sources.
while len(lines) > 0:
  try:
    index = randint(0,len(lines)-1)
    line = lines[index]
    final += line
    lines.remove(line)
  except UnicodeDecodeError:
    lines = lines[0:index] + lines[index+1:]

final_final = ''
for c in final:
  if ord(c) < 127:
    final_final += c

final = final_final
print final
      
