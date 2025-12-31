from src.utils.config import get_app_config


def test_app_config_reflects_environment(monkeypatch):
    monkeypatch.setenv("PORTFOLIO_NAME", "Test Portfolio")
    monkeypatch.setenv("DATA_SOURCE", "sample-source")
    monkeypatch.delenv("API_TOKEN", raising=False)
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    config = get_app_config()

    assert config.portfolio_name == "Test Portfolio"
    assert config.data_source == "sample-source"
    assert config.api_token is None
    assert config.log_level == "DEBUG"
