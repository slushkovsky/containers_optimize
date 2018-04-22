Server
======

.. py:class:: Server

   Симуляция сервера в кластере

  .. py:method:: __init__(id, resources, name='')

    :param int id: ID сервера 
    :param Resources resources: Параметры сервера (CPU, RAM, badwidth)
    :param str name: Опциональное имя для сервера

  .. py:method:: to_dict()

    Сериализация класса в dictionary. Используется для сериализации environment'a в JSON

  .. py:classmethod:: create()

    Внутренний метод. Создает класс автматически генерируя ID (id = порядковому номеру создаваемого класса)

  .. py:classmethod:: random_aws_instance(instances_file='aws_instances.json')

    Создает произвольный AWS сервер. Список доступных вариантов серверов содержится в JSON файле.

    :param str instances_file: Путь к JSON файлу со списком доступных конфигураций

  .. py:method:: calc_overload(sum_demands)

    Расчет перегрузки сервера при суммарной мощности выполняемых сервисов sum_demands

    :param Resources sum_demands: Суммарная мощность выполняемых контейнеров
    :return: Перегрузка по CPU, RAM, badwidth. Меньше 1 - ОК, больше - перегрузка
    :rtype: tuple(float, float, float)

