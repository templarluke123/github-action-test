import os
from selenium.webdriver.common.by import By

# 可在 GitHub → Settings → Secrets → Actions 設 ROUTER_URL
ROUTER_URL = os.getenv("ROUTER_URL", "http://www.routerlogin.com")

def test_login_fields_exist(driver):
    driver.get(ROUTER_URL)
    # 依你的 DOM（你之前說是 name="username"/"password"）
    driver.find_element(By.NAME, "username")
    driver.find_element(By.NAME, "password")

