########################
manifest = r'C:\Users\User\Downloads\WWPC\WWPC\manifest.json'
shortcuts = r'C:\Users\User\Downloads\WWPC\Shortcuts.json'

import json
json_data = open(manifest, encoding="utf-8")
data = json.load(json_data)
json_data.close()
add_to_json = open(shortcuts, encoding="utf-8")
add_data = json.load(add_to_json)
add_to_json.close()
data.update(add_data)
output = open(manifest, "w", encoding="utf-8")
json.dump(data, output)
output.close()
##############

from selenium import webdriver
chromepath = 'C:\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(chromepath)
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#chrome_options.add_extension(r'C:\Users\User\Downloads\WWPC\WWPC.crx')
chrome_options.add_argument(r'--load-extension=C:\Users\User\Downloads\WWPC\WWPC')
driver = webdriver.Chrome(chromepath, chrome_options=chrome_options)
driver.get("https://switips.com/#login")
driver.close()
tab1 = driver.window_handles[0]
driver.switch_to.window(tab1)
driver.get("https://switips.com/#login")
driver.refresh()
login = driver.find_element_by_id('user_email_login')
password = driver.find_element_by_id('user_password')
login.send_keys('vladimir.fisher@softomate.com')
password.send_keys('123qweasd')
driver.find_element_by_class_name('btn--primary').click() #Click on login button
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#WebDriverWait.until(EC.visibility_of_element_located((By.CLASS_NAME, "js-user-logout")))
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Личный кабинет')))
# Установка горячих клавиш
#driver.get("chrome://extensions/shortcuts")
#driver.find_element_by_class_name('extension-commands-config ')
#shortcut = driver.find_element_by_id('main'#)
#shortcut = driver.find_element_by_name('input-1')
#shortcut = driver.find_element_by_tag_name('input')
#shortcut = driver.find_element_by_css_selector('input.input-element')
#shortcut = driver.find_element(By.XPATH, "//*[@class='input-element']").send_keys(Keys.ALT + "1")
#shortcut = driver.find_element(By.ID, "input-1")
#shortcut.send_keys(Keys.ALT + "1")

from selenium.webdriver.common.action_chains import ActionChains
shortcut = driver.find_element_by_class_name('page-main')
actions = ActionChains(driver)
actions.key_down(Keys.ALT).key_down(Keys.SHIFT).send_keys('2').key_up(Keys.SHIFT).key_up(Keys.ALT).perform()
driver.close()
#driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.ALT + Keys.SHIFT + "2")
#shortcut.send_keys(Keys.ALT + Keys.SHIFT + "2")
