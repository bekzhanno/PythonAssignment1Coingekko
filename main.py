from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
crypto = cg.get_coins_markets(vs_currency='usd')
print(crypto)

N = int(input("Enter for filtering top N cryptocurrencies by market capitalization:  "))
i = 0
for i in range(N):
    i = i + 1
    print(i,".", crypto[i]['name'], "$",crypto[i]['market_cap'], '***price:', "$",crypto[i]['current_price'])
