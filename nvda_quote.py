import yfinance as yf
from datetime import datetime

def get_nvda_quote() -> dict:
    ticker = yf.Ticker("NVDA")
    info = ticker.fast_info  # 速度較快的基本資料
    data = {
        "symbol": "NVDA",
        "price": float(info.last_price),
        "currency": info.currency,
        "exchange": info.exchange,
        "time_fetched": datetime.now().isoformat(timespec="seconds"),
    }
    return data

def main():
    quote = get_nvda_quote()
    print("=== NVDA Quote ===")
    print(f"Symbol     : {quote['symbol']}")
    print(f"Price      : {quote['price']} {quote['currency']}")
    print(f"Exchange   : {quote['exchange']}")
    print(f"Fetched at : {quote['time_fetched']}")


if __name__ == "__main__":
    main()

