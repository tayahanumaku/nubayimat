import sys,os
if __name__=='__main__':
  ll=os.popen('echo "gemowa"').read()
  z=3*str(ll)
  print(z+str(8.7))
