import loading,random,time
lv1='u a n d o f p t'
four=['adopt','fond','fund','pond','dout']
three=['and','apt','ant','dot','dop','don','dat',
       'dan','duo','fun','fon','fan','fop','fat',
       'fud','not','nap','nod','nut','opt','pad',
       'pan','pat','pot','pod','pun','put','pud',
       'tap','tad','tan','tup','top','tod','tun',
       'out','oat']
two=['an','do','at','to','no','of','on','up']

cl=[]#complete list
pt=[]#points or gold
h=[]#hint
def start():

    print '\nSeperate with Two Letters only'
    while 1:
        for itr in cl:
            print '{}|'.format(itr),#print complete list
        print '\n{l:>40} {t}'.format(t='Left',l=len(two))
        if len(pt)<2:
            print '\n{l:>40} {t}'.format(t='Gold',l=len(pt))
        elif len(pt)>1:    
            print '\n{l:>40} {t}'.format(t='Golds',l=len(pt))
        if len(h)<2:
            print '\n{l:>40} {t}'.format(t='Hint',l=len(h))
        elif len(h)>1:
            print '\n{l:>40} {t}'.format(t='Hints',l=len(h))
        scb='\n{:>30}\n'.format(lv1.upper())#scramble words
        print scb
        i=raw_input(' {d:>5}: '.format(d='Enter to submit'))
        if len(i)>2:#check input
            print '\n\t\ttwo letters only '.upper()
        elif i in two:
            print '\nYou have seperate %s from %s\n'%(i,lv1.upper())
            pt.append(i)
            cl.append(i)
            rm=two.index(i)
            two.pop(rm)
        elif i=='h':
            r=random.randint(0,len(two)-1)
            if len(h)==0:
                print 'You need 5 gold to get 1 hint\n',
            elif len(h)!=0:
                print 'Hint:%s'%two[r]
                h.pop(0)
        elif i in cl:
            print '\n%s has already been seperated!!!'%i.upper()
        elif i not in two:
            print '\n\t0.0 Not in Dictionary 0_0'.upper()
            if len(pt)>0:
                pt.pop(0)
        if len(pt)==5:
            h.append(i)
            pt=[]
        if len(two)==0:
            loading.upto(10)
            level2()
            
def level2():

    print '\nSeperate with Four Letters and one with Five'
    while 1:
        for itr in cl:
            print '{}|'.format(itr),#print complete list
        print '\n{l:>40} {t}'.format(t='Left',l=len(four))
        if len(pt)<2:
            print '\n{l:>40} {t}'.format(t='Gold',l=len(pt))
        elif len(pt)>1:    
            print '\n{l:>40} {t}'.format(t='Golds',l=len(pt))
        if len(h)<2:
            print '\n{l:>40} {t}'.format(t='Hint',l=len(h))
        elif len(h)>1:
            print '\n{l:>40} {t}'.format(t='Hints',l=len(h))
        scb='\n{:>30}\n'.format(lv1.upper())#scramble words
        print scb
        i=raw_input(' {d:>5}: '.format(d='Enter to submit'))
        if len(i)>5:#check input
            print '\n\t\tfour letters only '.upper()
        elif i in four:
            print '\nYou have seperate %s from %s\n'%(i,lv1.upper())
            pt.append(i)
            cl.append(i)
            rm=four.index(i)
            four.pop(rm)
        elif i=='h':
            r=random.randint(0,len(four)-1)
            if len(h)==0:
                print 'You need 5 gold to get 1 hint\n',
            elif len(h)!=0:
                print 'Hint:%s'%four[r]
                h.pop(0)
        elif i in cl:
            print '\n%s has already been seperated!!!'%i.upper()
        elif i not in four:
            print '\n\t0.0 Not in Dictionary 0_0'.upper()
            if len(pt)>0:
                pt.pop(0)
        if len(pt)==5:
            h.append(i)
            pt=[]
        if len(four)==0:
            loading.upto(10)
            level3()
            
def level3():

    print '\nSeperate with Three Letters only'
    while 1:
        for itr in cl:
            print '{}|'.format(itr),#print complete list
        print '\n{l:>40} {t}'.format(t='Left',l=len(three))
        if len(pt)<2:
            print '\n{l:>40} {t}'.format(t='Gold',l=len(pt))
        elif len(pt)>1:    
            print '\n{l:>40} {t}'.format(t='Golds',l=len(pt))
        if len(h)<2:
            print '\n{l:>40} {t}'.format(t='Hint',l=len(h))
        elif len(h)>1:
            print '\n{l:>40} {t}'.format(t='Hints',l=len(h))
        scb='\n{:>30}\n'.format(lv1.upper())#scramble words
        print scb
        i=raw_input(' {d:>5}: '.format(d='Enter to submit'))
        if len(i)>3:#check input
            print '\n\t\tthree letters only '.upper()
        elif i in three:
            print '\nYou have seperate %s from %s\n'%(i,lv1.upper())
            pt.append(i)
            cl.append(i)
            rm=three.index(i)
            three.pop(rm)
        elif i=='h':
            r=random.randint(0,len(three)-1)
            if len(h)==0:
                print 'You need 5 gold to get 1 hint\n',
            elif len(h)!=0:
                print 'Hint:%s'%three[r]
                h.pop(0)
        elif i in cl:
            print '\n%s has already been seperated!!!'%i.upper()
        elif i not in three:
            print '\n\t0.0 Not in Dictionary 0_0'.upper()
            if len(pt)>0:
                pt.pop(0)
        if len(pt)==5:
            h.append(i)
            pt=[]
        if len(three)==0:
            print '\n All Levels Complete'
            


def set():            
    try:
        cel='|*|'*16
        print cel
        print '\n\twinnowing'.upper()
        print '\n\t\t|h| for hint\n'
        print cel
        start()
    except (KeyboardInterrupt,EOFError):
        print 'Exit'   
set()
