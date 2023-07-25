import urllib.request, json
url = "https://api.semanticscholar.org/graph/v1/paper/6fe5d5713b626139f880925188980ec95a82a631?fields=venue,year,title,authors.name,citationCount,citations.title,citations.authors,citations.year,citations.publicationTypes,citations.venue,citations.url,citations.openAccessPdf,citations.externalIds"

import requests
r = requests.get(url)
jsondata = r.json()
print(jsondata) # if response type was set to JSON, then you'll automatically have a JSON response here...

print('Data')
print(jsondata['title'])
print(jsondata['venue'])
print(jsondata['year'])
print(jsondata['citationCount'])

print(jsondata['authors'][0]['name'])

citations = jsondata['citations']
print(citations)
