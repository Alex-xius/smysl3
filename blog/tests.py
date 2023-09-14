from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from blog.views import home_page
from blog.models import Article
from datetime import datetime


class HomePageTest(TestCase):

    def test_home_page_displays_articles(self):
        Article.objects.create(
            title='title 1',
            full_text='full_text 1',
            summary='summary 1',
            category='category 1',
            pubdate=datetime.now()
            )
        Article.objects.create(
            title='title 2',
            full_text='full_text 2',
            summary='summary 2',
            category='category 2',
            pubdate=datetime.now()
        )
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('title 1', html)
        self.assertIn('summary 1', html)
        self.assertNotIn('text 1', html)

        self.assertIn('title 2', html)
        self.assertIn('summary 2', html)
        self.assertNotIn('text 2', html)

    def test_root_url_resolves_to_hone_page_view(self):
        found = resolve('/')  # Иди по этмоу адресу
        # проверь, что функиця которая срабатывает home_page
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  # Создаём запрос
        response = home_page(request)  # Поулчаем ожидаемый ответ
        # Декодируем его из юникода в ютф-8
        html = response.content.decode('utf8')
        # Проверь что в тайтле присутствует Сайт Алексея Исаева
        self.assertIn('<title>Сайт Алексея Исаева</title>', html)
        # Проверь что правда нчало кода начинается с <html>
        self.assertIn('<h1>Алексей Исаев</h1>', html)
        self.assertTrue(html.startswith('<html>'))
        self.assertTrue(html.endswith('</html>'))


class ArticleModelTest(TestCase):

    def test_artical_model_save_and_retrieve(self):
        # создай статью 1, сохрани в базе
        article1 = Article(
            title='article 1',
            full_text='full_text 1',
            summary='summary 1',
            category='category 1',
            pubdate=datetime.now()
        )
        article1.save()

        # создай статью 2, сохрани в базе
        article2 = Article(
            title='article 2',
            full_text='full_text 2',
            summary='summary 2',
            category='category 2',
            pubdate=datetime.now()
        )
        article2.save()

        # Загрузи из базы все статьи
        all_articles = Article.objects.all()
        # проверь: статей должно быть 2
        self.assertEqual(len(all_articles), 2)
        # проверь: первая статья из базы == статья 1
        self.assertEqual(
            all_articles[0].title,
            article1.title
        )
        # проверь: вторая статья из базы == статья 2
        self.assertEqual(
            all_articles[1].title,
            article2.title
        )
