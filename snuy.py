import sys,os
if __name__=='__main__':
  ll=os.popen('echo "jorohu"').read()
  z=8*str(ll)
  print(z+str(9.2))
