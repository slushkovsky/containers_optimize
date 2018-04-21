import tensorflow as tf
import tensorflow.contrib.slim as slim
import numpy as np


class Agent(object):
    '''
        :param: learning_rate:
        :param: states_count: MDP states count
        :param: actions_count: MDP actions count
        :param: hidden_count: Count of neurons on hidden layer of NN

        :attr: layer_input: Input NN layer
        :attr: layer_hidden: Hidden NN layer
        :attr: layer_output: Output NN layer
        :attr: chosen_action: NN result, next MDP action
    '''

    def __init__(self, learning_rate, states_count, actions_count, hidden_count):
        self.create_layers(
            input_count=states_count, 
            output_count=actions_count, 
            hidden_count=hidden_count
        )

        self.chosen_action = tf.argmax(self.layer_output, axis=1)

        #Следующие 6 строк устанавливают процедуру обучения. 
        #Нейросеть принимает на вход выбранное действие
        # и соответствующий выигрыш,
        #чтобы оценить функцию потерь и обновить веса модели.
        self.reward_holder = tf.placeholder(shape=[None], dtype=tf.float32)
        self.action_holder = tf.placeholder(shape=[None], dtype=tf.int32)
        
        self.indexes = tf.range(0, tf.shape(self.layer_output)[0]) * tf.shape(self.layer_output)[1] + self.action_holder

        self.responsible_outputs = tf.gather(
            tf.reshape(self.layer_output, [-1]), # Flattern output layer (make in an 1D array)
            self.indexes
        )
        #функция потерь
        self.loss = -tf.reduce_mean(tf.log(self.responsible_outputs) * self.reward_holder) 
        
        tvars = tf.trainable_variables()
        self.gradient_holders = [tf.placeholder(dtype=tf.float32, name=f'{i}_holder') for i, _ in enumarate(tvars))
        self.gradients = tf.gradients(self.loss, tvars)
        
        optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate) 
        self.update_batch = optimizer.apply_gradients(zip(self.gradient_holders, tvars))

    def create_layers(self, input_count, hidden_count, output_count):
        self.layer_input = tf.placeholder(
            shape=[None, input_count], 
            dtype=tf.float32
        )

        self.layer_hidden = slim.fully_connected(
            inputs=self.layer_input,
            num_outputs=hidden_count,
            biases_initializer=None,
            activation_fn=tf.nn.relu
        )

        self.layer_output = slim.fully_connected(
            inputs=self.layer_hidden,
            num_outputs=output_count,
            biases_initializer=None,
            activation_fn=tf.nn.softmax
        )
