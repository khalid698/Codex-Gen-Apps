import streamlit as st

from src.services.data_service import get_holdings


def render() -> None:
    st.header("Holdings")
    holdings = list(get_holdings())
    if not holdings:
        st.info("No holdings are currently available.")
        return

    table_data = [
        {
            "Symbol": holding.symbol,
            "Shares": holding.shares,
            "Price": f"${holding.price:,.2f}",
            "Value": f"${holding.value():,.2f}",
        }
        for holding in holdings
    ]

    st.table(table_data)
