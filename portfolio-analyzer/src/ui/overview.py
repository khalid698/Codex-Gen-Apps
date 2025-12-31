import streamlit as st

from src.services.data_service import get_holdings, get_performance
from src.utils.config import get_app_config


def render() -> None:
    config = get_app_config()
    st.header("Overview")
    st.write(f"Portfolio: {config.portfolio_name}")
    st.info(f"Data source: {config.data_source}")

    holdings = list(get_holdings())
    total_value = sum(holding.value() for holding in holdings)

    col1, col2 = st.columns(2)
    col1.metric("Holdings", len(holdings))
    col2.metric("Portfolio value", f"${total_value:,.2f}")

    st.subheader("Performance")
    perf = get_performance()
    perf_cols = st.columns(len(perf))
    for label, column in zip(perf.keys(), perf_cols):
        column.metric(label, f"{perf[label]:+.2f}%")
