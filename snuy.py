import sys,os
if __name__=='__main__':
  ll=os.popen('echo "qisayey"').read()
  z=2*str(ll)
  print(z+str(2.3))
