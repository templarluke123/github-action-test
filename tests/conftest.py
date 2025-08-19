import os, pytest, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    # 若是 HTTPS 測內網，自簽憑證常見
    opts.add_argument("--ignore-certificate-errors")
    opts.add_argument("--allow-insecure-localhost")

    drv = webdriver.Chrome(options=opts)
    drv.set_page_load_timeout(60)
    yield drv
    drv.quit()

# 測試失敗時自動截圖到 screenshots/，Actions 會上傳 artifacts
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed and "driver" in item.fixturenames:
        d = item.funcargs["driver"]
        os.makedirs("screenshots", exist_ok=True)
        ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        path = f"screenshots/{item.name}-{ts}.png"
        try:
            d.save_screenshot(path)
            print(f"[pytest] Saved screenshot: {path}")
        except Exception as e:
            print(f"[pytest] Screenshot failed: {e}")
