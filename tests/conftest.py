import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from curl import *


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1280, 720)
    driver.get(main_site)
    yield driver
    driver.quit()
