#!/usr/bin/python
# 

import json
from pprint import pprint

data_dir = '/Users/bassemd/Projects/bitcoin-manalysis/scrappers/reddit/data/'
filename = '%shot-bitcoin-1427411882.19.json' % (data_dir)

with open(filename) as data_file:    
    data = json.load(data_file)

pprint(data)