from selenium import webdriver
import pytest
from data import *


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(scooter)
    yield driver
    driver.quit()