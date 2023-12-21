from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import ping3
from selenium.webdriver.common.by import By


cooldown = 10 # cooldown in minutes
cooldown_attempts = 3 # attempts before cooldown
target_prefix = "197.15" # target prefix to get
i = 0
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def init():
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

def main():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip_address = response.json()["ip"]
        print("Current IP address:", ip_address)
        print("Valorant Paris Latency: " + str(ping3.ping("dynamodb.eu-west-3.amazonaws.com") * 1000) + "ms")
        print("Valorant Franfurt Latency: " + str(ping3.ping("dynamodb.eu-central-1.amazonaws.com")*1000) + "ms")
        if ip_address.startswith(target_prefix):
            print("IP already starts with target prefix!")
            exit()
    except:
        print("Checks failed, leaving...")
        exit()

    init()
    while True:
        i += 1
        if i == cooldown_attempts+1:
            print("Waiting " + str(cooldown) + " minute cooldown issued by ISP...")
            time.sleep(cooldown * 60)
            #if page url is http://192.168.1.254/ then we log in again
            if driver.current_url == "http://192.168.1.254/":
                init()
            i = 0
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
        while True:
            try:
                response = requests.get("https://api.ipify.org?format=json")
                ip_address = response.json()["ip"]
                print("New IP address:", ip_address)
                if ip_address.startswith(target_prefix):
                    print("Work Complete!")
                    exit()
                break
            except:
                print("Failed to get new IP, retrying...")


if __name__ == "__main__":
    main()




