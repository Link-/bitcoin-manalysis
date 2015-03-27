# Reddit Data Scrapper

In order to attain the goal of assessing the impact of news on the bitcoin price, the aggregation of news articles with their respective meta-data is a necessary task to complete.

Reddit is chosen as a focused source of news/events that have been deemed by the community as influencal. What is appealing to this niche 'could' have some form of impact on bitcoin in general given that this group of individuals interested in bitcoin have a solid understanding of the technology, its potential and are, mostly, have vested interests in it.

# Setup

In order to scrap the data from Reddit, it's as simple as calling a url that returns data in JSON format.
For now we're only interest in what made it to the 'hot' section.

	http://reddit.com/r/bitcoin/hot.json
	
Use reddit's API cursor:

	http://reddit.com/r/bitcoin/hot.json?after=t3_30dra4
	
There are no dependencies necessary other than the [Requests](http://docs.python-requests.org/en/latest/) library

	$ pip install requests
	
More information on the installation steps ([Installation](http://docs.python-requests.org/en/latest/user/install/))

