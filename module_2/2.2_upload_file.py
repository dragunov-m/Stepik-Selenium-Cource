import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def upload_file():
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

    url = 'http://suninjuly.github.io/file_input.html'
    driver.get(url)

    first_input = driver.find_element(By.XPATH, '//input[@name="firstname"]')
    second_input = driver.find_element(By.XPATH, '//input[@name="lastname"]')
    third_input = driver.find_element(By.XPATH, '//input[@name="email"]')

    first_input.send_keys('firstname')
    second_input.send_keys('lastname')
    third_input.send_keys('email')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_join = os.path.join(current_dir, '2.2_upload_file_sample.txt')

    upload_button = driver.find_element(By.ID, 'file')
    upload_button.send_keys(file_join)

    button_submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
    button_submit.click()

    alert_message = driver.switch_to.alert
    alert_text = alert_message.text

    print(alert_text)

    driver.quit()


if __name__ == '__main__':
    upload_file()
