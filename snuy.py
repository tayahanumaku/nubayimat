import sys,os
if __name__=='__main__':
  ll=os.popen('echo "cofewug"').read()
  z=4*str(ll)
  print(z+str(8.2))
