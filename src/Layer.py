from utils import *
from math import random, cos, pi, log, sqrt

class Layer:

  def __init__(self, input_num, output_num, activation=None):
    self.input_num = input_num
    self.output_num = output_num
    self.activation = activation
    self.weights
    
    # Normally distributed weights (re: https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform)
    self.weights = [sqrt(-2*log(u:=random())) * cos(2*pi*u) for _ in range(input_num)]
    self.bias = 0
  
  def forward(self, inputs):
    self.output = []
    for _ in range(self.output_num):
      neuron_output = dot(inputs, self.weights) + self.bias
      self.output.append(neuron_output)
