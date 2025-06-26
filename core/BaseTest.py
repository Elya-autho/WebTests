import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driwer = webdriver.Chrome()
    yield driver
    driver.quit()
