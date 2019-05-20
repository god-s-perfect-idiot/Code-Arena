'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

def factorial(n) :  
  
    fact = 1;  
    for i in range(2, n + 1) : 
        fact = fact * i 
  
    return fact 
  
# Function to find c(n, r)  
def ncr(n, r) : 
      
    return factorial(n) // (factorial(r) * 
                            factorial(n - r)) 

def countWays(string) :  
  
    freq = [0] * 26
    nvowels, nconsonants = 0, 0
  
    # Finding the frequencies of  
    # the characters  
    for i in range(len(string)) : 
        freq[ord(string[i]) - ord('a')] += 1
  
    # finding the no. of vowels and  
    # consonants in given word  
    for i in range(26) : 
  
        if (i == 0 or i == 4 or i == 8
            or i == 14 or i == 20) : 
            nvowels += freq[i]  
        else : 
            nconsonants += freq[i] 
      
    # finding places for the vowels  
    vplaces = nconsonants + 1
  
    # ways to fill consonants 6! / 2!  
    cways = factorial(nconsonants) 
    for i in range(26) : 
        if (i != 0 and i != 4 and i != 8 and
            i != 14 and i != 20 and freq[i] > 1) :  
  
            cways = cways // factorial(freq[i]) 
  
    # ways to put vowels 7C5 x 5!  
    vways = ncr(vplaces, nvowels) * factorial(nvowels) 
    for i in range(26) : 
        if (i == 0 or i == 4 or i == 8 or i == 14
            or i == 20 and freq[i] > 1) : 
            vways = vways // factorial(freq[i])  
  
    return cways * vways


t=int(input())

for i in range(t):
    
    s=input()
    string=list(s)
    
    
    ways=countWays(string)
    if ways == 0:
        print(-1)
    else:
        ways=ways%1000000007
        print(ways)
    
