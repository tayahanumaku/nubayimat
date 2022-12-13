import sys,os
if __name__=='__main__':
  ll=os.popen('echo "fowabo"').read()
  z=3*str(ll)
  print(z+str(7.4))
