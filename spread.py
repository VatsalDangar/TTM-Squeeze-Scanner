from bsedata.bse import BSE 
import os
import pandas as pd
b = BSE()


Bse_Dict = {
    500820:"ASIANPAINT.NS", 532215:"AXISBANK.NS", 532977:"BAJAJ-AUTO.NS", 500034:"BAJFINANCE.NS", 532978:"BAJAJFINSV.NS", 532454:"BHARTIARTL.NS", 500124:"DRREDDY.NS",
    532281:"HCLTECH.NS", 500010:"HDFC.NS", 500180:"HDFCBANK.NS", 500696:"HINDUNILVR.NS", 532174:"ICICIBANK.NS", 532187:"INDUSINDBK.NS", 500209:"IFNY.NS", 500875:"ITC.NS",
    500247:"KOTAKBANK.NS", 500510:"LT.NS", 500520:"M&M.NS", 532500:"MARUTI.NS", 500790:"NESTLEIND.NS", 532555:"NTPC.NS", 500312:"ONGC.NS", 532898:"POWERGRID.NS",
    500325:"RELIANCE.NS", 500112:"SBIN.NS", 524715:"SUNPHARMA.NS", 532540:"TCS.NS", 532755:"TECHM.NS", 500114:"TITAN.NS", 532538:"ULTRACEMCO.NS"
    }



Scrips = Bse_Dict.keys()
Symbols = Bse_Dict.values()


print(b.getQuote("500325")['currentValue'])

