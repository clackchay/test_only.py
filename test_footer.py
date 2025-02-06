from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Список страниц для проверки
PAGES = [
    "https://only.digital/",
    "https://only.digital/services",
    "https://only.digital/cases",
    "https://only.digital/about",
    "https://only.digital/contact"
]

@pytest.fixture(scope="module")
def driver():
    """Запуск браузера Chrome"""
    options = webdriver.ChromeOptions()

    # Правильный вызов драйвера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome
