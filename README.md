# Оптимизация контейнеров

## Установка
* Установить системные зависимости
  * [Install pipenv](https://gist.github.com/slushkovsky/9200486665f8643b1577b4bbee011540)
  * [Install redis](https://gist.github.com/slushkovsky/1adfd21284212f13afeea109d43e7d55)
* Установить python зависимости: `pipenv install`

## Запуск

### Подготовка
* Удостовериться, что redis-server запущен: `service redis start`
* Запустить виртуальное окружение: `pipenv shell`

### Обучение
Для старта выполнить: `python train.py`  
Все данные о состоянии симуляции отправляются в redis (в JSON формате)

### Frontend
Запуск frontend'a: `cd frontend && python app.py`  
Frontend запустится на localhost:5000
