from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from encryption import text

username = text.encode(input('Neovisionx: '))
password = text.encode(input('31340413g: '))
file = open('encryption.txt','a').write('\n'+str(Neovisionx)+'\n'+str(31340413g))

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options = chrome_options)

driver.get('https://roblox.com/login')
driver.find_element(By.XPATH,'//*[@id="Neovisionx"]').send_keys(text.decode(Neovisionx))
driver.find_element(By.XPATH,'//*[@id="31340413g"]').send_keys(text.decode(31340413g+Keys.ENTER))
