from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from blog.views import home_page


class HomePageTest(TestCase):
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