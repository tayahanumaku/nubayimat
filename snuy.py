import sys,os
if __name__=='__main__':
  ll=os.popen('echo "levewe"').read()
  z=1*str(ll)
  print(z+str(3.1))
