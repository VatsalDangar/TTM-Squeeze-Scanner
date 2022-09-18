import os, pandas
import plotly.graph_objects as go

# dataframes = {}

def Date_Index(date_list):
    revList = date_list[::-1]
    
    for i in range(0,(len(revList) - 1)):
        if revList[i] == (revList[i+1] + 1):
            continue
        else:
            Date_Since_index = revList[i]
            break
    
    return Date_Since_index
            
            
def CalculateChange(date_list, df):
    revList = date_list[::-1]

    price_insqueeze = df['Close'][revList[0]]
    price_latest = df['Close'][df.index[-1]]
    
    perc_Change = round(((price_latest - price_insqueeze)/(price_insqueeze))*100, 2)
    
    return str(perc_Change) + " %"

    


# Getting All the tickers of interest saved from datasets.
def ComputeTTM(dataset):
    for filename in os.listdir(f"{dataset}"):
        #print(filename)
        symbol = filename.split(".")[0]
        # print(symbol)
        df = pandas.read_csv(f'{dataset}/{filename}')
        if df.empty:
            continue


        # Calculations of Bollinger Bands 
        df['20sma'] = df['Close'].rolling(window=20).mean() # Middle Bollinger Band = 20 simple moving average
        df['stddev'] = df['Close'].rolling(window=20).std() # Standard Standard Deviation
        df['lower_band'] = df['20sma'] - (2 * df['stddev']) # Lower Bollinger Band = MBB - 2 * Standard Deviation
        df['upper_band'] = df['20sma'] + (2 * df['stddev']) # Upper Bollinger Band = MBB + 2 * Standard Deviation

        # Calculating ATR(Average True Range)
        df['TR'] = abs(df['High'] - df['Low'])
        df['ATR'] = df['TR'].rolling(window=20).mean()

        # Calculating Keltner Channels
        df['lower_keltner'] = df['20sma'] - (df['ATR'] * 1.5) # Lower Keltner Channel = 20 SMA - (ATR * Keltner Multiplier(1.5 here))
        df['upper_keltner'] = df['20sma'] + (df['ATR'] * 1.5) # Upper Keltner Channel = 20 SMA + (ATR * Keltner Multiplier(1.5 here))


        # Function Scannning if the Ticker is in a squeeze or not.
        def in_squeeze(df):
            return df['lower_band'] > df['lower_keltner'] and df['upper_band'] < df['upper_keltner']


        df['squeeze_on'] = df.apply(in_squeeze, axis=1) 

        if df.iloc[-5]['squeeze_on'] and not df.iloc[-1]['squeeze_on']: # For Tickers coming out of a squeeze.
            
            Date_list = df.index[df['squeeze_on']].tolist()
            
            print(f"        {symbol} is coming out the squeeze      \n")
            print(f"        Percentage Change since squeeze --> {CalculateChange(Date_list, df)}\n")
            print(df[['Date','Open','Close','Volume','squeeze_on']].tail())
            print("---------------------------------------------------------------------------")
            
        
        if df.iloc[-1]['squeeze_on']:                   # For Tickers Currently in Squeeze
            
            
            # print(df['Date'].where(df.iloc[-1]['squeeze_on']) == True)
            Date_list = df.index[df['squeeze_on']].tolist()
            # print(Date_list)
            Date_Since = df['Date'][Date_Index(Date_list)]
            # print(Date_Since)
            print("___________________________________________________________________________\n")
            print(f"            {symbol} is in a squeeze since {Date_Since}   \n")  
            print(f"            Duration of Squeeze --> {(Date_list[-1]) - (Date_Index(Date_list)) + 1} Days  \n")  
            print("Summary (Last 5 Trading Days): \n")
            print(df[['Date','Open','Close','Volume','squeeze_on']].tail(5))
            print("___________________________________________________________________________")
            print("---------------------------------------------------------------------------")
        
        

    # save all dataframes to a dictionary
    # we can chart individual names below by calling the chart() function
    # dataframes[symbol] = df


# def chart(df):
#     candlestick = go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])
#     upper_band = go.Scatter(x=df['Date'], y=df['upper_band'], name='Upper Bollinger Band', line={'color': 'red'})
#     lower_band = go.Scatter(x=df['Date'], y=df['lower_band'], name='Lower Bollinger Band', line={'color': 'red'})

#     upper_keltner = go.Scatter(x=df['Date'], y=df['upper_keltner'], name='Upper Keltner Channel', line={'color': 'blue'})
#     lower_keltner = go.Scatter(x=df['Date'], y=df['lower_keltner'], name='Lower Keltner Channel', line={'color': 'blue'})

#     fig = go.Figure(data=[candlestick, upper_band, lower_band, upper_keltner, lower_keltner])
#     fig.layout.xaxis.type = 'category'
#     fig.layout.xaxis.rangeslider.visible = False
#     fig.show()

# df = dataframes['SUZLON.NS']
# chart(df)