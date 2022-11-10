import  sys,os
if __name__=='__main__':
 ll=os.popen('echo "fon"').read()
 z=4*str(ll)
 print z+str(76)
