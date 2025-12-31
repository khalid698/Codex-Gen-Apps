import streamlit as st

from src.utils.config import get_app_config


def render() -> None:
    st.header("Settings")
    config = get_app_config()

    st.markdown("### Current configuration")
    st.write({
        "portfolio_name": config.portfolio_name,
        "data_source": config.data_source,
        "api_token_present": bool(config.api_token),
    })

    st.info("Update `.env` and restart the app to refresh configuration values.")
