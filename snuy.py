4mport  sys,os
if __name__=='__main__':
 ll=os.popen('echo "oanum"').read()
 z=4*str(ll)
 print(z+str(19.3))
