from selenium import webdriver
from faker import Faker
import requests

fake = Faker()
driver = webdriver.Chrome()
driver.get("https://www.sfm.com/offshore-company-formation/seychelles")

# Generate company name
name = requests.get("https://namelix.com/api/generate").json()["names"][0]
# Get Regus virtual address
address = requests.get("https://www.regus.com/api/locations/seychelles").json()["address"]
driver.find_element_by_id("company_name").send_keys(name + " Ltd.")
driver.find_element_by_id("email").send_keys(fake.email(domain="proton.me"))
driver.find_element_by_id("address").send_keys(address)
driver.find_element_by_id("nominee_director").click()
driver.find_element_by_id("deferred_payment").click()
driver.find_element_by_id("submit").click()
driver.quit()