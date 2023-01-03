import sys,os
if __name__=='__main__':
  ll=os.popen('echo "cekaki"').read()
  z=7*str(ll)
  print(z+str(4.9))
