# 🧠 Multi-Agent Stock Analysis System

This project implements a modular multi-agent system using Google ADK principles to analyze stock-related queries using real-time data from the Alpha Vantage API.

## 📌 Objective
Answer user queries like:
- "Why did Tesla stock drop today?"
- "What’s happening with Palantir stock recently?"
- "How has Nvidia stock changed in the last 7 days?"

## 🛠 Agents Implemented
- **identify_ticker** – Extracts ticker from user query
- **ticker_news** – Fetches recent news using Alpha Vantage `NEWS_SENTIMENT`
- **ticker_price** – Fetches live stock price via `GLOBAL_QUOTE`
- **ticker_price_change** – Calculates price delta from daily data
- **ticker_analysis** – Coordinates all agents and returns structured summary

## ⚙️ How to Run
```bash
pip install requests
python main.py
```

## 🧪 Sample Queries
```
Why did Tesla stock drop today?
What’s happening with Palantir stock recently?
How has Nvidia stock changed in the last 7 days?
```

## 🧾 Example Output
```
Stock: TSLA
Current price of TSLA is $174.75
Price changed by $-4.20 in last 7 days

Recent News:
- Tesla cuts prices in key markets: Tesla reduced EV prices across Europe.
- Investor confidence shaken: Analysts cite market slowdown.
```

## 🔗 API Used
- [Alpha Vantage API](https://www.alphavantage.co/)

## 📁 Repo Structure
```
stock-analysis-bot/
├── main.py
├── README.md
├── agents.yaml
├── orchestration.yaml

