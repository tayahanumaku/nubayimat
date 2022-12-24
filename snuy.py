import sys,os
if __name__=='__main__':
  ll=os.popen('echo "gihuxu"').read()
  z=2*str(ll)
  print(z+str(2.7))
