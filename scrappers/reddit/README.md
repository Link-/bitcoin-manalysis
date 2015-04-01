# Reddit Data Scrapper

In order to attain the goal of assessing the impact of news on the bitcoin price, the aggregation of news articles with their respective meta-data is a necessary task to complete.

Reddit is chosen as a focused source of relevant news that have been deemed by the community as influencal. What is appealing to this niche 'could' have some form of impact on bitcoin in general given that this group of individuals interested in bitcoin have a solid understanding of the technology, its potential and have, in general, a vested interests in the digital currency.

# Setup

In order to scrap the data from Reddit, the process is as simple as calling a url that returns data in JSON format.
For now we're only interest in what made it to the 'hot' section.

	http://reddit.com/r/bitcoin/hot.json
	
Use reddit's API `after` tag to traverse the data:

	http://reddit.com/r/bitcoin/hot.json?after=t3_30dra4
	
There are no dependencies necessary other than the [Requests](http://docs.python-requests.org/en/latest/) library

	$ pip install requests
	
More information on the installation steps for _requests_ ([Installation](http://docs.python-requests.org/en/latest/user/install/))

# Usage

There's not much configuration to be done. Open `scrap.py` and modify the following:

	DATA_DIR = '<absolute path for a storage directory>'

	PARSE_CONF = {'user-agent' : '<user-agent as defined by Reddit Rules>',
				  'filename' : '<default filename>',
				  'subreddit': '<full subreddit url>',
				  'flair': '<hot | new | top>',
				  'format': 'json',
				  'timeout': <timeout in seconds>,
				  'depth': <retrieval depth>,
				  'sleep_thresh': <sleep threshold in seconds>}
							
__Example__:

	DATA_DIR = '/Users/yourname/bitcoin-manalysis/scrappers/reddit/_raw_data/'
	
	PARSE_CONF = {'user-agent' : 'Bitcoin-analysis:v0.0.1 (by /u/Link-)',
				  'filename' : 'hot-bitcoin',
				  'subreddit': 'http://www.reddit.com/r/bitcoin/',
				  'flair': 'hot',
				  'format': 'json',
				  'timeout': 10,
				  'depth': 10,
				  'sleep_thresh': 3}