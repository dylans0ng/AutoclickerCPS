from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Installs the driver and accesses the CPS test website before maximizing the window
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://clickspeedtest.com/clicks-per-second.html')
driver.maximize_window()

# Waits for the clicker element to be present
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'clicker'))
)

button_element = driver.find_element(By.ID, 'clicker')

while True:
    try:
        button_element.click()
    except:
        break

current_click_score = driver.find_element(By.ID, 'clicks').text.strip(' CPS')
world_record_cps = driver.find_element(By.CLASS_NAME, 'cps-bold').text.strip(' CPS.') # Gets rid of the CPS. part from the string

if int(current_click_score) > int(world_record_cps):
    print('Congratulations! Your CPS was ' + current_click_score + ' CPS, beating the world record of ' + world_record_cps + '!')
else:
    print('Unfortunately, your CPS of '+ current_click_score + ' did not beat the world record of ' + world_record_cps + '.')

time.sleep(2) # Wait for 2 seconds
driver.quit()