# New York Times Data Scrapper

NewYork Times (NYT) is another source of news articles. They have a good API to use for querying relevant articles and more specifically sort them by their number of views/shares/emailed (which is quite nice!).

# Setup

In order to get articles through the NYTimes API, you need to register a (free) account to request your keys.

[API Overview](http://developer.nytimes.com/page)

__Key Rate Limits__

* 10 Calls per second
* 10,000 Calls per day

Another tool used for analysis is the interactive online [JSON Viewer](http://jsonviewer.stack.hu/)

# Usage

Article Search Request URI (sample):

	http://api.nytimes.com/svc/search/v2/articlesearch.json?q=bitcoin&fq=bitcoin&begin_date=20090101&sort=newest&page=0&api-key=<private key here>
	
###Configuration

There's not much configuration to be done. Open `scrap.py` and modify the following:

	PARSE_CONF = {'raw_data_dir': '<absolute path for a storage directory>',
				'user-agent': '<any user-agent of choice>',
				'filename': '<default filename>',
				'url': '<full API url>',
				'format': 'json',
				'timeout': <timeout in seconds>,
				'start_depth': <start depth>,		
				'depth': <retrieval depth>,
				'sleep_thresh': <sleep threshold in seconds>,
				'query': 'bitcoin',
				'sort': '<newest | oldest>',
				'begin_date': <yyyymmdd>,
				'end_date': <yyyymmdd>,
				'api_key': '<your api key>'}

__A few important things to note:__

* `start_depth` : is used to configure the page number from which to start collecting information. It follows the following rules:
	* `if start_depth > total number of pages` : the execution will be halt with a `sys.exit('error')`
	* otherwise the retrieval will start from the specified page number i.e. start_depth
* `depth` : is used to specify the maximum number of pages to retrieve. It follows the following rules:
	* `if depth = 0` : execution will halt, there's nothing to parse
	* `else if depth > total number of pages` : then depth will take the value of the calculated total number of pages
	* otherwise the retrieval will proceed until the specified depth (number of pages) is reached
	
__Mind the following:__

* The first page has a value of `0` which means when you specify a value for depth it will retrieve `n+1` pages. (example: if depth = 10, the script will retrieve 11 pages)

__Example__


	PARSE_CONF = {'raw_data_dir': '/Users/yourname/bitcoin-manalysis/scrappers/nyt/_raw_data/',
				'user-agent': 'Bit-Analyzer:v0.0.1',
				'filename': 'nyt-bitcoin',
				'url': 'http://api.nytimes.com/svc/search/v2/articlesearch',
				'format': 'json',
				'timeout': 10,
				'start_depth': 0,
				'depth': 10,
				'sleep_thresh': 3,
				'query': 'bitcoin',
				'sort': 'newest',
				'begin_date': 20090101,	
				'end_date': 20150303,
				'api_key': ''}

# Disclaimer

This is a very __VERY__ dirty code. Use it at your own risk (although it shouldn't do anything __that__ weird...)