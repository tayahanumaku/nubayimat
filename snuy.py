import  sys,os
if __name__=='__main__':
 ll=os.popen('echo "iwanchi"').read()
 z=5*str(ll)
 print(z+str(812.1))
