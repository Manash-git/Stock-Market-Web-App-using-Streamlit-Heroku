# importing necessary library

import yfinance as yf
import streamlit as st

# list of Ticker for various company
# https://www.nasdaq.com/market-activity/stocks/screener
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75


st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Google!
""")

# define the ticker for google 

ticker_gl = 'GOOGL'

# fetch the data

ticker_gl_data = yf.Ticker(ticker_gl)

#get the historical prices for this ticker
tickerDf = ticker_gl_data.history(period='1d', start='2010-5-31', end='2020-5-31')


st.write("""
## Closing Price

""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price

""")
st.line_chart(tickerDf.Volume)


st.write("""
     
         
#### © Manash Mondal
#### Github: https://github.com/Manash-git 
""")


# streamlit run app.py