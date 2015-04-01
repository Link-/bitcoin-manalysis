    @version: 0.1.2

This analysis **(a work in progress)** is an attempt to find a relationship between bitcoin related news and the rise or fall of the bitcoin exchange rate (BTC/USD).

##Sample

Quick sample of what we have so far, gives you a glimpse of what to expect if you want to digg in:

[Bitcoin-Price-News-Impact_v0.1.2.ipynb](http://nbviewer.ipython.org/github/Link-/bitcoin-manalysis/blob/master/data_analysis/Bitcoin-Price-News-Impact_v0.1.2.ipynb)

##Prerequisites

* python 2.7
* ipython (Jupyter) 3.0.0
* [requests](http://docs.python-requests.org/en/latest/)
* [matplotlib](http://matplotlib.org)
* wget (for OSX use homebrew)

##Data
####Bitcoin Data
Download all the bitcoin price historical data. This can be found in [http://api.bitcoincharts.com/v1/csv/](http://api.bitcoincharts.com/v1/csv/)

In order to get all the available data for all available markets, execute the following:

	$ cd <data directory>
    $ wget -A csv.gz -r -l 1 -nd http://api.bitcoincharts.com/v1/csv/
    
From this entire bitcoincharts repo, the most comprehensive catalog of data is `btceUSD.csv`.

For the Bitcoin Transactions Volume (in BTC or USD) you can get this data from Quandl through their API

* [http://www.quandl.com/api/v1/datasets/BCHAIN/ETRAV.csv (BTC)](http://www.quandl.com/api/v1/datasets/BCHAIN/ETRAV.csv)
* [http://www.quandl.com/api/v1/datasets/BCHAIN/ETRVU.csv (USD)](http://www.quandl.com/api/v1/datasets/BCHAIN/ETRVU.csv)

###Raw Data

If you want access to the exact raw data sets I'm using, I have uploaded them to Google Drive

[Raw Data - Google Drive](https://drive.google.com/folderview?id=0B5eZRVoBwyOafkxHVjd5NlpNX2R2V0xMS1AzcG9rQjdDdm5KdzQyUGFWQUx4cG9Cb2d6MEk&usp=sharing)

####News Articles
The best centralized source of filtered/relevant news is undoutably Reddit, specifically `/r/bitcoin`. Yes, the posts of this subreddit can be of numerous types (news articles, videos, blog posts etc...) but we will deal with this issue during the data cleanup process.

Another relevant source is the NewYork Times articles. They have a nice API which can be used to aggregate bitcoin related articles.

In order to gather this data, a scrapper per source was developed and can be found in the directory `scrappers/<source>`

##Interesting Links

[matplotlib - 2D and 3D plotting in Python](http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb)