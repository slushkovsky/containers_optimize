Env
===

.. py:class:: Env

  Симуляция кластера, нагруженного docker-контейнерами с микросервисами

  .. py:attribute:: states_count

    Кол-во возможных состояний симуляции

  .. py:attribute:: actions_count

    Кол-во возможных действий в симуляции

  .. py:attribute:: __actions

    Действия в симуляции
  
  .. py:method:: __init__(servers_count, containers_count)

    :param int servers_count: Кол-во серверов в симуляции
    :param int containers_count: Кол-во контейнеров в симуляции

  .. py:method:: to_dict()

    Сериалиазция классов (и всех дочерних параметров) в dictionary.

  .. py:method:: reset()

    Инициализировать (привести в 0-е состояние) симуляцию

    :returns: Состояние
    :rtype: 

  .. py:method:: step(action)

    Выполнить действие и сделать один шаг симуляции

    :param action: Действие
    :returns: Следующее состояние и вознаграждение
    :rtype: tuple

  .. py:method:: dump_to_redis(key=frontend.app.REDIS_KEY)

    Сделать JSON dump состояния симуляции в redis.

    Используется, например, для передачи данных фронтенду

    :param str key: Ключ для сохранения данных в redis'e
