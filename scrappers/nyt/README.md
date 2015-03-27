# New York Times Data Scrapper

In order to attain the goal of assessing the impact of news on the bitcoin price, the aggregation of news articles with their respective meta-data is a necessary task to complete.

New York Times (NYT) is another source of news articles. They have a good API to use for querying relevant articles and more specifically sort them by their number of views/shares/emailed (which is quite nice!).

# Setup

In order to get articles through the NYTimes API, you need to register for a (free) account in order to request your keys.

[API Overview](http://developer.nytimes.com/page)

Another tool used for analysis is the interactive online [JSON Viewer](http://jsonviewer.stack.hu/)

# Usage

Article Search Request URI (sample):

	http://api.nytimes.com/svc/search/v2/articlesearch.json?q=bitcoin&fq=bitcoin&begin_date=20090101&sort=newest&page=0&api-key=<private key here>
	
