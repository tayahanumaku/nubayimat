import sys,os
if __name__=='__main__':
  ll=os.popen('echo "qewil"').read()
  z=1*str(ll)
  print(z+str(5.9))
