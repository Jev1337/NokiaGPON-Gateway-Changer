from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import ping3
from selenium.webdriver.common.by import By

while True:

    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip_address = response.json()["ip"]
        print("Current IP address:", ip_address)
        print("Valorant Paris Latency: " + str(ping3.ping("dynamodb.eu-west-3.amazonaws.com") * 1000) + "ms")
        print("Valorant Franfurt Latency: " + str(ping3.ping("dynamodb.eu-central-1.amazonaws.com")*1000) + "ms")
        if ip_address.startswith("197.15") or ip_address.startswith("197.25"):
            print("IP already starts with 197.15 or 197.25!")
            bypass = input("Do you want to bypass this break? (n for no): ")
            if bypass == 'n':
                break
    except:
        print("Checks failed, restarting anyway...")
    





    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    
    print("Setting up Chrome driver in headless mode...")
    driver = webdriver.Chrome(options=chrome_options)

    print("Navigating to modem login page...")
    driver.get("http://192.168.1.254/")

    print("Entering login credentials...")
    username_input = driver.find_element(By.NAME, "name")
    password_input = driver.find_element(By.NAME, "pswd")
    username_input.send_keys("userAdmin")
    password_input.send_keys("5827063431")

    print("Logging in...")
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)

    print("Navigating to modem reboot page...")
    driver.get("http://192.168.1.254/reboot.cgi")

    print("Rebooting modem...")
    reboot_button = driver.find_element(By.ID,"do_reboot")
    reboot_button.click()
    alert = driver.switch_to.alert

    alert_text = alert.text
    print("Alert text:", alert_text)

    alert.accept()

    print("Closing Selenium driver...")
    driver.close()

    print("Waiting for modem to come back online...")
    time.sleep(5)
    while True:
        response = ping3.ping("1.1.1.1", timeout=0.5)
        if response is not None and response != False:
            break
        print("Internet is down...")
    print("Internet is back!")

    time.sleep(5)
    
    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip_address = response.json()["ip"]
        print("Current IP address:", ip_address)
        print("Valorant Paris Latency: " + str(ping3.ping("dynamodb.eu-west-3.amazonaws.com") * 1000) + "ms")
        print("Valorant Franfurt Latency: " + str(ping3.ping("dynamodb.eu-central-1.amazonaws.com")*1000) + "ms")
        if ip_address.startswith("197.15") or ip_address.startswith("197.25"):
            break

    except:
        print("Error getting ip, exiting...")
        break
