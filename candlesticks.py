from secrets import choice

from pip import main
from snapshot import *
from squeeze import *

def candlemenu():
    # Main Menu for CandleStick Patterns.
    print("\t\t\t\tSelect Dataset -->")
    print("\t\t\t\t\t             (1) Sensex30")
    print("\t\t\t\t\t             (2) Low Cap Stonks")
    
    user_in = int(input("Enter Your Choice : "))
    print('\n')
    
    if(user_in == 1):
        dataset = 'Datasets'
        print("\n\t\t\t<< Sensex CandleStick Patterns  >>")
    elif(user_in == 2):
        dataset = 'Datasets_LowCap'
        print("\n\t\t\t<< LowCap CandleStick Patterns >>")
    else:
        print("\t\t\t\t\t Invalid Choice")
        
    print("\t\t\t\tSelect Patttern -->")
    print("\t\t\t\t\t             (1) Bullish Engulfing")
    print("\t\t\t\t\t             (2) Morning Star")
    
    choice = int(input("Enter Your Choice : "))
    print('\n')
    
    if(user_in == 1):
        bullEngulf(dataset)
    elif(user_in == 2):
        morningStar(dataset)
    else:
        print("\t\t\t\t\t Invalid Choice")
        
    
           
def bullEngulf(dataset):
# the price opens lower than the previous low, 
# yet buying pressure pushes the price up to a higher level than the previous high, 
# culminating in an obvious win for the buyers.        
    for filename in os.listdir(f"{dataset}"):
        #print(filename)
        symbol = filename.split(".")[0]
        # print(symbol)
        df = pandas.read_csv(f'{dataset}/{filename}')
        if df.empty:
            continue
   
        prev_close = df.iloc[-2]['Close']
        prev_open = df.iloc[-2]['Open']
        new_close = df.iloc[-1]['Close']
        new_open = df.iloc[-1]['Open']
        
        if prev_close < prev_open:
            if prev_close > new_open and new_close > prev_open :
                print("___________________________________________________________________________\n")
                print(f"            {symbol} is in indicating Bullish Engulfing   \n")   
                print("Summary (Last 5 Trading Days): \n")
                print(df[['Date','Open','Close','Volume']].tail(5))
                print("___________________________________________________________________________")
                print("---------------------------------------------------------------------------")
            
 
def morningStar(dataset):
# Day 1: On first day, a large bearish candlestick is formed, representing further continuation of a downtrend.
# Day 2: On second day, a small candlestick either bullish or bearish, is formed which gaps down from the first candlestick formed on Day 1.
# Day 3: On third day a large bullish candlestick is formed which gaps up from the candlestick formed on Day2.
#        It opens above the close of the Day 2 candlestick and closes atleast near the center or midpoint of the candlestick formed on Day 1.
    
    
    for filename in os.listdir(f"{dataset}"):
        #print(filename)
        symbol = filename.split(".")[0]
        # print(symbol)
        df = pandas.read_csv(f'{dataset}/{filename}')
        if df.empty:
            continue
        
        fir_close = df.iloc[-3]['Close']
        fir_open = df.iloc[-3]['Open']
        sec_close = df.iloc[-2]['Close']
        sec_open = df.iloc[-2]['Open']
        new_close = df.iloc[-1]['Close']
        new_open = df.iloc[-1]['Open']
        
        if fir_open > fir_close:
            if sec_open < fir_close and sec_close < fir_close and fir_open < fir_close:
                if new_open > sec_open and new_close > new_open :
                    print("___________________________________________________________________________\n")
                    print(f"            {symbol} is in indicating Morning Star pattern   \n")   
                    print("Summary (Last 5 Trading Days): \n")
                    print(df[['Date','Open','Close','Volume']].tail(5))
                    print("___________________________________________________________________________")
                    print("---------------------------------------------------------------------------")
    else:
        print("___________________________________________________________________________\n")
        print("                  No Stock Indicating Morning Star\n")
        print("---------------------------------------------------------------------------")
                       
