import  sys.os
if __name__=='__main__':
 ll=os.popen('ls -l').read()
 z=2*str(ll)
 print z*2+str(3)
