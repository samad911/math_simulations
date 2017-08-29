import time
x,y,z,i,n=1,1,1,0,0
l=[1,3,5,7,9,11,13,15]
for z in l:
    for y in l:
        for x in l:
            #main logic with try count
            i=i+1
            print 'The values of x,y,z: ',x,y,z,'\n Try # is:',i
            if (x+y+z)==30:
                print 'Hurrey!!'
                time.sleep(0.5)
                n=1
if i == 512 and n==0:
    print '\n ------------ NO HITS-----------! '
