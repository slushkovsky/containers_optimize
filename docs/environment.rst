Симуляция (Env)
===============

.. py:class:: Env

  .. py:method:: __init__(servers_count, containers_count)

    :param int servers_count: Кол-во серверов в симуляции
    :param int containers_count: Кол-во контейнеров в симуляции

  .. py:method:: reset()

    Инициализировать (привести в 0-е состояние) симуляцию

    :returns: Состояние
    :rtype: 

  .. py:method:: step(action)

    Выполнить действие и сделать один шаг симуляции

    :param action: Действие
    :returns: Следующее состояние и вознаграждение
    :rtype: tuple
