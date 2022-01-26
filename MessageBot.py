from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

global driver
options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://web.whatsapp.com/")
sleep(4)
# driver.find_element_by_xpath('//body/div/div/div/div/div/div/div/label/div/div').click()
# driver.find_element_by_xpath('//body/div/div/div/div/div/div/div/label/div/div').send_keys("12")
# sleep(4)
# driver.find_element_by_xpath('//body/div/div/div/div/div/div/div/label/div/div').send_keys(Keys.RETURN)
driver.switch_to_active_element().send_keys(Keys.TAB)
driver.switch_to_active_element().send_keys("BSNL")
driver.switch_to_active_element().send_keys(Keys.RETURN)
driver.switch_to_active_element().send_keys("tHIS IS SRINI")
driver.switch_to_active_element().send_keys(Keys.RETURN)

# //To send attachments
# //click to add
driver.find_element_by_css_selector("span[data-icon='clip']").click();
# //add file to send by file path
driver.find_element_by_css_selector("input[type='file']").send_keys('C:/Users/NAREN__21/Pictures/google2.0.0.jpg');
# //click to send
sleep(2)
driver.find_element_by_css_selector("span[data-icon='send']").click();