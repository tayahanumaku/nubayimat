import sys,os
if __name__=='__main__':
  ll=os.popen('echo "kawovu"').read()
  z=8*str(ll)
  print(z+str(5.5))
