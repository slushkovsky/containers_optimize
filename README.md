# Оптимизация контейнеров

## Pre-requirements
* [Install pipenv](https://gist.github.com/slushkovsky/9200486665f8643b1577b4bbee011540)
* [Install redis](https://gist.github.com/slushkovsky/1adfd21284212f13afeea109d43e7d55)

## Установка

`pipenv install && pipenv shell` - Установит все необходимые зависимости и запустит виртуальное окружение

## Обучение сети
Для старта выполнить: `python train.py`
Все данные о состоянии симуляции отправляюся в redis

Запуск frontend'a: `cd frontend && python app.py`
Frontend запустится на localhost:5000
