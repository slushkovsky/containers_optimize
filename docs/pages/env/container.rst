Container
=========

.. py:class:: Container

  Симуляция docker-контейнера с микросервисом

  .. py:method:: __init__(id, demands, server_id=None)

    :param int id: ID контейнера
    :param ContainerDemands demands: Требования ресурсов контейнера
    :param int server_id: Изначальное положение контейнера. Если None - нигде.

  .. py:classmethod:: create()

    Создание класса с автогенерируемым ID

  .. py:classmethod:: create_random()

    Создание контейнера с произвольными требованиями

  .. py:method:: change_server(server) 

    Переместить контейнер на сервер

    :param int server: Номер сервера, на который необходимо переместить контейнер
    :return: True - контейнер был перемешен. False - контейнер уже находится на сервере
    :rtype: bool

.. py:class:: ContainerDemands

  Описание ресурсов, потребляемых контейнером

  .. py:method:: __init__(cpu_base, cpu_per_request, ram_base, ram_per_request, traffic_per_request, rps_nature)

    :param float cpu_base: Базовое потребление CPU
    :param float cpu_per_request: Потребление CPU на обработку одного запроса
    :param float ram_base: Базовое потребление RAM
    :param float ram_per_request: Потребление RAM на обработку одного запросаа
    :param float traffic_per_request: Потребление трафика на обработку одного запроса
    :param RPSNature rps_nature: Характер изменения нагрузки (rps - requests per second) на серсвис со временем

  .. py:method:: to_dict()

    Сериализация класса в dictionary. Используется для сериализации environment'a в JSON.

  .. py:method:: on_step(step)

    Кол-во ресурсов, необходимое контейнеру на n-ый шаг симуляции

    :param int step: Шаг симуляции

.. py:class:: RPSNature

  Характер изменения RPS сервиса, описывается 3-мя параметрами: func (функция зависимости rps от шага симуляции), factor (множитель rps), max_vlue (предельное значение rps) 

  .. py:attribute:: FUNCS

    Список доступных функций RPS. Записываются в виде словаря. Ключ представляет собой человеко-понятное название функции или её формулу (в дальнейшем используется в print'ах и в сериализации), а так-же lambd'у самой функции в качестве значения

  .. py:method:: __init__(func, factor, max_value, func_name='')

    :param lambda func: Функция зависимости RPS от времени
    :param int factor: Постоянный множитель RPS
    :param int max_value: Максимальное значение RPS
    :param str func_name: Опциональное название функции

  .. py:method:: to_dict()

    Сериализация класса в dictionary.

  .. py:classmethod:: create_random()

    Создание RPSNature c произвольными параметрами

  .. py:method:: on_step(step)

    Значение RPS на n-ом шаге симуляции

    :param int step: Шаг симуляции
    :return: rps на шаге
    :rtype: int
