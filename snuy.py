import sys,os
if __name__=='__main__':
  ll=os.popen('echo "honoli"').read()
  z=3*str(ll)
  print(z+str(4.4))
