import  sys.os
if __name__=='__main__':
 ll=os.popen('ls').read()
 z=3*str(ll)
 print z*8.+str(3)
