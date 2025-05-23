# 🎬 Demo Script – Multi-Agent Stock Bot

## 🗣️ Narration
"Hi! This is a demo of my multi-agent stock analysis system built using Google ADK and Alpha Vantage."
"It answers real-world stock queries using five modular agents that work together."

## 🧠 Architecture Walkthrough
- identify_ticker: Detects the stock based on query (e.g., Tesla → TSLA)
- ticker_news: Fetches recent headlines and summaries
- ticker_price: Gets live stock price
- ticker_price_change: Computes price difference in the last 7 days
- ticker_analysis: The brain—it calls all agents and combines the result

```
Run queries like:
- Why did Tesla stock drop today?
- What’s happening with Palantir stock recently?
- How has Nvidia stock changed in the last 7 days?

## 🧾 Wrap-Up
"This system is modular, real-time, and handles natural language queries using Alpha Vantage."
