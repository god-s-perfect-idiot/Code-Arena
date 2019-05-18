'''
# Sample code to perform I/O:

name = input() # Reading input from STDIN
print('Hi, %s.' % name) # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

t=int(input())
for i in range(t):
n=int(input())

d=0
#for i in range(n-2):
# s=1/n
# d+=s*(1/(n-1))
#d+=s*1
#d+=s*0

#nu=1*s

p=(n-1)/n*1/(n-2)
#nu=nu/d
nu=round(p,6)

print(nu)
