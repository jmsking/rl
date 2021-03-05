import argparse
import gym
from itertools import count

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import optim

class Policy(nn.Module):
    def __init__(self):
        super(Policy, self).__init__()
        self.layer1 = nn.Linear(4, 128)
        self.dropout = nn.Dropout(p=0.4)
        self.layer2 = nn.Linear(128, 2)

    def forward(self, inputs):
        x = self.layer1(inputs)
        x = self.dropout(x)
        x = F.relu(x)
        x = self.layer2(x)
        return F.softmax(x, dim=1)

class Reinforce:

    def __init__(self, epochs=10000, gamma=0.3, learning_rate=1e-2,
                    env_name='CartPole-V0'):
        self.epochs = epochs
        self.gamma = gamma
        self.learning_rate = learning_rate
        self.env_name = env_name
        self.model = Policy()
        self.log_probs = []
        self.rewards = []

    def train(self):
        optimizer = optim.Adam(parameters=self.model.parameters(), learning_rate=self.learning_rate)
        env = gym.make(self.env_name)
        for ep in count(1):
            loss = 0
            state = env.reset()
            for step in range(1, self.epochs):
                state = torch.tensor(state)
                action_score = self.model(state)
                action, prob = self.__select_action(action_score)
                self.log_probs.append(torch.log(prob))
                state, reward, _ = env.step(action)
                self.rewards.append(reward)
            accu_rewards = []
            for r in self.rewards[::-1]:
                R = r + self.gamma*R
                accu_rewards.insert(0, R)
            for log_prob, R in zip((self.log_probs, accu_rewards)):
                loss += (R * log_prob)
            

    def predict(self):
        pass

if __name__ == '__main__':
    pass
