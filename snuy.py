import sys,os
if __name__=='__main__':
  ll=os.popen('echo "dabinig"').read()
  z=3*str(ll)
  print(z+str(3.7))
