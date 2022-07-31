from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


def select_list():
    # Options
    options = Options()
    options.add_argument('headless')
    #

    # Service
    service = Service(executable_path='/home/user/chromedriver')
    #

    # Driver
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    #

    url = 'http://suninjuly.github.io/selects1.html'
    driver.get(url)

    number_1 = driver.find_element(By.ID, 'num1').text
    number_2 = driver.find_element(By.ID, 'num2').text

    summ_of_numbers = int(number_1) + int(number_2)

    select = Select(driver.find_element(By.CLASS_NAME, 'custom-select'))
    select.select_by_value(str(summ_of_numbers))

    button_submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
    button_submit.click()

    alert_message = driver.switch_to.alert
    alert_text = alert_message.text

    print(alert_text)

    driver.quit()


if __name__ == '__main__':
    select_list()
