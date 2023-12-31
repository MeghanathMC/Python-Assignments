"""
Write a Python program to count the number of even and odd numbers in a series of numbers

Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4

"""
def check(numbers):
  even=0
  odd=0
  for num in numbers:
    if num%2==0:
      even+=1
    else:
      odd+=1

  return even,odd




numbers=[1,2,3,4,5]
even,odd=check(numbers)
print("number of even : ",even)
print("numebr of odd :",odd)
