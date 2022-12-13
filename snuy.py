import sys,os
if __name__=='__main__':
  ll=os.popen('echo "kowu"').read()
  z=1*str(ll)
  print(z+str(8.8))
