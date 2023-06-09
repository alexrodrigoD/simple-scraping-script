from selenium import webdriver
from bs4 import BeautifulSoup 
import pandas as pd

driver = webdriver.Chrome("C:/bin/chromedriver.exe")

Names = []

driver.get("https://www.fiverr.com/categories/programming-tech/buy/software-development/python?source=pagination&page=2&offset=-1")

content = driver.page_source
soup = BeautifulSoup(content, features="lxml")
for a in soup.findAll('div',attrs={'class':'seller-name'}):
	name = a.find('a', href=True, attrs={'class':'text-semi-bold'})
	Names.append(name.text)

df = pd.DataFrame({'Name':Names}) 
df.to_csv('products.csv', index=False, encoding='utf-8')

# print(Names)