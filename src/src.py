from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
crypto = cg.get_coins_markets(vs_currency='usd')
print(crypto)
