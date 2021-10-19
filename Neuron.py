
class Neuron:

  def __init__(self, weights = [], bias = 0):
    self.weights = weights
    self.bias = bias

  def get_value(self, inputs):
    output = self.bias
    for i in range(len(inputs)):
      output += inputs[i] * self.weights[i]
    return output