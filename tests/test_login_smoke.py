import os, pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ROUTER_URL = os.getenv("ROUTER_URL", "http://www.routerlogin.com")

@pytest.mark.smoke
def test_login_fields_exist():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=opts)
    try:
        driver.get(ROUTER_URL)
        # 你環境的 DOM：name="username" / name="password"
        assert driver.find_element(By.NAME, "username")
        assert driver.find_element(By.NAME, "password")
    finally:
        driver.quit()
