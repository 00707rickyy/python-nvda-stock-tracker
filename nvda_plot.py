import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd

def load_data(filename: str = "nvda_log.csv") -> pd.DataFrame:
    # 如果冇 'time' 就用手動欄名
    df = pd.read_csv(filename)

    if "time" not in df.columns:
        # 沒有 header 的情況：重新讀，指定欄名
        df = pd.read_csv(filename, header=None, names=["time", "price"])

    df["time"] = pd.to_datetime(df["time"])
    df = df.sort_values("time").reset_index(drop=True)
    return df


def plot_price(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 5))
    plt.plot(df["time"], df["price"], label="NVDA price")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.title("NVDA price over time (logged from yfinance)")
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.show()

def main():
    df = load_data("nvda_log.csv")
    print(df.head()) 
    plot_price(df)
    
def plot_price(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 5))
    plt.plot(df["time"], df["price"], label="NVDA price")
    df["ma_5"] = df["price"].rolling(window=5).mean()
    plt.plot(df["time"], df["ma_5"], linestyle="--", label="5-point moving average")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.title("NVDA price over time (with 5-point moving average)")
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()


