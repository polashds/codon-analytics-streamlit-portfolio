# codon-analytics-streamlit-portfolio
A collection of production-ready deployment templates built for deploying microgig projects


# codon-analytics-streamlit-portfolio

This document contains starter code for the folder structure you provided. Paste each file into the matching path in your repository.

---

## `README.md`

````md
# Codon Analytics — Streamlit Portfolio

This repository is a Streamlit portfolio showcasing data-science projects. Each project lives under `projects/` and can be launched individually. The main portfolio dashboard is `portfolio_showcase_streamlit/app.py`.

## Quick start

1. Create a virtual environment and install dependencies:

```bash
python -m venv codondev
source codondev/Scrips/activate   # or .venv\Scripts\activate on Windows

pip install -r requirements.txt
````

2. Run the portfolio dashboard:

```bash
streamlit run codon-ananlytics-streamlit-portfolio/app.py
```

3. To run an individual project (example):

```bash
streamlit run projects/project01_stock_dashboard/app.py
```

````

---

## `requirements.txt`

```text
streamlit>=1.20
pandas>=1.5
plotly>=5.0
yfinance>=0.2.18
numpy>=1.24
scikit-learn>=1.1
matplotlib>=3.6
pillow>=9.0
altair>=4.2
````

---

## `portfolio_overview.md`

```md
# Portfolio overview

This portfolio contains a collection of small data apps built with Streamlit to demonstrate skills in EDA, visualization, basic ML, and app deployment.

## Highlights
- Stock dashboard (real-time fetch via yfinance)
- Weather dashboard (sample data)
- Ecommerce forecasting (example model pipeline)

Each project folder has a README explaining data, how to run, and expected outputs.
```

---

## `projects/project01_stock_dashboard/README.md`

```md
# Project 01 — Stock Dashboard

Simple Streamlit app that fetches stock prices with `yfinance`, shows interactive charts and basic indicators.

Files:
- `app.py` — Streamlit app
- `data_utils.py` — data fetching + caching
- `visualizations.py` — reusable plotting helpers
- `sample.csv` — example saved data
```

---

## `projects/project01_stock_dashboard/sample.csv`

```csv
Date,Open,High,Low,Close,Volume
2023-01-03,130,135,128,134,1200000
2023-01-04,134,137,133,136,900000
```

---

## `projects/project01_stock_dashboard/data_utils.py`

```python
import pandas as pd
import yfinance as yf
import streamlit as st

@st.cache_data
def fetch_ticker(ticker: str, period: str = "6mo") -> pd.DataFrame:
    """Fetch OHLCV data for a ticker using yfinance."""
    df = yf.download(ticker, period=period, progress=False)
    if df.empty:
        return pd.DataFrame()
    df = df.reset_index()
    df.columns = [c if isinstance(c, str) else str(c) for c in df.columns]
    return df

def load_sample(path: str) -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=["Date"])
```

---

## `projects/project01_stock_dashboard/visualizations.py`

```python
import plotly.graph_objects as go


def plot_candlestick(df, title: str = "Price"):
    fig = go.Figure(data=[go.Candlestick(
        x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close']
    )])
    fig.update_layout(title=title, xaxis_rangeslider_visible=False)
    return fig


def plot_close_line(df, title: str = "Close Price"):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name='Close'))
    fig.update_layout(title=title)
    return fig
```

---

## `projects/project01_stock_dashboard/app.py`

```python
import streamlit as st
from data_utils import fetch_ticker, load_sample
from visualizations import plot_candlestick, plot_close_line
import pandas as pd

st.set_page_config(page_title="Stock Dashboard - Project01", layout="wide")

st.title("Project 01 — Stock Dashboard")

col1, col2 = st.columns([1,3])
with col1:
    ticker = st.text_input("Ticker", value="AAPL")
    period = st.selectbox("Period", ["1mo","3mo","6mo","1y","2y"], index=2)
    use_sample = st.checkbox("Use sample data instead", value=False)

with col2:
    if use_sample:
        df = load_sample("sample.csv")
    else:
        df = fetch_ticker(ticker, period=period)

    if df.empty:
        st.warning("No data found for ticker. Try sample data or another symbol.")
    else:
        st.plotly_chart(plot_candlestick(df, title=f"{ticker} Candlestick"), use_container_width=True)
        st.plotly_chart(plot_close_line(df, title=f"{ticker} Close Price"), use_container_width=True)

st.markdown("---")
st.write("Data preview")
if not df.empty:
    st.dataframe(df.tail())
```

---

## `projects/project50_ecommerce_forecasting/README.md`

```md
# Project 50 — Ecommerce Forecasting

A small demonstration of building a forecasting pipeline for product sales. Includes a toy model and simple dashboard.
```

---

