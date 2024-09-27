
# Logical Effort Model Simulator for VLSI

This repository contains a Python-based simulator of the Logical Effort model used in Very-Large-Scale Integration (VLSI) design. The Logical Effort model is a powerful method for estimating the delay of digital circuits and helps in optimizing the performance of logic gates by balancing gate sizes across a circuit.

## Features

- Simulates the delay and path optimization using the Logical Effort model.
- Provides insights into the trade-offs between delay, capacitance, and transistor sizes.
- Helps in understanding the optimal configuration for minimizing delay in a VLSI circuit.

## Getting Started

### Prerequisites

To use the simulator, you need the following:

- Python 3.x installed
- Standard libraries such as `numpy`, `matplotlib` for data manipulation and visualization. Install them using:

```bash
pip install numpy matplotlib
```

### Usage

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the directory and run the simulator:
    ```bash
    cd LogicalEffortSimulator
    python LogicalEffortSimulator.py
    ```

3. Follow the instructions to input the parameters for simulating the logical effort.

### Example

Here's a simple example of how to run the simulator:

```bash
# Example command to simulate a simple gate configuration:
python LogicalEffortSimulator.py
```

### Output

The simulator will display the calculated delay, optimal sizing, and other relevant data about the logic gate configuration you provided.

## Logical Effort Theory

The Logical Effort model was introduced in the seminal paper by Ivan Sutherland, Robert Sproull, and David Harris in the following publication:

- **Reference**: Ivan E. Sutherland, Robert F. Sproull, and David Harris, "Logical Effort: Designing for Speed on the Back of an Envelope," IEEE Journal of Solid-State Circuits, vol. 31, no. 2, pp. 236-248, Feb. 1996. [Link to paper](https://doi.org/10.1109/4.485299)

This model provides a method for comparing the delay of different logic gate designs and optimizing them for minimal delay.

## Contribution

Feel free to submit issues and pull requests to improve the simulator or add new features.
