#Stock price One day, a friend of mine told me that the key to #financial freedom is investing in stocks. While it is greatly true #during the market boom, it still remains an attractive options #today to trade stocks part time. Given the easy access to online #trading platform, there are many self made value investors or #housewife traders.

#There are even success stories and advertisements which boast “Get #Rich Quick Scheme”
#to learn how to invest in stocks with a staggering return of 40% #and even more. Investing has become the boon for the working #professionals today.

import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2017, 1, 11)

df = web.DataReader("MSFT", 'yahoo', start, end)
df.tail()

%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style

# Adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')

close_px.plot(label='MSFT')
mavg.plot(label='mavg')
plt.legend()