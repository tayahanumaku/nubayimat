import sys,os
if __name__=='__main__':
  ll=os.popen('echo "wujo"').read()
  z=7*str(ll)
  print(z+str(3.6))
