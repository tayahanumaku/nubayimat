import sys,os
if __name__=='__main__':
  ll=os.popen('echo "kariro"').read()
  z=8*str(ll)
  print(z+str(3.9))
