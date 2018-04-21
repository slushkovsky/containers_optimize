import tensorflow as tf
import numpy as np

from agent import Agent
from history import History
from env import env
import settings


if __name__ == '__main__':
    servers_count = 2
    containers_count = 2

    tf.reset_default_graph() #Очищаем граф tensorflow

    env = Env(server_count=servers_count, containers_count=containers_count)
    net = Agent(
        learning_rate=settings.LEARNING_RATE,
        states_count=env.states_count,
        actions_count=env.actions_count,
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
            out = sess.run(
                net.layer_output,
                feed_dict={
                    net.state_in: [state]
                }
            )

            new_state, step_reward = env.step(action)
            history.add(state, action, step_reward, new_state)
            
            state = new_state

            grads = sess.run(
                net.gradients,
                feed_dict={
                    net.reward_holder: history.discounted_rewards(gamma=settings.REWARD_HISTORY_DISCOUNT),
                    net.action_holder: history.get_actions(),
                    net.state_in: np.vstack(history.get_states())
                }
            )

            for i, grad in enumerate(grads):
                gradBuffer[i] += grad

            if iter_num % settings.UPDATE_FREQUENCY == 0 and iter_num != 0:
                sess.run(net.update_batch, feed_dict=dict(zip(net.gradient_holders, gradBuffer)))
                
                gradBuffer = [0] * len(gradBuffer)
            
            if iter_num % settings.PRINT_TIMEOUT_ITERATIONS == 0:
                print(np.mean(history.get_rewards()[-100:]))
