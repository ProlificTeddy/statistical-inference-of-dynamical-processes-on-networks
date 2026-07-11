# Statistical Inference of Dynamical Processes on Networks

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![arXiv](https://img.shields.io/badge/arXiv-2607.08672v1-orange)](https://arxiv.org/pdf/2607.08672v1)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)](#)

## Overview

This repository contains an implementation of the research paper **"Statistical inference of dynamical processes on networks"** by Javier Ureña-Carrion, Tiago P. Peixoto, and Gerardo Iñiguez. The paper presents a novel framework for inferring the underlying mechanisms of binary-state spreading processes on networks, such as disease transmission, opinion dynamics, and information diffusion.

The framework uses statistical model selection to identify the most plausible spreading mechanism from observed dynamics, even in the absence of direct information about interaction mechanisms. The authors explore six archetypal spreading mechanisms and analyze their detectability across a broad parameter space, emphasizing the role of network sparsity and phase transitions in improving inference accuracy.

This repository provides a Python implementation of the proposed framework, allowing users to:
- Simulate binary-state spreading processes on networks.
- Perform model selection to infer the most likely spreading mechanism.
- Reproduce key results from the paper.

---

## Core Idea

The paper addresses the challenge of inferring spreading mechanisms on networks when only limited empirical data (e.g., who interacts with whom) is available. The key contributions include:
1. **General Framework for Model Selection:** A statistical approach to distinguish between competing hypotheses of spreading mechanisms based on observed dynamics.
2. **Detectability Analysis:** A systematic exploration of the parameter space to characterize the conditions under which accurate inference is possible.
3. **Empirical Validation:** An assessment of spreading mechanisms across real-world datasets, highlighting the impact of data preprocessing on inference outcomes.

The six archetypal spreading mechanisms analyzed in the paper are:
1. Simple contagion processes (e.g., SIS, SIR models).
2. Complex contagion processes.
3. Threshold models.
4. Voter models.
5. Majority-rule models.
6. Independent cascade models.

The framework leverages asymptotic approximations in the thermodynamic limit to predict inference outcomes in finite systems, providing a robust and scalable solution for real-world applications.

---

## How It Works

The implementation follows these core steps:

1. **Network Generation or Input:**
   - Users can either generate synthetic networks (e.g., Erdős-Rényi, Barabási-Albert) or input real-world network data.

2. **Simulation of Spreading Dynamics:**
   - The script simulates binary-state spreading processes on the network using one of the six predefined mechanisms. Users can specify parameters such as infection rate, recovery rate, or threshold.

3. **Data Collection:**
   - The dynamics are observed over time, and the resulting data (e.g., node states at each timestep) is recorded for inference.

4. **Model Selection:**
   - The framework evaluates the likelihood of different spreading mechanisms given the observed data. It uses statistical techniques to rank the mechanisms and identify the most plausible one.

5. **Visualization and Results:**
   - The script generates visualizations of the spreading dynamics and outputs the inferred mechanism along with its likelihood score.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/statistical-inference-dynamics.git
   cd statistical-inference-dynamics
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. You're ready to go!

---

## Usage

The main script for running the implementation is `implementation.py`. Below are examples of how to use it:

### 1. Simulate Spreading Dynamics
To simulate a binary-state spreading process on a network:
```bash
python implementation.py --mode simulate --network erdos_renyi --nodes 100 --edges 200 --mechanism SIS --infection_rate 0.1 --recovery_rate 0.05 --timesteps 100
```

- `--mode simulate`: Run the simulation mode.
- `--network`: Type of network to generate (`erdos_renyi`, `barabasi_albert`, or `input` for custom networks).
- `--nodes`: Number of nodes in the network (for synthetic networks).
- `--edges`: Number of edges in the network (for synthetic networks).
- `--mechanism`: Spreading mechanism to simulate (`SIS`, `SIR`, `threshold`, etc.).
- `--infection_rate`: Infection rate for the spreading process.
- `--recovery_rate`: Recovery rate for the spreading process.
- `--timesteps`: Number of timesteps to simulate.

### 2. Perform Model Selection
To infer the most likely spreading mechanism from observed data:
```bash
python implementation.py --mode infer --data_path data/simulation_results.csv --mechanisms SIS SIR threshold voter
```

- `--mode infer`: Run the model selection mode.
- `--data_path`: Path to the observed data (CSV file).
- `--mechanisms`: List of mechanisms to consider during inference.

### 3. Visualize Results
To visualize the spreading dynamics and inference results:
```bash
python implementation.py --mode visualize --data_path data/simulation_results.csv --output_path results/visualization.png
```

- `--mode visualize`: Run the visualization mode.
- `--data_path`: Path to the observed data (CSV file).
- `--output_path`: Path to save the visualization.

---

## Example

Here’s a complete example of simulating a spreading process, performing model selection, and visualizing the results:

1. Simulate a simple SIS process on an Erdős-Rényi network:
   ```bash
   python implementation.py --mode simulate --network erdos_renyi --nodes 100 --edges 200 --mechanism SIS --infection_rate 0.1 --recovery_rate 0.05 --timesteps 100
   ```

2. Infer the spreading mechanism:
   ```bash
   python implementation.py --mode infer --data_path data/simulation_results.csv --mechanisms SIS SIR threshold voter
   ```

3. Visualize the results:
   ```bash
   python implementation.py --mode visualize --data_path data/simulation_results.csv --output_path results/visualization.png
   ```

---

## Repository Structure

```
statistical-inference-dynamics/
│
├── implementation.py       # Main script for simulation, inference, and visualization
├── networks/               # Example network data
├── data/                   # Simulated or input data
├── results/                # Output results and visualizations
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Citation

If you use this code, please cite the original paper:

```
@article{urena2023statistical,
  title={Statistical inference of dynamical processes on networks},
  author={Ureña-Carrion, Javier and Peixoto, Tiago P. and Iñiguez, Gerardo},
  journal={arXiv preprint arXiv:2607.08672v1},
  year={2023}
}
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

We acknowledge the authors of the paper for their groundbreaking research and for providing the theoretical foundation for this implementation. Special thanks to the open-source community for providing tools and libraries that made this project possible.