Utils
=====

.. py:class:: Resources

  .. py:method:: __init__(cpu, ram, traffic)

    :param float cpu: Значение ресурса CPU
    :param float ram: Значение ресурса RAM
    :param float traffic: Значение ресурса badwidth

  .. py:method:: to_dict()

    Сериализация класса в dictionary. Используется для сериализации environment'a в JSON

