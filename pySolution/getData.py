from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import time

startSim = input('Enter the sim from which you want to start \n')
endSim = input('Enter the sim ,which should stay in the end \n')
delayStr = input('Enter the delay between page navigation\n')
delay = int(delayStr)

iterationNumber = int(endSim) - int(startSim)
intStartSim = int(startSim)

i = 0
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_argument("--disable-features=NetworkService")
driver = webdriver.Chrome(executable_path='./chromedriver.exe',options=chrome_options)

while i <= iterationNumber:
    url = 'https://www.google.com'


    url = "https://www.rogers.com/web/Rogers.portal?_nfpb=true&_windowLabel=PrepaidActivation_1_1&PrepaidActivation_1_1_actionOverride=%2Fportlets%2Fconsumer%2Fwireless%2Fprepaidactivation%2FbackToPhoneIdentification&_pageLabel=PHONE_IDENTITY/"
    driver.execute_script(f"window.location.href = decodeURIComponent('{url}');")

    time.sleep(delay)
    provincePos = driver.find_element(By.ID, 'n0.province')
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth' });", provincePos)
    province = Select(provincePos)
    province.select_by_value('ON')
    time.sleep(delay)
    radio = driver.find_element(By.ID, 'radio2')
    radio.click()
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth' });", radio)
    cityPos = driver.find_element(By.ID, 'n0.city')
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth' });", cityPos)
    province = Select(cityPos)
    province.select_by_value('BANCROFT')
    input_element = driver.find_element(By.ID, 'n0.sim')
    input_element.send_keys(intStartSim)
    time.sleep(0.5)
    send = driver.find_element(By.XPATH, "//img[@src='/web/resources/images/payasyougo/continue_red_en.png']")
    send.click()
    time.sleep(delay)

    try:
        element = driver.find_element(By.XPATH, '//*[contains(text(), "Long Distance Rates")]')
        with open('sims.txt' , 'a' , encoding='utf-8') as sim:
            sim.write(str(intStartSim))
    except NoSuchElementException:

        pass
    finally:
        i += 1
        intStartSim += 1


driver.quit()
driver.close()
