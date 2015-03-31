# New York Times Data Scrapper

In order to attain the goal of assessing the impact of news on the bitcoin price, the aggregation of news articles with their respective meta-data is a necessary task to complete.

New York Times (NYT) is another source of news articles. They have a good API to use for querying relevant articles and more specifically sort them by their number of views/shares/emailed (which is quite nice!).

# Setup

In order to get articles through the NYTimes API, you need to register for a (free) account in order to request your keys.

[API Overview](http://developer.nytimes.com/page)

__Key Rate Limits__

* 10 Calls per second
* 10,000 Calls per day

Another tool used for analysis is the interactive online [JSON Viewer](http://jsonviewer.stack.hu/)

# Usage

Article Search Request URI (sample):

	http://api.nytimes.com/svc/search/v2/articlesearch.json?q=bitcoin&fq=bitcoin&begin_date=20090101&sort=newest&page=0&api-key=<private key here>
	

	PARSE_CONF = {'raw_data_dir': '<directory>',
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

__Example__


	PARSE_CONF = {'raw_data_dir': '/Users/yourname/bitcoin-manalysis/scrappers/nyt/_raw_data/',
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

## Risk

This is a very VERY dirty code. Use it at your own risk (although it shouldn't do anything that weird...)