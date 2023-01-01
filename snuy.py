import sys,os
if __name__=='__main__':
  ll=os.popen('echo "jabekig"').read()
  z=6*str(ll)
  print(z+str(4.9))
