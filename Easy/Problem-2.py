#Given an integer x, return true if x is a palindrome, and false otherwise.

#Example 1:
#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.

#Example 2:
#Input: x = -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

#Example 3:
#Input: x = 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

#Answer
x = int(input("Enter a number: "))
if x<0:
    print("False")
else:
    c=x
    y=0
    while c>0:
        y=y*10+(c%10)
        c=c//10
    if y==x:
        print('True')
    else:
        print("False")