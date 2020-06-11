
# Project 1: Navigation

### Deep Reinforment Learning Project (Navigation)

This project contains an implementation of an agent that navigate a square world to collect yellow bananas

![Agent](./images/simulation.gif)

### Environment

The environment for this project is based on [Unity ML Agent](https://github.com/Unity-Technologies/ml-agents).
The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. 

Four discrete actions are available, corresponding to:

#### Actions
- **`0`** - Move Forward.
- **`1`** - Move Backward.
- **`2`** - Turn Left.
- **`3`** - Turn Right.

#### Rewards
A reward of ```+1``` is provided for collecting a yellow banana
A reward of ```-1``` is provided for collecting a blue banana. Thus, the goal of the agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The task is episodic, and in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes.

### Environment Setup

#### 1. Python

- Follow the instructions in the [DRLND GitHub repository](https://github.com/udacity/deep-reinforcement-learning#dependencies) to set up your Python environment.

- Install Pytorch and other dependencies

#### 2. Unity ML-Agent

1. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux_NoVis.zip) to obtain the environment.

- Clone the project to have access to it locally

### 3. Run the Navigation Notebook

You can train the Agent in 2 ways:

1. Run the notebook within Udacity Online Workspace.

2. Build the environment locally.

You can use the simulator locally to watch the agent.


```python

```
