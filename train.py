import tensorflow as tf
import numpy as np

from net import Net
from history import History
from env.env import Env
from env.log import logger
import settings


if __name__ == '__main__':
    servers_count = 3
    containers_count = 20

    tf.reset_default_graph() #Очищаем граф tensorflow

    env = Env(servers_count=servers_count, containers_count=containers_count)
    net = Net(
        learning_rate=settings.LEARNING_RATE,
        input_count=env.state_size,
        output_count=env.actions_count,
        hidden_count=settings.NN_HIDDEN_COUNT
    )

    history = History()

    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)
     
        gradBuffer = sess.run(tf.trainable_variables())

        for i, grad in enumerate(gradBuffer):
            gradBuffer[i] = 0
            
        state = env.reset()
        
        for iter_num in range(settings.TRAIN_ITERATIONS):
            action = sess.run(
                net.chosen_action,
                feed_dict={
                    net.layer_input: [state]
                }
            )

            new_state, step_reward = env.step(action[0])
            history.add(state, action, step_reward, new_state)
            
            state = new_state

            grads = sess.run(
                net.gradients,
                feed_dict={
                    net.reward_holder: history.discounted_rewards(gamma=settings.REWARD_HISTORY_DISCOUNT),
                    net.action_holder: history.get_actions(),
                    net.layer_input: np.vstack(history.get_states())
                }
            )

            for i, grad in enumerate(grads):
                gradBuffer[i] += grad

            if iter_num % settings.UPDATE_FREQUENCY == 0 and iter_num != 0:
                sess.run(net.update_batch, feed_dict=dict(zip(net.gradient_holders, gradBuffer)))
                
                gradBuffer = [0] * len(gradBuffer)
            
            if iter_num % settings.PRINT_TIMEOUT_ITERATIONS == 0:
                print(np.mean(history.get_rewards()[-100:]))
