import streamlit as st

from src.ui import holdings, overview, performance, settings


PAGES = {
    "Overview": overview.render,
    "Holdings": holdings.render,
    "Performance": performance.render,
    "Settings": settings.render,
}


def main() -> None:
    st.set_page_config(page_title="Portfolio Analyzer", layout="wide")
    st.sidebar.title("Portfolio Navigator")
    st.sidebar.caption("Streamlit + Python 3.11+")
    navigation = st.sidebar.radio("Go to", list(PAGES.keys()))
    PAGES[navigation]()


if __name__ == "__main__":
    main()
