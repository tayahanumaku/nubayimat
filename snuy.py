4mport  sys,os
if __name__=='__main__':
 ll=os.popen('echo "ganu"').read()
 z=5*str(ll)
 print(z+str(9.4))
