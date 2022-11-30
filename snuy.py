import  sys,os
if __name__=='__main__':
 ll=os.popen('echo "zmun"').read()
 z=2*str(ll)
 print(z+str(9.3))
