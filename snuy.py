import sys,os
if __name__=='__main__':
  ll=os.popen('echo "fasoyey"').read()
  z=8*str(ll)
  print(z+str(9.6))
