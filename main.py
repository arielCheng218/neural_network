import numpy as np

def main():
  with open('data_banknote_authentication.txt') as f:
    lines = f.readlines()
    np.random.shuffle(lines)
    inp = []
    exp = []
    for line in lines:
      line = line.split(",")
      inp.append([float(x) for x in line[:3]])
      exp.append([float(line[-1])])
    print(inp)
    print(exp)
    # training set
    
    # testing set

if __name__ == "__main__":
  pass