import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
@pytest.fixture
def driver():
    # AJUSTEMENT CLOUD 1 : Mode Headless obligatoire pour GitHub Actions
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
   
    # AJUSTEMENT CLOUD 2 : Déconnexion sécurisée (uniquement si le bouton est présent)
    try:
        logout_btn = browser.find_elements(By.CSS_SELECTOR, ".logout")
        if logout_btn:
            logout_btn[0].click()
    except Exception:
        pass # Évite de faire planter le teardown si le test a échoué avant
    browser.quit()