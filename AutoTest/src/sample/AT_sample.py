from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

print(0)
driver = webdriver.Ie(r"C:\Users\PK-180416-02u\anaconda3\Scripts\IEDriverServer.exe")

print(1)

driver.set_page_load_timeout(10)
try:
    driver.get("http://example.selenium.jp/reserveApp/")
except TimeoutException:
    pass

print(driver.current_url)

print(2)
sleep(5)

print(3)
print(driver.current_url)

print(4)
element_year = driver.find_element_by_id("reserve_year")
element_month = driver.find_element_by_id("reserve_month")
element_day = driver.find_element_by_id("reserve_day")
element_guest_name = driver.find_element_by_id("guestname")
element_next_button = driver.find_element_by_id("goto_next")

print(5)
sleep(3)
element_year.clear()
element_year.send_keys("2020")

print(6)
sleep(3)
element_month.clear()
element_month.send_keys("7")

print(7)
sleep(3)
element_day.clear()
element_day.send_keys("20")

print(8)
sleep(3)
element_guest_name.send_keys("テスト太郎")

print(9)
driver.set_page_load_timeout(30)
try:
    element_next_button.click()
    print("クリックok")
    print(driver.current_url)
except TimeoutException:
    pass

print(10)
print(driver.current_url)

print(11)
sleep(10)
element_submit = driver.find_element_by_id("commit")
element_submit.submit()

print(12)
sleep(10)
driver.close()
driver.quit()

print(13)