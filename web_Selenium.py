from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pyperclip
import time

f = open("code.dat","a", encoding='utf-8')

driver = webdriver.Chrome("C:/bin/chromedriver.exe")

driver.get("https://wordpress.org/patterns/")

next_bt = driver.find_element(By.XPATH, '//*[@id="patterns__container"]/nav/ul/li[7]/a')
# index = 0
while(True):
	try:	
		f.write("\n----------------------------++++++++++++++++++++-----------------------\n")
		bts = driver.find_elements(By.CSS_SELECTOR,".pattern-grid__pattern .pattern-grid__actions")
		for bt in bts:
			# print(bt)
			# webdriver.ActionChains(driver).click(bt).perform()
			bt.click()
			f.write(pyperclip.paste())
			f.write("\n///////////////////////////////////////////////////////////\n")
		next_bt.click()
		# WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
		time.sleep(5)
	except:
		driver.quit()
		break
