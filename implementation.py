import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class BinaryStateSpreadingModel:
    def __init__(self, network, spreading_mechanism, beta, gamma):
        """
        Initialize the binary-state spreading model.

        Args:
            network (torch.Tensor): Adjacency matrix of the network (N x N).
            spreading_mechanism (str): Type of spreading mechanism ('SIS', 'SIR', etc.).
            beta (float): Infection rate.
            gamma (float): Recovery rate.
        """
        self.network = network
        self.spreading_mechanism = spreading_mechanism
        self.beta = beta
        self.gamma = gamma
        self.num_nodes = network.shape[0]

    def simulate(self, initial_state, num_steps):
        """
        Simulate the spreading process.

        Args:
            initial_state (torch.Tensor): Initial state of nodes (N,).
            num_steps (int): Number of time steps to simulate.

        Returns:
            torch.Tensor: State of nodes over time (num_steps x N).
        """
        states = torch.zeros((num_steps, self.num_nodes), dtype=torch.float32)
        states[0] = initial_state

        for t in range(1, num_steps):
            current_state = states[t - 1]
            new_state = current_state.clone()

            for i in range(self.num_nodes):
                if current_state[i] == 1:  # Infected
                    if torch.rand(1).item() < self.gamma:
                        new_state[i] = 0  # Recover
                elif current_state[i] == 0:  # Susceptible
                    neighbors = torch.where(self.network[i] > 0)[0]
                    infection_prob = 1 - torch.prod(1 - self.beta * current_state[neighbors])
                    if torch.rand(1).item() < infection_prob:
                        new_state[i] = 1  # Become infected

            states[t] = new_state

        return states

def generate_random_network(num_nodes, edge_prob):
    """
    Generate a random adjacency matrix for an undirected network.

    Args:
        num_nodes (int): Number of nodes in the network.
        edge_prob (float): Probability of an edge between any two nodes.

    Returns:
        torch.Tensor: Adjacency matrix (num_nodes x num_nodes).
    """
    adjacency_matrix = (torch.rand((num_nodes, num_nodes)) < edge_prob).float()
    adjacency_matrix = torch.triu(adjacency_matrix, diagonal=1)
    adjacency_matrix = adjacency_matrix + adjacency_matrix.T
    return adjacency_matrix

if __name__ == '__main__':
    # Parameters
    num_nodes = 10
    edge_prob = 0.2
    beta = 0.3
    gamma = 0.1
    num_steps = 20

    # Generate random network
    network = generate_random_network(num_nodes, edge_prob)

    # Initialize spreading model
    spreading_model = BinaryStateSpreadingModel(network, spreading_mechanism='SIS', beta=beta, gamma=gamma)

    # Initial state (randomly infect some nodes)
    initial_state = (torch.rand(num_nodes) < 0.2).float()

    # Simulate the spreading process
    states = spreading_model.simulate(initial_state, num_steps)

    # Print results
    print("Network adjacency matrix:")
    print(network)
    print("\nInitial state:")
    print(initial_state)
    print("\nStates over time:")
    print(states)