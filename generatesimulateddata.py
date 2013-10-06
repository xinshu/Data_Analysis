import sys

def generate_data(beta0, beta1):
  xy = []
  for i in range(50):
    x = -4 + 8.0*float(i)/50.0
#    y = -beta0*x/beta1 + 0.5/beta1
    y = -beta0*x/beta1
    tuple = (str(x), str(y))
    xy.append(tuple)
  return xy

def main():
  if len(sys.argv)!=2:
    print 'usage: ./generatesimulateddata.py simulate.txt'
    sys.exit(1)
  simulate = generate_data(-26.166, 25.484)
  outfile = open(sys.argv[1], 'w')
  for i in range(len(simulate)):
    outfile.write(simulate[i][0]+', '+simulate[i][1]+'\n')
  outfile.close()
  
if __name__ == '__main__':
  main()