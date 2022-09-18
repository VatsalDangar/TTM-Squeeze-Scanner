import os
import yfinance as yf
from datetime import *

def readUpdateTimes(group):
    with open(f"TimeLog_{group}.txt") as f:
        up_time = f.read()
    
    return up_time    
        
def UpdateTime(CurrentTime, group):
    format_data = "%d/%m/%y %H:%M:%S %p"
    
    with open(f"Timelog_{group}.txt","w") as f:
        current = datetime.strftime(CurrentTime, format_data)
        f.write(current)

Last_Sensex_Update = datetime.strptime(readUpdateTimes("Sensex"), "%d/%m/%y %H:%M:%S %p")
Last_Lowcap_Update = datetime.strptime(readUpdateTimes("LowCap"), "%d/%m/%y %H:%M:%S %p")
# Last_Sensex_Update = datetime(2022, 1, 19, 18, 29, 27, 605231)
# Last_Lowcap_Update = datetime(2022, 1, 19, 18, 29, 27, 605231)
format_data = "%d/%m/%y %H:%M:%S %p"

## SENSEX - 30
def snapSensex30():
    global Last_Sensex_Update 
    global format_data
    CurrentTime = datetime.now()   # datetime(year, month, day, hour, minute, second)
    
    TimeDiff = ((CurrentTime - Last_Sensex_Update).total_seconds())/3600 # Time Difference in hours.
    
    print(f"<<<<< Dateset Last Updated {datetime.strftime(Last_Sensex_Update, format_data)} >>>>>\n")
    
    if (TimeDiff > 2):
        print("<<<<<<<<<<<<  Updating Datasets  >>>>>>>>>>>> \n") 
        with open('Tickers.csv') as f:
            lines = f.read().splitlines()
            for symbol in lines:
                print(symbol)
                data = yf.download(symbol, period = "6mo")
                data.to_csv("datasets/{}.csv".format(symbol))
                UpdateTime(CurrentTime, "Sensex")


## To Add Tickers into datasets.
def addTickers():
    
    print("<--- SELECT A DATASET --->\n")
    print("Add Tickers to --> (1) Sensex ")
    print("                   (2) Low Cap ")
    print("____________________________________\n")
    
    addChoice = int(input("Enter Choice : "))
    print("____________________________________\n")
    
    if (addChoice == 1):      # For Sensex
        add = str(input("Enter The Ticker --> "))  + ".NS"      
        NewTick = yf.download(add, period = "6mo")
        NewTick.to_csv(f"datasets/{add}.csv")
        with open("Tickers.csv","a") as f:
            f.write(f"{add}")
            
    elif (addChoice == 2):                                    # For LowCap
        add = str(input("Enter The Ticker --> ")) + ".NS"     
        NewTick = yf.download(add, period = "6mo")
        NewTick.to_csv(f"datasets/{add}.csv")
        with open("SmallCap.csv","a") as f:
            f.write(f"{add}")

## Low Cap Tickers.
def SnapLowCap():
    
    
    global Last_Lowcap_Update 
    CurrentTime = datetime.now()   # datetime(year, month, day, hour, minute, second)
    global format_data
    
    TimeDiff = ((CurrentTime - Last_Lowcap_Update).total_seconds())/3600 # Time Difference in hours.
    
    print(f"<<<<< Dateset Last Updated {datetime.strftime(Last_Lowcap_Update, format_data)} >>>>>\n")
    
    
    if (TimeDiff > 2):
        print("<<<<<<<<<<<<  Updating Datasets  >>>>>>>>>>>> \n") 
        with open('SmallCap.csv') as f:
            lines = f.read().splitlines()
            for symbol in lines:
                print(symbol)
                data = yf.download(symbol, period = "6mo")
                data.to_csv("datasets_LowCap/{}.csv".format(symbol))
                UpdateTime(CurrentTime, "LowCap")


def ForceUpdate():
    
    CurrentTime = datetime.now()
        
    print("<<<<<<<<<<<<  Updating SenSex Datasets  >>>>>>>>>>>> \n") 
    with open('Tickers.csv') as f:
        lines = f.read().splitlines()
        for symbol in lines:
            print(symbol)
            data = yf.download(symbol, period = "6mo")
            data.to_csv("datasets/{}.csv".format(symbol))
            UpdateTime(CurrentTime, "Sensex")
    
    print("\n________________________________________________________________________\n")
    
    print("<<<<<<<<<<<<  Updating LowCap DataSet  >>>>>>>>>>>> \n") 
    with open('SmallCap.csv') as f:
        lines = f.read().splitlines()
        for symbol in lines:
            print(symbol)
            data = yf.download(symbol, period = "6mo")
            data.to_csv("datasets_LowCap/{}.csv".format(symbol))
            UpdateTime(CurrentTime, "LowCap")
            
    print("\n       <<<<    SUCCESSFULLY UPDATED    >>>>            ")        
    
    
