# Проект tree-menu:

### Древовидное меню на Django, используя custom template tag.

[Тестовое задание](https://docs.google.com/document/d/1XTnbcXhejyGB-I2cHRiiSZqI3ElHzqDJeetwHkJbTa8/edit)

<br>

## Оглавление:

- [Технологии](#технологии)
- [Установка и запуск](#установка-и-запуск)
- [Описание работы](#описание-работы)
- [Автор](#автор)

<br>

## Технологии:

<details><summary>Подробнее</summary>

**Языки программирования, библиотеки и модули:**

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-blue?logo=python)](https://www.python.org/)

**Фреймворк, расширения и библиотеки:**

[![Django](https://img.shields.io/badge/Django-v5.0.3-blue?logo=Django)](https://www.djangoproject.com/)

**Базы данных и инструменты работы с БД:**

[![SQLite3](https://img.shields.io/badge/-SQLite3-464646?logo=SQLite)](https://www.sqlite.com/version3.html)

[⬆️Оглавление](#оглавление)

</details>

<br>

## Установка и запуск:

Удобно использовать принцип copy-paste - копировать команды из GitHub Readme и вставлять в командную строку Git Bash или IDE (например VSCode).

<details><summary>Запуск</summary>

1. Клонируйте репозиторий с GitHub:

```bash
git clone https://github.com/alexpro2022/Django-tree_menu.git
```

2. Создайте и активируйте виртуальное окружение:

   - Если у вас Linux/macOS

   ```bash
    python -m venv venv && source venv/bin/activate
   ```

   - Если у вас Windows

   ```bash
    python -m venv venv && source venv/Scripts/activate
   ```

3. Установите в виртуальное окружение все необходимые зависимости из файла **requirements.txt**:

```bash
python -m pip install --upgrade pip && pip install -r requirements.txt
```

4. Выполните миграции, загрузку данных, создание суперюзера и запустите приложение:

```bash
python app/manage.py makemigrations && \
python app/manage.py migrate && \
python app/manage.py load_test_data && \
python app/manage.py runserver
```

Сервер запустится локально по адресу `http://127.0.0.1:8000/`

5. Остановить приложение можно комбинацией клавиш Ctl-C.
<h1></h1>
 </details>

<h1></h1></details>

## Описание работы:

На странице `http://<hostname>/menus/` представлены два тестовых меню(если вы выполнили инструкцию [по установке и запуску](#установка-и-запуск)), при клике на название которых происходит раскрытие меню.
Принцип работы приложения основан загрузке из БД всего меню с подзагрузкой подменю с определнными настройки.

[⬆️Оглавление](#оглавление)

<br>

## Автор:

[Артем Суржиков](https://github.com/Surzhikov161)
