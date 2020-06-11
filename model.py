#Import Neccesary Libraries

import torch
import torch.nn as nn
import torch.nn.functional as F

#Define the Q_Network
class Q_Network(nn.Module):
    """ Actor (Policy) Model. """

    def __init__(self, state_size, action_size, seed, fc1_units=256, fc2_units=128):
        
        """Initialize parameters and build model.
        Parameters
        ==========
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_units (int): Number of nodes in first hidden layer
            fc2_units (int): Number of nodes in second hidden layer
        """
        
        super(Q_Network, self).__init__()
        self.seed = torch.manual_seed(seed)
        # Define 3 fully connected layers
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.fc2 = nn.Linear(fc1_units, fc2_units)
        self.fc3 = nn.Linear(fc2_units, action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        return self.fc3(x)