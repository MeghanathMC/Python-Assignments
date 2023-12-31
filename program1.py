"""
Write a Python program to construct the following pattern, using a nested for loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
* 
"""
#function
def pattern(n):
  for i in range(n):
    for j in range(i+1):
      print("*", end=" ")
    print()
  j=n-1
  while j>0:
    for i in range(j):
      print("*",end=" ")
    print()
    j=j-1


n=int(input("enter no.of rows: "))
pattern(n)












