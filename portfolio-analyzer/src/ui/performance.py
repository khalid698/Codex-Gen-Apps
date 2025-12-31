import streamlit as st

from src.services.data_service import get_performance, get_performance_history


def render() -> None:
    st.header("Performance")

    perf = get_performance()
    st.subheader("Recent snapshots")
    perf_cols = st.columns(len(perf))
    for label, column in zip(perf.keys(), perf_cols):
        column.metric(label, f"{perf[label]:+.2f}%")

    history = get_performance_history()
    st.subheader("Trend")
    values = [row["return"] for row in history]
    st.line_chart(values, height=300)
    cleaned = ", ".join(row["date"] for row in history)
    st.caption(f"Monthly checkpoints: {cleaned}")
