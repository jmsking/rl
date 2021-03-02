import gym
import matplotlib.pyplot as plt

env_name = 'CartPole-v0'

plt.figure(figsize=(5,4))
plt.title(env_name)

env = gym.make(env_name)
env.reset()
for idx in range(1000):
    img = env.render(mode='rgb_array')
    plt.imshow(img)
    env.step(env.action_space.sample())
env.close()