import  sys,os
if __name__=='__main__':
 ll=os.popen('echo "buandt"').read()
 z=3*str(ll)
 print(z+str(87) )
