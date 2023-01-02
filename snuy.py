import sys,os
if __name__=='__main__':
  ll=os.popen('echo "qipuc"').read()
  z=9*str(ll)
  print(z+str(1.7))
