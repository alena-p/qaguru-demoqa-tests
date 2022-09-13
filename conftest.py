import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def browser_config():
    browser.config.base_url = "https://demoqa.com"
    browser.config.browser_name = "chrome"
    #browser.config.window_width = 760
    #browser.config.window_height = 1024

    yield
