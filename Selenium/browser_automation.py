from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:/Users/offso/AppData/Local/Programs/Python/Python38-32/Lib/chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

messagefield = driver.find_element_by_xpath('//*[@id="user-message"]')
messagefield.send_keys('Hello')

showbutton = driver.find_element_by_xpath('//*[@id="get-input"]/button').click()

#using Drag and Drop

driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
driver.maximize_window()
source = driver.find_element_by_xpath('//*[@id="box6"]')
dest = driver.find_element_by_xpath('//*[@id="box105"]')
action = ActionChains(driver)
action.drag_and_drop(source,dest).perform()

#imlementing waits importing EC, By,WebDriverWait

driver.get("http://www.google.com/earth")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span'))).click()
