import  sys,os
if __name__=='__main__':
 ll=os.popen('echo "rnausb"').read()
 z=4*str(ll)
 print(z+str(12.8))
