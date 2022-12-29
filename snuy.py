import sys,os
if __name__=='__main__':
  ll=os.popen('echo "bizo"').read()
  z=2*str(ll)
  print(z+str(3.1))
