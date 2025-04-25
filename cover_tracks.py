import requests
from datetime import datetime, timedelta
from selenium import webdriver

# Generate invoice
invoice = {
    "client": "Fake Client Inc.",
    "amount": 5000,
    "date": (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
}
requests.post("https://api.waveapps.com/invoices", json=invoice)
# Encrypt and store on Mega
os.system("veracrypt --create invoice.hc && mega-put invoice.hc /encrypted")
# Setup Nevis shell
driver = webdriver.Chrome()
driver.get("https://www.nevisoffshore.com/company-formation")
driver.find_element_by_id("company_name").send_keys("Nevis Holdings Ltd.")
driver.find_element_by_id("deferred_payment").click()
driver.find_element_by_id("submit").click()
driver.quit()