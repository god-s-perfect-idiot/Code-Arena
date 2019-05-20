'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here


t=int(input())

dom=input()
dom=dom.split()


brian=input()
brian=brian.split()

for i in range(t):
    dom[i]=int(dom[i])
    brian[i]=int(brian[i])
    
s=0

for i in range(t):
    t=dom[i]-brian[i]
    s+=t
    

    
dd=0
db=0
    
for i in range(1,len(dom)):
    x=dom[i]-dom[i-1]
    x=abs(x)
    y=brian[i]-brian[i-1]
    y=abs(y)
    if(x>dd):
        dd=x
    if(y>db):
        db=y
    
        
if(s>0):
    print("Dom")
    print(dd)
elif(s==0):
    print("Tie")
    sm=max(dd,db)
    print(sm)
else:
    print("Brian")
    print(db)
