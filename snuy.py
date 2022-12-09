import sys,os
if __name__=='__main__':
  ll=os.popen('echo "zofiki"').read()
  z=2*str(ll)
  print(z+str(5.1))
