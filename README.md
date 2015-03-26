    @version: 0.1.2
    @description: This notebook will read Bitcoin price values and transaction volumes
    from CSV files and display a figure showing the relationship between the two.

This analysis **(a work in progress)** is an attempt to find a corollation between bitcoin related news and the rise or fall of the bitcoin exchange rate (BTC/USD).

Note: http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb

###DATA
####Get the Bitcoin (Sample) Data
Download all the bitcoin price historical data. This can be found in http://api.bitcoincharts.com/v1/csv/
In order to get all the available data from all markets, execute the following:

    wget -A csv.gz -r -l 1 -nd http://api.bitcoincharts.com/v1/csv/
    
From this entire bitcoincharts repo, the most comprehensive catalog of data is `btceUSD.csv`.

For the purposes of this excercise, i'm using a small data sample `b7USD.csv`.

For the Bitcoin Transactions Volume (in BTC or USD) you can get this data from Quandl through their API

    http://www.quandl.com/api/v1/datasets/BCHAIN/ETRAV.csv (BTC)
    http://www.quandl.com/api/v1/datasets/BCHAIN/ETRVU.csv (USD)

####Unzip the package

    $: gunzip btceUSD.csv.gz

