import sys,os
if __name__=='__main__':
  ll=os.popen('echo "wirezu"').read()
  z=6*str(ll)
  print(z+str(7.3))
