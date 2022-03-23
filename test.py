import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup


PATH = "/Web Scrapping/chromedriver/chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("http://labservices.icddrb.org/biochemistry")

x = driver.find_element(By.NAME, 'dataTable_length')
drop = Select(x)

# Select by value [for All data showing]
drop.select_by_value("-1")

# select by visible text
# drop.select_by_visible_text('All')

all_rows = driver.find_elements(By.XPATH, "//table[@id= 'dataTable']/tbody/tr[*]")

print(len(all_rows))

lab_test_url = []

for a in driver.find_elements(By.XPATH, './/a'):
    # print(a.get_attribute('href'))
    lab_test_url.append(a.get_attribute('href'))
print(lab_test_url)


def counter(x):
    x = len(lab_test_url)
    x = x - 1
    return x


def new_window_visit(visit_url, count):
    # Open a new window
    driver.execute_script("window.open('');")
    # Switch to the new window and open new URL
    driver.switch_to.window(driver.window_handles[count])
    driver.get(visit_url)
    time.sleep(5)


for i in range(len(lab_test_url)):
    new_window_visit(lab_test_url[i], i)


# driver.quit()
# for a in r:
#     print(a.text)
# a.click()
# x = driver.find_element(By.CLASS_NAME, 'col-md-12')
# print(x.text)
#
# driver.quit()

