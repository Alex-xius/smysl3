import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class BasicInstallTest(unittest.TestCase):  
    '''Я решил прокачаться в когортном анализе
    Зшаел в гугл, ввел запрос и кликнул по одной из ссылок'''

    def setUp(self):  
        self.browser = webdriver.Chrome()  

    def tearDown(self):  
        self.browser.quit()

    def test_page_title(self):  
        # В браузере открылся сайт (по адресу http://127.0.0.1:8000)
        # В заголовке было написано 'Сайт Алексея Исаева'
        self.browser.get('http://localhost:8000')  
        self.assertIn('Сайт Алексея Исаева', self.browser.title)  

    def test_page_header(self):  
        # В шапке сайта написанно "Алексей Исаев"
        self.browser.get('http://localhost:8000')  
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Алексей Исаев', header.text) 


if __name__ == '__main__':  
    unittest.main()

