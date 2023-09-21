import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from blog.models import Article
from datetime import datetime
import os


class BasicInstallTest(LiveServerTestCase):  
    '''Я решил прокачаться в когортном анализе
    Зшаел в гугл, ввел запрос и кликнул по одной из ссылок'''

    def setUp(self):
        # создаём объект в базе 
        Article.objects.create(
            title='title 1',
            full_text='full_text 1',
            summary='summary 1',
            category='category 1',
            pubdate=datetime.now(),
            slug='title-1'
            )
        
        self.browser = webdriver.Chrome()  
        # поулчаем переменную STAGING_SERVER, если таковая имеется
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.life_server_url = 'http://' + staging_server
        #открываем главную странциу
        self.browser.get(self.live_server_url)

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

    def test_layout_and_styling(self):
        # У заголовка сайта есть отступ > 10 px
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertTrue(header.location['x'] > 10)

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



