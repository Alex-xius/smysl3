import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class BasicInstallTest(unittest.TestCase):  
    '''Я решил прокачаться в когортном анализе
    Зшаел в гугл, ввел запрос и кликнул по одной из ссылок'''

    def setUp(self):
        self.browser = webdriver.Chrome()  
        self.browser.get('http://localhost:8000')

    def tearDown(self):  
        self.browser.quit()

    def test_page_title(self):  
        # В браузере открылся сайт (по адресу http://127.0.0.1:8000)
        # В заголовке было написано 'Сайт Алексея Исаева'
        self.assertIn('Сайт Алексея Исаева', self.browser.title)  

    def test_page_header(self):  
        # В шапке сайта написанно "Алексей Исаев"
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertIn('Алексей Исаев', header.text) 

    def test_home_page_blog(self):
        #Под шапкой расположен блок со статьями
        article_list = self.browser.find_elements(By.CLASS_NAME, 'article-list')
        self.assertTrue(article_list)

    def test_home_page_articales_look_correct(self):
        # У кажлй статьт есть заголовок  и 1 абзац с текстом 
        article_title = self.browser.find_elements(By.CLASS_NAME, 'article-title')
        article_summary = self.browser.find_elements(By.CLASS_NAME, 'article-summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)


if __name__ == '__main__':  
    unittest.main()

