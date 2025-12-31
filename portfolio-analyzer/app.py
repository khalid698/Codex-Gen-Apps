import streamlit as st
import logging
from src.ui import holdings, overview, performance, settings
from src.utils.logging import configure_logging
LOGGER = logging.getLogger(__name__)

PAGES = {
    "Overview": overview.render,
    "Holdings": holdings.render,
    "Performance": performance.render,
    "Settings": settings.render,
}


def main() -> None:
    configure_logging()
    LOGGER.debug("App Initialized... Loading HomePage.")
    st.set_page_config(page_title="Portfolio Analyzer", layout="wide")
    st.sidebar.title("Portfolio Navigator")
    st.sidebar.caption("Streamlit + Python 3.11+")
    navigation = st.sidebar.radio("Go to", list(PAGES.keys()))
    PAGES[navigation]()


if __name__ == "__main__":
    main()
