# Yandex Disk Tests

## Обзор

API и UI тесты для Яндекс.Диск.

## Установка

1. Клонировать репозиторий:

```bash
git clone https://github.com/ainurnazirov/yandex_disk_tests.git
```

2. Перейти в директорию проекта:

```bash
cd yandex_disk_tests
```

3. Установить зависимости:

```bash
pip install -r requirements.txt
```

## Использование

Запуск тестов:

```bash
pytest -v -s
```

Чтобы добавить время для обход капчи раскомментируйте строку [здесь](ui_tests/test_ui.py#L54)