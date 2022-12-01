import  sys,os
if __name__=='__main__':
 ll=os.popen('echo "ponau"').read()
 z=4*str(ll)
 print(z+str(5.8))
