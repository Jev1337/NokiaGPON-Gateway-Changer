from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import ping3
from selenium.webdriver.common.by import By


try:
    response = requests.get("https://api.ipify.org?format=json")
    ip_address = response.json()["ip"]
    print("Current IP address:", ip_address)
    print("Valorant Paris Latency: " + str(ping3.ping("dynamodb.eu-west-3.amazonaws.com") * 1000) + "ms")
    print("Valorant Franfurt Latency: " + str(ping3.ping("dynamodb.eu-central-1.amazonaws.com")*1000) + "ms")
    if ip_address.startswith("197.15") or ip_address.startswith("197.25"):
        print("IP already starts with 197.15 or 197.25!")
        exit()
except:
    print("Checks failed, Getting New IP anyway...")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

print("Navigating to modem login page...")
driver.get("http://192.168.1.254/")

print("Entering login credentials...")
username_input = driver.find_element(By.NAME, "name")
password_input = driver.find_element(By.NAME, "pswd")
username_input.send_keys("AdminGPON")
password_input.send_keys("ALC#FGU")

print("Logging in...")
password_input.send_keys(Keys.RETURN)

time.sleep(5)

print("Navigating to WAN page...")
driver.get("http://192.168.1.254/wan_config_glb.cgi")


print("Starting Operation...")

select = driver.find_element(By.ID,"conn_id")

select.click()
select.send_keys("2")
select.send_keys(Keys.RETURN)

#while True:
print("Trying to Get New IP...")
checkbox = driver.find_element(By.NAME,"conn_en")
checkbox.click()
button = driver.find_element(By.ID,"do_edit")
button.click()
print("Waiting for refresh...")
time.sleep(6)
checkbox = driver.find_element(By.NAME,"conn_en")
checkbox.click()
button = driver.find_element(By.ID,"do_edit")
button.click()
print("Finishing up...")
time.sleep(6)

print("Checking IP address...")
response = requests.get("https://api.ipify.org?format=json")
ip_address = response.json()["ip"]
print("New IP address:", ip_address)
if ip_address.startswith("197.15") or ip_address.startswith("197.25"):
    print("Shit")





