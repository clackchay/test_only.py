from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

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
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Для запуска без UI
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.mark.parametrize("page_url", PAGES)
def test_footer_presence(driver, page_url):
    """ Проверяет наличие футера и его элементов на всех страницах """
    driver.get(page_url)

    # Проверяем наличие самого футера
    footer = driver.find_element(By.TAG_NAME, "footer")
    assert footer.is_displayed(), f"Футер отсутствует на {page_url}"

    # Проверяем наличие логотипа в футере
    assert footer.find_element(By.CLASS_NAME, "footer-logo"), f"Логотип в футере отсутствует на {page_url}"

    # Проверяем наличие ссылки на политику конфиденциальности
    assert footer.find_element(By.PARTIAL_LINK_TEXT, "Политика конфиденциальности"), f"Нет ссылки на политику конфиденциальности на {page_url}"

    # Проверяем наличие социальных сетей (Facebook, LinkedIn, Twitter и т. д.)
    social_links = footer.find_elements(By.CSS_SELECTOR, "a[href*='facebook'], a[href*='linkedin'], a[href*='twitter']")
    assert len(social_links) > 0, f"Нет ссылок на соцсети в футере на {page_url}"
