import sys,os
storeinput = ''
spacelength = ''
listd = [ld for ld in os.listdir(os.getcwd())]
def dynamic():
    sys.stdout.flush()
    print '\r',
def flush():
    global fn
    fn = raw_input('\nFilename: ')
    if  fn in listd:
        while 1:
            prompt = raw_input('%s exist Overwrite [y/n] '%fn)
            if prompt == 'y':
                ov()
                sys.exit()
            elif prompt == 'n':
                flush()
            else:
                continue
    elif fn == '':
        flush()
    else:
        ov()
        sys.exit()
def ov():
    os.system('touch %s'%fn)
    with open(fn,'w') as f:
        f.write(storeinput)   
    rc = [rc for rc in  open(fn).read() if rc.strip() != '']
    rl = [rl for rl in open(fn)]
    print ' {}C {}L written '.format(len(rc),len(rl))

def sg():
    global temp
    temp = []
    for getinput in i:
        temp.append(getinput)
        if getinput.isalpha():
            break
def f():
    global storeinput,spacelength,i
    while 1:
        try:
            i = raw_input('~ ')
            storeinput += i+'\n'
            if i.startswith(' '):
                sg() 
                slicetemp = len(temp[:-1])
                spacelength += slicetemp*' '
                s()
        except(KeyboardInterrupt):
            flush() 
            sys.exit()
def s():
    global spacelength,storeinput,i
    try:
        while 1:
            indentlength = len(spacelength)+2
            writeindent = len(spacelength)
            i= raw_input(indentlength*' ')
            storeinput += writeindent*' '
            storeinput += i+'\n' 
            if i.startswith(' '): 
                sg()
                slicetemp = len(temp[:-1])
                spacelength += slicetemp*' '
    except (EOFError):
        if len(spacelength)==0:
            dynamic()
            f() 
        else:
            slicetemp = len(temp[:-1]) 
            spacelength = spacelength[:-slicetemp] 
            dynamic() 
            s() 
    except (KeyboardInterrupt):
        flush()
        sys.exit()
print '\n Python Text Editor\n'
try:
    f()
except:
    print '\nEditor Exit!'
    
