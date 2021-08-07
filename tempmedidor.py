from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os


chrome_options = Options()
chrome_options.add_argument("-headless")
driver = webdriver.Chrome(options = chrome_options , executable_path = 'chromedriver.exe')
driver.get("https://www.google.com/search?q=temperatura&oq=temp&aqs=edge.0.69i59l2j0i131i433i512j69i57j69i61j69i60j69i61.1809j0j9&sourceid=chrome&ie=UTF-8")
time.sleep(4)
print("Medidor de temperatura by Gabriel Ricardo o BRABO =)")
time.sleep(4)
print("Aguarde estamos medindo...")
time.sleep(4)
os.system ("cls")
print("Pronto... Aqui esta!!")
time.sleep(1)
tempc = driver.find_element_by_xpath('//*[@id="wob_tm"]')
txttemp = tempc.text
local = driver.find_element_by_xpath('//*[@id="wob_loc"]')
txtlocal = local.text
print ("Sua Temperatura é {}°C".format(txttemp))
print ("Seu local: {}".format(txtlocal))