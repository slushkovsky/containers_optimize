State
=====

.. py:class:: State

  Состояние MDP системы в виде списка признаков.
  Данные о контейнерах записываются последовательно друг за другом, в порядке: контейнер1_id_сервера, контейнер1_потребление_cpu, контейнер1_потребление_ram, контейнер1_потребление_трафика, контейнер2_id_сервера...

  .. NOTE::
    
    Класс унаследован от list, поддерживает все его операции

  .. py:method:: __init__(containers, step)

    :param list[Container] containers: Список контейнеров 
    :param int step: Шаг симуляции

  .. py:staticmethod:: get_state_len(containers_count)

    Расчитывает длину stat'a

    :param int containers_count: Кол-во контейнеров 
