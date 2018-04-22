Net
===

.. py:class:: Net

  | Нейронная сеть для решения задачи.
  | Принимает решение - какое действие выполнить на следующем шаге.

  Структура: 

  * входящий слой (кол-во нейронов равно )
  * 1 скрытый слой
  * выходящий слой (кол-во нейронов равно кол-ву возможных действий)



  .. py:attribute:: layer_input

    Входной слой

  .. py:attribute:: layer_hidden

    Скрытый (внутренний) слой

  .. py:attribute:: layer_output

    Выходной слой

  .. py:attribute:: gradients


  .. py:method:: __init__(learning_rate, input_count, hidden_count, output_count)
    
    :param float leraning_reate:
    :param int input_count: Кол-во нейронов на входном слое
    :param int hidden_count: Кол-во нейронов на скрытом (внутреннем) слое
    :param int output_count: Кол-во нейронов на выходящем слое

  .. py:method:: _create_layers(inputs_count, hidden_count, outputs_count)

    Внутренний (приватный) метод, создающий слои сети

    .. NOTE::
      Данный метод является внутренним (приватным) и не предназначен для использования из-вне класса. 
      Если вы все-же хотите это сделать - подумайте три раза

    :param int input_count: Кол-во нейронов на входном слое
    :param int hidden_count: Кол-во нейронов на скрытом (внутреннем) слое
    :param int output_count: Кол-во нейронов на выходном слое


