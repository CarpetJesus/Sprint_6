import pytest
from selenium import webdriver
from curl import *


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(main_site)
    yield driver
    driver.quit()
