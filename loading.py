import sys,time
def upto(l):
    """simple loading ui""" 
    lds='|'*10
    c=1
    p=1
    while 1:
        for i in range(len(lds)):
            time.sleep(1)
            print ' {}% {:>5} '.format(p,lds[c:]),
            print '{:<1}'.format(lds[:c]),
            sys.stdout.flush()
            print '\r',
            c+=1
            p+=1
            if c==10:
                c=1
            if p==l:
                return
                
                