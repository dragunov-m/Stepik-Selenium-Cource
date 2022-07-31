import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class TestForms(unittest.TestCase):

    def test_first_registration(self):
        # Options
        options = Options()
        #options.add_argument('headless')
        #

        # Service
        service = Service(executable_path='/home/user/chromedriver')
        #

        # Driver
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(5)
        #

        link = "http://suninjuly.github.io/registration1.html"
        driver.get(link)

        # Ваш код, который заполняет обязательные поля
        first = driver.find_element(By.CSS_SELECTOR, '.form-control.first:required')
        first.send_keys('S')
        second = driver.find_element(By.CSS_SELECTOR, '.form-control.second:required')
        second.send_keys('S')
        third = driver.find_element(By.CSS_SELECTOR, '.form-control.third:required')
        third.send_keys('S')

        # Отправляем заполненную форму
        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Something wrong!')

        driver.quit()

    def test_second_registration(self):
        # Options
        options = Options()
        #options.add_argument('headless')
        #

        # Service
        service = Service(executable_path='/home/user/chromedriver')
        #

        # Driver
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(5)
        #

        link = "http://suninjuly.github.io/registration2.html"
        driver.get(link)

        # Ваш код, который заполняет обязательные поля
        first = driver.find_element(By.CSS_SELECTOR, '.form-control.first:required')
        first.send_keys('S')
        second = driver.find_element(By.CSS_SELECTOR, '.form-control.second:required')
        second.send_keys('S')
        third = driver.find_element(By.CSS_SELECTOR, '.form-control.third:required')
        third.send_keys('S')

        # Отправляем заполненную форму
        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Something wrong!')

        driver.quit()


if __name__ == '__main__':
    unittest.main()
