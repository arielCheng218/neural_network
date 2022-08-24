from Layer import Layer

def main():
  input = [1, 2, 2]

  layer1 = Layer(3, 2)
  layer2 = Layer(2, 1)

  layer1.forward(input)
  layer2.forward(layer1.output)

  print(layer2.output)

main() 