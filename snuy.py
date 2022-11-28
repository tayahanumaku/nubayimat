import  sys,os
if __name__=='__main__':
 ll=os.popen('echo "dabim"').read()
 z=2*str(ll)
 print(z+str(8.7))
