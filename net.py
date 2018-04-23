import tensorflow as tf
import tensorflow.contrib.slim as slim
import numpy as np

from env.log import logger


class Net(object):
    
    def __init__(self, learning_rate, input_count, hidden_count, output_count):
        logger.info(f'Initilizing net (learning rate: {learning_rate}, inputs: {input_count}, hidden: {hidden_count}, outputs: {output_count})')
        self.create_layers(
            input_count=input_count,
            output_count=output_count,
            hidden_count=hidden_count
        )

        self.chosen_action = tf.argmax(self.layer_output, axis=1)

        self.reward_holder = tf.placeholder(shape=[None], dtype=tf.float32, name='reward_holder')
        self.action_holder = tf.placeholder(shape=[None], dtype=tf.int32, name='action_holder')
        
        self.indexes = tf.range(0, tf.shape(self.layer_output)[0]) * tf.shape(self.layer_output)[1] + self.action_holder

        self.responsible_outputs = tf.gather(
            tf.reshape(self.layer_output, [-1]), # Flattern output layer (make in an 1D array)
            self.indexes
        )

        self.loss = -tf.reduce_mean(tf.log(self.responsible_outputs) * self.reward_holder) 
        
        tvars = tf.trainable_variables()
        self.gradient_holders = [tf.placeholder(dtype=tf.float32, name=f'{i}_holder') for i, _ in enumerate(tvars)]
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
