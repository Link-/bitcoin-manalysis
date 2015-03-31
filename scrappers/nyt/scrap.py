#!/usr/bin/python
# 
# Python News Scrapper
# for the purposes of the bitcoin
# trend analysis excercise
# 
# @version: 0.0.1
# @dependencies: requests
#
# run: 
# $: python scrap.py
#
# Note: This is hacked code 
# in a rush so don't judge
# IT DOES NOT HANDLE ANY 
# EXCEPTION! USE IT AT YOUR
# OWN RISK...
# 
# Data Source: NYTimes Data

import requests
import json
import time
import pprint
from math import ceil
import sys

PARSE_CONF = {'raw_data_dir': '',
				'user-agent': 'Bit-Analyzer:v0.0.1',
				'filename': 'nyt-bitcoin',
				'url': 'http://api.nytimes.com/svc/search/v2/articlesearch',
				'format': 'json',
				'timeout': 10,
				'start_depth': 0,				# you will thank me for this when the request times out
				'depth': 10,					# returns depth+1 pages and start_depth+depth pages
				'sleep_thresh': 3,
				'query': 'bitcoin',
				'sort': 'newest',
				'begin_date': 20090101,			# yyyymmdd
				'end_date': 20150303,			# yyyymmdd
				'api_key': ''}


def request_data(page=0):
	# Craft the URL
	url = '%s.%s?q=%s&begin_date=%s&end_date=%s&sort=%s&page=%d&api-key=%s' % (PARSE_CONF['url'], \
					 	    PARSE_CONF['format'], \
					 	    PARSE_CONF['query'], \
					 	    PARSE_CONF['begin_date'], \
					 	    PARSE_CONF['end_date'], \
					 	    PARSE_CONF['sort'], \
					 	    page, \
					 	    PARSE_CONF['api_key'])

	# Define the user-agent
	headers = {'user-agent': PARSE_CONF['user-agent']}
	# Intialize the request + timeout
	r = requests.get(url, headers=headers, timeout=PARSE_CONF['timeout'])
	# Debugging : Print status code
	print "RESPONSE: %d" % r.status_code
	# Return content
	return r.content

def dump_info_file(content):
	# Define the filename
	curr_filename = '%s%s-%s.%s' % (PARSE_CONF['raw_data_dir'], \
								   PARSE_CONF['filename'], \
								   str(time.time()), \
								   PARSE_CONF['format'])
	# Write content to file
	with open(curr_filename, 'wb') as feed:
		feed.write(content)

def get_data(page=0):
	# Get content
	ir_content = request_data(page)
	# Dump data into a file
	dump_info_file(ir_content)
	# jsonify
	json_content = json.loads(ir_content)
	# Get the after cursor key
	hits = json_content['response']['meta']['hits']
	# Return total number of results
	return int(hits)

def main():
	# Fetching your DATAZ
	print "... FETCHING YOUR DATAZ ..."
	start_depth = PARSE_CONF['start_depth']
	print "START_DEPTH : %d" % start_depth
	# Initial data request
	# Return the total number of results
	# that the query returns
	hits = get_data(start_depth)
	# Calculate the total number of pages
	# to retrieve
	total_pages = ceil(hits / 10)
	# Debuggin purposes
	print "HITS %d : %s" % (hits, total_pages)
	# Check start_depth (although
	# it might be too late here)
	if start_depth > total_pages:
		sys.exit('Start depth too high!')
	# Define depth
	depth = PARSE_CONF['depth']
	# Debugging 
	print "INITIAL DEPTH %d" % (depth)
	# Check the depth if correct
	if total_pages < 1 or depth == 0:
		# Exit because we got all
		# the content we need
		sys.exit(0)
	elif depth > total_pages:
		# Get data up to the 
		# total_pages 
		depth = int(total_pages)
	# Filtered depth
	print "RECALIBRATED DEPTH %d" % (depth)

	# Loop until we reach necessary depth
	for x in xrange(start_depth+1, depth+1):
		print "SLEEPING %d seconds" % (PARSE_CONF['sleep_thresh'])
		# Wait between each request and the
		# because we are nice
		time.sleep(PARSE_CONF['sleep_thresh'])
		# Get data of a given page
		get_data(x)
		# DEBUG
		print "PAGE %d of %d" % (x, depth)

if __name__ == "__main__":
	main()