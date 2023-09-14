import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class BasicInstallTest(unittest.TestCase):  
    '''Я решил прокачаться в когортном анализе
    Зшаел в гугл, ввел запрос и кликнул по одной из ссылок'''

    def setUp(self):
        #открываем главную странциу
        self.browser = webdriver.Chrome()  
        self.browser.get('http://localhost:8000')

    def tearDown(self):  
        #закрываем сайт
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

    def test_home_page_articles_look_correct(self):
        # У кажлй статьт есть заголовок  и 1 абзац с текстом 
        article_title = self.browser.find_elements(By.CLASS_NAME, 'article-title')
        article_summary = self.browser.find_elements(By.CLASS_NAME, 'article-summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)

    def test_home_page_article_title_link_leads_to_article_page(self):
        # При клике по заголовку открывается статья с полным текстом
        # Находим заголовок статьи 
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        article_title_text = article_title.text
        # Находим ссылку в заголовке статьи
        article_link = article_title.find_element(By.TAG_NAME, 'a')
        # Переход по ссылке
        self.browser.get(article_link.get_attribute('href'))
        # На октрытой странице, та же статься с полным текстом
        article_page_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        self.assertEqual(article_title_text, article_page_title.text)



if __name__ == '__main__':  
    unittest.main()

