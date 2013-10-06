import sys
import random

def gauss_2d(mu1, mu2, sigma1, sigma2):
  x = str(random.gauss(mu1, sigma1))
  y = str(random.gauss(mu2, sigma2))
  tuple = (x, y)
  return tuple
  
def my_gauss_2d(n):
  n = 5
  gauss_xy = []

  for i in range(n):
    tuple = gauss_2d(1,0,1,1)
    gauss_xy.append(tuple)
  for i in range(n):
    tuple = gauss_2d(0,1,1,1)
    gauss_xy.append(tuple)
  my_tuple = random.choice(gauss_xy)
  new_gauss_xy_tuple = gauss_2d(float(my_tuple[0]), float(my_tuple[1]), 1/5, 1/5)
  class_tuple_hash = {}
  if my_tuple in gauss_xy[:5]:
    class_tuple_hash[1] = my_tuple
  else:
    class_tuple_hash[2] = my_tuple
  return class_tuple_hash

def generate_two_classes(num):
  classes_hash = {}
  classes_hash[1] = []
  classes_hash[2] = []
  for i in range(num):
    tuple_hash = my_gauss_2d(5)
    if 1 in tuple_hash:
      classes_hash[1].append(tuple_hash[1])
    elif 2 in tuple_hash:
      classes_hash[2].append(tuple_hash[2])
  return classes_hash
  
def main():
  if len(sys.argv) != 3:
    print 'usage: ./gauss2d.py file1-to-write file2-to-write'
    sys.exit(1)
  N = 200
  classes = generate_two_classes(N)
  class1 = classes.get(1)
  class2 = classes.get(2)
  outfile1 = open(sys.argv[1], 'w')
  for i in range(len(class1)):
    outfile1.write(class1[i][0]+', '+class1[i][1]+'\n')
  outfile1.close()
  outfile2 = open(sys.argv[2], 'w')
  for i in range(len(class2)):
    outfile2.write(class2[i][0]+', '+class2[i][1]+'\n')
  outfile2.close()
  
if __name__ == '__main__':
  main()