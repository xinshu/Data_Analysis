import sys
import math

def read_data(filename):
  coordinate_list = []
  infile = open(filename, 'r')
  for line in infile:
    w_list = line.split(',')
    coordinate_list.append(w_list)
  infile.close()
  return coordinate_list

def least_square(filename1, filename2):
  class1 = read_data(filename1)
  class2 = read_data(filename2)
  beta_x = 0
  beta_y = 0
  for i in range(len(class2)):
    x = float(class2[i][0])
    y = float(class2[i][1])
    beta_x = beta_x + x*0.5/(x**2+y**2)
    beta_y = beta_y + y*0.5/(x**2+y**2)
  for i in range(len(class1)):
    x = float(class1[i][0])
    y = float(class1[i][1])
    beta_x = beta_x - x*0.5/(x**2+y**2)
    beta_y = beta_y - y*0.5/(x**2+y**2)
  
  cnt = 0
  for i in range(len(class1)):
    x = float(class1[i][0])
    y = float(class1[i][1])
    val = x*beta_x+y*beta_y
#    print val>0.5
    if val>0.0:
      cnt = cnt + 1
#      print cnt
  false_positive = float(cnt)/float(len(class1))
  print false_positive
  
  cnt = 0
  for i in range(len(class2)):
    x = float(class2[i][0])
    y = float(class2[i][1])
    if x*beta_x+y*beta_y < 0.0:
      cnt = cnt + 1
  false_negative = float(cnt)/float(len(class2))
  
  beta_rate_tuple = (beta_x, beta_y, false_positive, false_negative)
  return beta_rate_tuple

def main():
  if len(sys.argv) != 4:
    print 'usage: ./leastsquare.py class1.txt class2.txt write-file'
    sys.exit(1)
#  print read_data(sys.argv[1])[4][1]
  beta_error_rate = least_square(sys.argv[1], sys.argv[2])
  print 'beta_x = ', beta_error_rate[0]
  print 'beta_y = ', beta_error_rate[1]
  print 'flase positive rate = ', beta_error_rate[2]
  print 'flase negative rate = ', beta_error_rate[3]
  outfile = open(sys.argv[3], 'w')
  outfile.write('beta_x = ' + str(beta_error_rate[0]) + '\n')
  outfile.write('beta_y = ' + str(beta_error_rate[1]) + '\n')
  outfile.write('flase positive rate = ' + str(beta_error_rate[2]) + '\n')
  outfile.write('flase negative rate = ' + str(beta_error_rate[3]) + '\n')
  outfile.close()

if __name__ == '__main__':
  main()