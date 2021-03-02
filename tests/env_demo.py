import gym

env = gym.make('CartPole-v0')
env.reset()
for idx in range(1000):
    env.render()
    env.step(env.action_space.sample())
env.close()