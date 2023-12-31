"""Write a Python program to get the Fibonacci series between 0 and 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34 """

def fibonocci(max):
  fib_series=[]
  a,b=0,1
  while a<=max:
    fib_series.append(a)
    a,b=b,a+b

  return fib_series

max=50
result=[]
result=fibonocci(max)
print("fibonoci series generated till 50 :",result)
