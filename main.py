import re
import requests
from datetime import datetime, timedelta

API_KEY = "DL79PMWQG2T141QY"

def identify_ticker(query):
    query = query.lower()
    companies = {
        "tesla": "TSLA",
        "palantir": "PLTR",
        "nvidia": "NVDA",
    }
    for name, ticker in companies.items():
        if name in query:
            return ticker
    return "AAPL"

def get_ticker_news(ticker):
    url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={API_KEY}"
    res = requests.get(url)
    data = res.json()
    articles = data.get("feed", [])[:3]
    return "\n".join([f"- {a['title']}: {a['summary']}" for a in articles]) if articles else "No news found."

def get_ticker_price(ticker):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={API_KEY}"
    res = requests.get(url)
    data = res.json().get("Global Quote", {})
    price = data.get("05. price", "N/A")
    return f"Current price of {ticker} is ${price}"

def get_ticker_price_change(ticker, days=7):
    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=days)
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={API_KEY}"
    res = requests.get(url)
    data = res.json().get("Time Series (Daily)", {})
    try:
        sorted_dates = sorted(data.keys(), reverse=True)
        price_now = float(data[sorted_dates[0]]['4. close'])
        price_then = float(data[sorted_dates[days]]['4. close'])
        delta = round(price_now - price_then, 2)
        return f"Price changed by ${delta} in last {days} days"
    except:
        return "Price change data unavailable."

def analyze_stock(query):
    ticker = identify_ticker(query)
    price_info = get_ticker_price(ticker)
    change_info = get_ticker_price_change(ticker)
    news_info = get_ticker_news(ticker)
    return f"Stock: {ticker}\n{price_info}\n{change_info}\n\nRecent News:\n{news_info}"

if __name__ == "__main__":
    queries = [
        "Why did Tesla stock drop today?",
        "What’s happening with Palantir stock recently?",
        "How has Nvidia stock changed in the last 7 days?"
    ]
    for q in queries:
        print(f"\n--- Query: {q} ---")
        print(analyze_stock(q))
