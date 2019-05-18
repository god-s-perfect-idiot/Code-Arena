'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

t = int(input())

for i in range(t):
    text=input()
    pattern=input()

    #if pattern in text:
     #   print("YES")
    #lse:
     #   print("NO")
    
    s=text.find(pattern)
    if(s==-1):
        print("NO")
    else:
        print("YES")
