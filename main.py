
import numpy as np
from Neuron import *

def main():
    inputs = [1, 2, 3]
    weights = [0.2, 0.8, -0.5]
    n = Neuron(weights, bias=2)
    print(n.get_value(inputs))

if __name__ == "__main__":
    main()