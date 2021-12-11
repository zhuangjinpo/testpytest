from selenium import webdriver
import time

we = webdriver.Chrome()
we.get("https://www.baidu.com",)
we.maximize_window()
we.find_element_by_id("kw").send_keys("王贵与安娜")
we.find_element_by_id("su").click()
time.sleep(2)
we.find_element_by_xpath('//*[@mu="https://baike.baidu.com/item/王贵与安娜/14136"]/div/div/h3/a').click()
a_handle = we.current_window_handle
handles = we.window_handles

for i in handles:
    if i != a_handle:
        we.switch_to.window(i)
time.sleep(2)
s = we.find_element_by_xpath('//*[@id="posterCon"]/dt/dl/dd[1]/h1').text
if s == "王贵与安娜":
    print("right")

