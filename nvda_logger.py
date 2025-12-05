import yfinance as yf
from datetime import datetime
import csv
import time

def get_nvda_price() -> float:
    ticker = yf.Ticker("NVDA")
    info = ticker.fast_info
    return float(info.last_price)

def append_to_csv(filename: str, price: float) -> None:
    now = datetime.now().isoformat(timespec="seconds")
    row = {"time": now, "price": price}

    write_header = False
    try:
        with open(filename, "r", encoding="utf-8"):
            pass
    except FileNotFoundError:
        write_header = True

    with open(filename, "a", encoding="utf-8", newline="") as f:
        fieldnames = ["time", "price"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(row)
    print(f"[{now}] Logged price: {price}")

def main():
    filename = "nvda_log.csv"
    print("Start logging NVDA price. Press Ctrl+C to stop.")
    try:
        while True:
            price = get_nvda_price()
            append_to_csv(filename, price)
            time.sleep(60)  # 每 60 秒抓一次
    except KeyboardInterrupt:
        
        print("Stopped logging.")

if __name__ == "__main__":
    main()