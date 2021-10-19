
import numpy as np
from Layer import *

def main():

  X = [
    [2, 3, 2, 2.5],
    [2.0, 3.4, 1, 3],
    [1, 3, 2, 6]
  ]

  layer1 = Layer(4, 5)
  layer2 = Layer(5, 2)

  layer1.forward(X)
  layer2.forward(layer1.output)

  print(layer1.output)

main()