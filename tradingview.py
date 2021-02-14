from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from PIL import Image
import urllib.request

WEBDRIVER_PATH = '/usr/local/bin/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1024,600")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument('window-size=800x841')

# chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(
    executable_path=WEBDRIVER_PATH,
    options=chrome_options,
    service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])

driver.get('http://www.tradingview.com/chart')
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.ID, 'header-toolbar-symbol-search'))).click()
search: WebElement = driver.find_element_by_class_name('search-1t76YXcC')
search.send_keys(Keys.COMMAND + "a")
search.send_keys("LSE:HUR")
search.send_keys(Keys.ENTER)
time.sleep(2)
# driver.execute_script("document.body.style.zoom='130%'")
toolbar = driver.find_element_by_class_name('toolbar-2n2cwgp5')
hover = ActionChains(driver).move_to_element(toolbar)
hover.perform()
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, 'scrollRight-2SEqCpTf'))).click()
toolbar = driver.find_element_by_id('header-toolbar-screenshot')
hover = ActionChains(driver).move_to_element(toolbar)
hover.perform()
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, 'header-toolbar-screenshot'))).click()
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((
        By.XPATH,
        '//*[@id="overlap-manager-root"]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/a'
    ))).click()
driver.switch_to.window(driver.window_handles[-1])
url = driver.current_url

print(url)
image = Image.open(urllib.request.urlopen(url))
image.save('tvimage.png')
driver.quit()