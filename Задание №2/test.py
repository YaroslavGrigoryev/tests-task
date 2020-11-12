import time
from selenium import webdriver

driver = webdriver.Chrome() #запускаем наш Driver
driver.maximize_window()

driver.get('https://coinmarketcap.com/') #открываем страничку

change_language = driver.find_element_by_xpath('//div[@id="__next"]/div/div/div[3]/div/div/div[2]/div[3]/div/div/button')
change_language.click()
time.sleep(2)

lang_ru = driver.find_element_by_xpath("//a[@href='/ru/']"); #найти ссылку /ru/
lang_ru.click()
time.sleep(2)

change_language = driver.find_element_by_xpath('//div[@id="__next"]/div/div/div[3]/div/div/div[2]/div[3]/div/div/button')
change_language.click()
time.sleep(2)

lang_vi = driver.find_element_by_xpath("//a[@href='/vi/']"); 
lang_vi.click()
time.sleep(2)

change_language = driver.find_element_by_xpath('//div[@id="__next"]/div/div/div[3]/div/div/div[2]/div[3]/div/div/button')
change_language.click()
time.sleep(2)

lang_tr = driver.find_element_by_xpath("//a[@href='/tr/']"); 
lang_tr.click()
time.sleep(2)

change_language = driver.find_element_by_xpath('//div[@id="__next"]/div/div/div[3]/div/div/div[2]/div[3]/div/div/button')
change_language.click()
time.sleep(2)

lang_es = driver.find_element_by_xpath("//a[@href='/es/']"); 
lang_es.click()

