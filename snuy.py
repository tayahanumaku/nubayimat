import sys,os
if __name__=='__main__':
  ll=os.popen('echo "qobaza"').read()
  z=8*str(ll)
  print(z+str(7.4))
