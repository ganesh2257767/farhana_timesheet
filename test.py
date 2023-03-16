from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta
import time
import os
import csv

username = os.environ.get('user_name')
password = os.environ.get('password')
print(username, password)

options = Options()
options.headless = True

c_options = webdriver.ChromeOptions()

download_path = r"C:\Users\ganeshku\OneDrive - AMDOCS\Backup Folders\Desktop\Farhana\\"

prefs = {
    "download.default_directory": download_path
}

c_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path=r"C:\Users\ganeshku\3DObjects\chromedriver.exe", chrome_options=c_options)
driver.maximize_window()
driver.get("https://app.brighthr.com/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"/html/body/div/div[2]/form/fieldset/div[1]/div/input").send_keys(username)
driver.find_element(By.XPATH,"/html/body/div/div[2]/form/fieldset/div[2]/div/input").send_keys(password)
driver.find_element(By.XPATH,"/html/body/div/div[2]/form/fieldset/div[3]/button[1]").click()
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div/div/a[6]/div/div").click()
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/nav/a[3]/div[2]/span").click()
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/form/div/div[1]/div[1]/div/div[2]/input").click()
select = Select(driver.find_element(By.ID,"week"))
select.select_by_visible_text("Custom dates")
driver.find_element(By.ID,"daypicker").click()

def get_date_range():

    input_dt = datetime.today()
    first_day = input_dt.replace(day=1)
    next_month = input_dt.month + 1
    
    if next_month == 13:
        next_month = 1

    last_day = datetime(input_dt.year, next_month, 1) - timedelta(days=1)
    first_day_of_month = first_day.strftime("%a %b %d %Y")
    last_day_of_month = last_day.strftime("%a %b %d %Y")

    x1 = f"//div[@aria-label='{first_day_of_month}']"
    x2 = f"//div[@aria-label='{last_day_of_month}']"
    return x1, x2

x1, x2 = get_date_range()

driver.find_element(By.XPATH, x1).click()
driver.find_element(By.XPATH, x2).click()
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/form/div/div[5]/div/div/div[2]/div/div[2]/div[2]/div[2]/button[2]").click()
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[3]/form/div/div[7]/button[1]").click()
time.sleep(15)
driver.close()

