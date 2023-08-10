from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

def get_price(coin_ids: str, vs_currencies: str):
   price = cg.get_price(ids=coin_ids, vs_currencies=vs_currencies)
   print(price)
   return price

if __name__ == "__main__":
   get_price("bitcoin", "usd")