import sys,os
if __name__=='__main__':
  ll=os.popen('echo "zakora"').read()
  z=6*str(ll)
  print(z+str(9.6))
