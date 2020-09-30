Hackerrank-Missingdata
=============

### Missing Stock Prices


A time series of a stock's highest price during a trading day (at the New York Stock Exchange), is provided to you. In each test case, the day's highest prices is missing for certain days. By analyzing the data, try to identify the missing price for those particular days.

### Input Format
The first line contains an integer N, which is the number of rows of data to follow.
This is followed by N rows of data, each of which contains a time-stamp in the first column and the day's highest price for the stock in the second column. There is a tab delimiter between the two columns of data.
There are exactly twenty rows in each input file, where the day's highest price is missing. The missing prices are marked as "Missing_1", "Missing_2" .."Missing_20". These missing records have been randomly dispersed in the rows of data.

### Output Format
The output should contain exactly twenty rows, each containg your predicted value, for each of the missing values (Missing_1, Missing_2 ... Missing_20) in that order.


### Scoring

We will compute the mean of the magnitude of the percentage difference by comparing your expected answers with the actual stock price high, for each of the missing records (in all test cases - samples included).

d = Summation of abs((expected price - computed price)/expected price) x 100 (for all missing records, in all test cases).

Your final score on a scale of 100 will be: 50 x max(2 - d, 0)

i.e, if the mean value of 'd' exceed 2% (your predictions are off by 2% or more on an average) you will score a zero. If your predictions are all right on target, you will score 100.

When you hit "Compile and Test" (instead of submit) we will run your solution against the three sample test cases only. And the visible score at that time, will be normalized out of 1, rather than 100.

In case your program throws an error (or an incorrect output format) for a single test case, the overall score assigned will be zero.
