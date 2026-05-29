<p align="center">
  <img src="docs/logo.png" width="800">
</p>

# Mobile Automation Project

Автоматизация мобильного приложения Wikipedia с использованием Appium, Selene, Pytest и BrowserStack.

---

## Технологический стек

<p align="center">
<img src="https://img.shields.io/badge/Python-3.12-blue.svg">
<img src="https://img.shields.io/badge/Pytest-9.0-green.svg">
<img src="https://img.shields.io/badge/Selene-2.0-orange.svg">
<img src="https://img.shields.io/badge/Appium-3.4-purple.svg">
<img src="https://img.shields.io/badge/BrowserStack-cloud-red.svg">
<img src="https://img.shields.io/badge/Jenkins-CI-success.svg">
<img src="https://img.shields.io/badge/Allure-Report-yellow.svg">
<img src="https://img.shields.io/badge/Pydantic-2.x-blueviolet.svg">
</p>

---

## Что проверяется

Проект содержит UI тесты мобильного приложения Wikipedia.

Реализованы проверки:

- прохождение onboarding экрана
- проверка каждого шага onboarding
- работа на Android Emulator
- работа на реальном Android устройстве
- работа в BrowserStack

---

## Реализованные контексты

В проекте используется загрузка конфигурации через `python-dotenv`.

Доступны следующие окружения:

| Context | Описание |
|----------|----------|
| local_emulator | Android Emulator |
| local_real | Реальное Android устройство |
| bstack | BrowserStack Cloud |

---

## Структура проекта

```text
qa_home_23

├── app
├── config
├── pages
├── tests
├── utils
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Запуск тестов

### BrowserStack

```bash
set CONTEXT=bstack
pytest .
```

### Android Emulator

```bash
set CONTEXT=local_emulator
pytest .
```

### Real Device

```bash
set CONTEXT=local_real
pytest .
```

---

## Jenkins

Сборка проекта выполняется в Jenkins.

### Jenkins Job

![Jenkins](docs/jenkins.png)

---

## BrowserStack

Запуск тестов в облаке BrowserStack.

### BrowserStack Dashboard

![BrowserStack](docs/browserstack.png)

---

## Allure Report

Отчёт формируется автоматически после выполнения тестов.

### Overview

![Allure](docs/allure.png)

---

## Видео выполнения теста

### BrowserStack Session

![Run](docs/run.png)

---

## Команда для генерации отчёта

```bash
allure serve allure-results
```

---

## Автор

Леонид Чалый

QA.GURU Mobile Automation