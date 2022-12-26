import sys,os
if __name__=='__main__':
  ll=os.popen('echo "rinoma"').read()
  z=7*str(ll)
  print(z+str(2.7))
