"""Write a program to print the following number pattern using a loop.
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 """
n=int(input("enter the value of n:"))
for x in range(n):
  for i in range(x+1):
    print(i+1,end=" ")
  print()
    