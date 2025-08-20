import streamlit as st
import pandas as pd
import numpy as np

# Sample pipeline data
np.random.seed(42)
dates = pd.date_range(start="2025-07-01", periods=30)

pipeline_df = pd.DataFrame({
    "date": dates,
    "jobs_run": np.random.randint(80, 150, len(dates)),
    "success_rate": np.random.uniform(90, 100, len(dates)),
    "avg_time": np.random.uniform(5, 12, len(dates)),
    "records_processed": np.random.randint(5_000_000, 15_000_000, len(dates)),
    "validation_errors": np.random.randint(0, 20, len(dates)),
    "schema_errors": np.random.randint(0, 10, len(dates)),
    "connectivity_errors": np.random.randint(0, 5, len(dates)),
    "timeout_errors": np.random.randint(0, 8, len(dates)),
    "sla_breaches": np.random.randint(0, 3, len(dates))
})

# Layout
st.set_page_config(layout="wide")
st.title("⚙️ Pipeline Performance Dashboard")

# KPI cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Jobs Run Today", pipeline_df.jobs_run.iloc[-1])
col2.metric("Success Rate", f"{pipeline_df.success_rate.iloc[-1]:.2f}%")
col3.metric("Avg Processing Time", f"{pipeline_df.avg_time.iloc[-1]:.1f} min")
col4.metric("Records Processed", f"{pipeline_df.records_processed.iloc[-1]/1_000_000:.1f}M")

# Trends
st.subheader("Pipeline Status Trends")
st.line_chart(pipeline_df.set_index("date")[["success_rate"]])
st.bar_chart(pipeline_df.set_index("date")[["avg_time"]])

# Errors
st.subheader("Error Types Breakdown")
errors_df = pipeline_df[["validation_errors", "schema_errors", "connectivity_errors", "timeout_errors"]].sum().reset_index()
errors_df.columns = ["ErrorType", "Count"]
st.bar_chart(errors_df.set_index("ErrorType"))

# SLA monitoring
st.subheader("SLA Breaches Over Time")
st.bar_chart(pipeline_df.set_index("date")[["sla_breaches"]])
