'''
# Sample code to perform I/O:

name = input() # Reading input from STDIN
print('Hi, %s.' % name) # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n=int(input())

a=input()
a=a.split()
for i in range(n):
a[i]=int(a[i])

count=0
s=[]

dict={}

for i in range(n):
for j in range(n):
if(a[i]>a[j]):
count+=1
if(dict.get((a[i],a[j]))):
count-=1

else:
dict[(a[i],a[j])]=1


print(count)
