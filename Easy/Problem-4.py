'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
#Answer
strs = ["dog","racecar","car"]
i=0
n=0
k=0
f=''
while i<len(min(strs, key=len)):
    j=0
    c=strs[0][k]
    while j<len(strs):
        if c==strs[j][i]:
            n=n+1
        j=j+1
    if n==len(strs):
        f=f+strs[0][i]
    else:
        break
    n=0
    i=i+1
    k=k+1
print(f)
    
            
        
        
        
        
        
    