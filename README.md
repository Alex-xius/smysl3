## smysl3
Учебный проект по созданию сайта на Django по плйлисту Alexey Kulichevskiy

# Урок 1
- Создал функциональные тесты, чтобы релизовывать функционал исходя из них
- Создал приложение blog и в неём unit тесты, в которых декомпозировал задачи из функциональных тестов
- Создал функцию view которая удовлетворяет и функциональным тестам unit тестам  

# Урок 2
2.1 Коммит: Сделал 2 новых функциональных теста, которые не проходят    
2.2 Коммит:
- Cоздано 2 unit теста, которые необходимо пройти
- Создана моедль Article информацией статей, занесена в базу
- В админку добавлено управление статьями Article
- Произведен рефакторинг функции view
- html код был перенесен в temlate/blog/home_page.html
- Во view добавлен контекст, в который бередаётся QuerySet с Article
- В home_page.html добавлено отображение статей
- Все тесты проходят 

# Урок 3
- Создан новый функциональный тест, внесены правки в юнит тест, на проверку ссылки и создан юнит тест для провеки страницы статьи
- Создана функция во view для статьи 
- Создан шаблон для статьи
- Добавлен url с динамической генерацией по id
- И практически сразу заменен на slug, генерирующийся по тайтлу
- Так же в моедль я добавил функцию get_url, которая через reverse получает ссылку на статью
- И добавил эти самые ссылки в заголовки статей
- Переназначил маг метод __str__ в моедле статьи для кореектного отображения в адмике 
- Все тесты удачно пройдены

# Урок 4
- Создан base.html
- Произведен рефакторинг функциональных тестов
- Так же они были перенесены в отдельную папку
- Создана и подключена статика

# Урок 5
- Произведен рефакторинг наших щаблонов
- Дбавленны шрифты
- Добавоен аватар
- Обновленна статика (base.css)

# Урок 6
- Произведен рефакторинг юнит тестов
- Небольшая доработка стиля домашней страницы
- Большая доработка стиля страницы статьи