## `projects/project50_ecommerce_forecasting/model_utils.py`

```python
import pandas as pd
from sklearn.linear_model import LinearRegression


def train_simple_trend(df: pd.DataFrame, date_col='date', target='sales'):
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df['t'] = (df[date_col] - df[date_col].min()).dt.days
    X = df[['t']]
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    return model


def predict_trend(model, df_dates):
    import pandas as pd
    df = pd.DataFrame({ 'date': pd.to_datetime(df_dates) })
    df['t'] = (df['date'] - df['date'].min()).dt.days
    preds = model.predict(df[['t']])
    df['forecast'] = preds
    return df
```

---

## `projects/project50_ecommerce_forecasting/visualizations.py`

```python
import matplotlib.pyplot as plt


def plot_forecast(df, date_col='date', actual='sales', forecast='forecast'):
    fig, ax = plt.subplots(figsize=(8,3))
    ax.plot(df[date_col], df[actual], label='Actual')
    ax.plot(df[date_col], df[forecast], label='Forecast')
    ax.legend()
    ax.set_xlabel('Date')
    return fig
```

---

## `projects/project50_ecommerce_forecasting/app.py`

```python
import streamlit as st
import pandas as pd
from model_utils import train_simple_trend, predict_trend
from visualizations import plot_forecast

st.set_page_config(page_title="Ecommerce Forecasting - Project50")
st.title("Project 50 — Ecommerce Forecasting")

st.markdown("Upload a CSV with columns: date,sales")
uploaded = st.file_uploader("Choose CSV", type=['csv'])

if uploaded is not None:
    df = pd.read_csv(uploaded, parse_dates=['date'])
    st.write(df.head())
    model = train_simple_trend(df, date_col='date', target='sales')
    future_dates = pd.date_range(df['date'].max(), periods=30, freq='D')
    pred_df = predict_trend(model, future_dates)
    merged = pd.concat([df.rename(columns={'date':'date'}) , pred_df.rename(columns={'date':'date','forecast':'forecast'})], ignore_index=True, sort=False)
    st.pyplot(plot_forecast(merged, date_col='date', actual='sales', forecast='forecast'))
else:
    st.info("Upload a sample dataset to try the forecasting demo.")
```

---

## `portfolio_showcase_streamlit/projects_config.json`

```json
{
  "projects": [
    {
      "id": "project01_stock_dashboard",
      "title": "Stock Dashboard",
      "description": "Interactive stock charts using yfinance and Plotly.",
      "path": "../projects/project01_stock_dashboard/app.py",
      "tags": ["streamlit","finance","visualization"]
    },
    {
      "id": "project50_ecommerce_forecasting",
      "title": "Ecommerce Forecasting",
      "description": "Toy forecasting pipeline and dashboard.",
      "path": "../projects/project50_ecommerce_forecasting/app.py",
      "tags": ["streamlit","forecasting","ml"]
    }
  ]
}
```

---

## `portfolio_showcase_streamlit/app.py`

```python
import streamlit as st
import json
import subprocess
import os
from pathlib import Path

st.set_page_config(page_title="Codon Analytics — Portfolio", layout="wide")

BASE = Path(__file__).parent
CONFIG_PATH = BASE / "projects_config.json"

st.title("Codon Analytics — Project Showcase")

with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

projects = config.get('projects', [])

for proj in projects:
    st.subheader(proj['title'])
    st.write(proj['description'])
    cols = st.columns([3,1])
    with cols[0]:
        st.write("Tags: " + ", ".join(proj.get('tags', [])))
    with cols[1]:
        if st.button(f"Open {proj['title']}", key=proj['id']):
            # Launch project in separate streamlit process on a different port
            # Note: this is a simple helper for local dev. For deployment, host each app and embed URLs.
            app_path = (BASE / proj['path']).resolve()
            port = 8501
            # find a free port by incrementing (naive)
            while True:
                import socket
                s = socket.socket()
                try:
                    s.bind(("127.0.0.1", port))
                    s.close()
                    break
                except OSError:
                    port += 1
            cmd = ["streamlit", "run", str(app_path), "--server.port", str(port), "--server.headless", "true"]
            st.info(f"Starting {proj['title']} on http://127.0.0.1:{port}")
            # Launch as background process
            subprocess.Popen(cmd)

st.markdown("---")
st.info("Tip: run individual apps directly with `streamlit run projects/<project>/app.py` for faster startup during development.")
```

---

### Notes

* These are starter templates — tweak UI, styling, and plotting to match your needs.
* For production or hosted portfolios, consider deploying each project as its own service and embedding via iframe or using Streamlit Community Cloud.

---

If you'd like, I can also generate `gitignore`, CI (GitHub Actions) workflow, or Dockerfiles for running the portfolio. Let me know which files you want next.
