from django.urls import resolve, reverse
from django.test import TestCase
from django.http import HttpRequest
from blog.views import home_page, article_page
from blog.models import Article
from datetime import datetime
from pytils.translit import slugify


class ArticlePageTest(TestCase):

    def test_article_page_dysplays_correct_article(self):
        Article.objects.create(
            title='title 1',
            full_text='full_text 1',
            summary='summary 1',
            category='category 1',
            pubdate=datetime.now(),
            slug='title-1'
            )

        request = HttpRequest()
        response = article_page(request, 'title-1')
        html = response.content.decode('utf8')

        self.assertIn('title 1', html)
        self.assertNotIn('summary 1', html)
        self.assertIn('text 1', html)


class HomePageTest(TestCase):

    def test_home_page_displays_articles(self):
        Article.objects.create(
            title='title 1',
            full_text='full_text 1',
            summary='summary 1',
            category='category 1',
            pubdate=datetime.now(),
            slug='title-1'
            )
        Article.objects.create(
            title='title 2',
            full_text='full_text 2',
            summary='summary 2',
            category='category 2',
            pubdate=datetime.now(),
            slug='title-2'
        )
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('title 1', html)
        self.assertIn('blog/title-1', html)
        self.assertIn('summary 1', html)
        self.assertNotIn('text 1', html)

        self.assertIn('title 2', html)
        self.assertIn('blog/title-2', html)
        self.assertIn('summary 2', html)
        self.assertNotIn('text 2', html)

    def test_home_page_returns_correct_html(self):
        url = reverse('home-page')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'blog/home_page.html')


class ArticleModelTest(TestCase):

    def test_artical_model_save_and_retrieve(self):
        # создай статью 1, сохрани в базе
        article1 = Article(
            title='article 1',
            full_text='full_text 1',
            summary='summary 1',
            category='category 1',
            pubdate=datetime.now(),
            slug='title-1'
        )
        article1.save()

        # создай статью 2, сохрани в базе
        article2 = Article(
            title='article 2',
            full_text='full_text 2',
            summary='summary 2',
            category='category 2',
            pubdate=datetime.now(),
            slug='title-1'
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

        self.assertEqual(
            all_articles[0].slug,
            article1.slug
        )

        self.assertEqual(
            all_articles[1].slug,
            article2.slug
        )
