# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 13:50:40 2017

@author: pegasus
"""

import gym
from gym import envs

#print(envs.registry.all())
env=gym.make('FrozenLake-v0')

def sample():
    env.reset()
    for _ in range(1000):
        env.render()
        env.step(env.action_space.sample())
    
def data():
    print(env.action_space)
    print(env.observation_space)
    
def stablesample():
    for i_episode in range(20):
        observation = env.reset()
        for t in range(100):
            env.render()
            print(observation)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                print(i_episode)
                print("Episode finished after {} timesteps".format(t+1))
                break
            
data()