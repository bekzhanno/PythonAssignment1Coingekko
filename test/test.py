from src import *

N = int(input("Enter for filtering top N cryptocurrencies by market capitalization:  "))
i = -1
for i in range(N):
    print(i+1,".", crypto[i]['name'], "$",crypto[i]['market_cap'], '***price:', "$",crypto[i]['current_price'])
    i = i + 1