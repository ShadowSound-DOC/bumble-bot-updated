from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://bumble.com/")
main_window = driver.current_window_handle

time.sleep(60)




time.sleep(3)


time.sleep(4)
swipe = True
while swipe:
    try:

        like_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span')
        like_button.click()
        print("Liked")
        time.sleep(2)

    except:
        print("Fail")