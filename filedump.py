from taxfree import TaxFree
import json

search = TaxFree()

for vine_type in ['rødvin', 'hvitvin', 'rosévin', 'ressertvin', 'musserende', 'sterkvin', 'perlende vin']:
    with open('{}.json'.format(vine_type), 'w') as outfile:
        json.dump(search.search('', 'vin', vine_type), outfile)

with open('beer.json', 'w') as outfile:
    beers = search.search('', 'øl')
    json.dump(beers, outfile)

with open('brennevin.json', 'w') as outfile:
    fortified = search.search('', 'brennevin')
    json.dump(fortified, outfile)
