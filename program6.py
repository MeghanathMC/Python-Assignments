"""Write a program to print multiplication table of a given number
"""






def multi(num):
  for x in range(1,11):
    print(f"{num}*{x} = {num*x}")

num=int(input("enter a number : "))
print(multi(num))