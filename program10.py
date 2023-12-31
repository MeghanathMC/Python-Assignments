# Write a program to display all prime numbers within a range

def isprime(max):
  if max<=1:
    return False
  for i in range(2,int(max**0.5)+1 ):
    if max%i==0:
      return False
  return True


max=int(input("enter the maxrange : "))
for x in range(2,max+1):
  if(isprime(x)):
    print(x)
