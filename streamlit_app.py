import streamlit as st
import pandas as pd
import numpy as np

# Sample data
np.random.seed(42)
dates = pd.date_range(start="2025-07-01", periods=30)

df = pd.DataFrame({
    "date": dates,
    "valid_isin_pct": np.random.uniform(95, 100, len(dates)),
    "sla_met": np.random.uniform(90, 100, len(dates)),
    "dup_records": np.random.randint(10, 80, len(dates)),
    "null_errors": np.random.randint(5, 20, len(dates)),
    "format_errors": np.random.randint(2, 10, len(dates)),
    "vendor_conflicts": np.random.randint(1, 15, len(dates)),
})

# Dashboard layout
st.set_page_config(layout="wide")
st.title("📊 Data Stewardship Performance Dashboard")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("ISIN Validity %", f"{df.valid_isin_pct.iloc[-1]:.2f}%")
col2.metric("SLA Compliance %", f"{df.sla_met.iloc[-1]:.2f}%")
col3.metric("Duplicate Records Today", df.dup_records.iloc[-1])

# Line Charts
st.subheader("Quality Trends Over Time")
st.line_chart(df.set_index("date")[["valid_isin_pct", "sla_met"]])

# Error Breakdown
st.subheader("Error Distribution")
errors_df = df[["null_errors", "format_errors", "vendor_conflicts"]].sum().reset_index()
errors_df.columns = ["ErrorType", "Count"]
st.bar_chart(errors_df.set_index("ErrorType"))

# Duplicates Over Time
st.subheader("Duplicate Records Over Time")
st.bar_chart(df.set_index("date")[["dup_records"]])
