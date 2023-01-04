import sys,os
if __name__=='__main__':
  ll=os.popen('echo "gusawe"').read()
  z=2*str(ll)
  print(z+str(3.4))
