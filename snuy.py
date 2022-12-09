import sys,os
if __name__=='__main__':
  ll=os.popen('echo "tuvi"').read()
  z=8*str(ll)
  print(z+str(5.6))
