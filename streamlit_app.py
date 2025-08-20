import streamlit as st
import pandas as pd
import numpy as np

# Sample data
data = {
    "date": pd.date_range(start="2025-07-01", periods=30),
    "valid_isin_pct": np.random.uniform(95, 100, 30),
    "dup_records": np.random.randint(0, 50, 30),
    "sla_met": np.random.uniform(90, 100, 30)
}
df = pd.DataFrame(data)

# Dashboard
st.title("Data Stewardship Performance Dashboard")

st.line_chart(df.set_index("date")[["valid_isin_pct", "sla_met"]])
st.bar_chart(df.set_index("date")[["dup_records"]])

st.metric(label="Current ISIN Validity %", value=f"{df.valid_isin_pct.iloc[-1]:.2f}%")
st.metric(label="Current SLA Compliance %", value=f"{df.sla_met.iloc[-1]:.2f}%")
st.metric(label="Duplicates (Today)", value=df.dup_records.iloc[-1])
