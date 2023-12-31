"""  Write a Python program to check the validity of passwords input by users.
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters. """


import re


def check_password(password):
  length=len(password)
  if(length>=6 and length<=16 and
     re.search("[A-Z]",password) and
     re.search("[a-z]",password) and
     re.search("[0-9]",password) and
     re.search("[$#@]",password)):
     return True
  else:
    return False

password=input("enter your password")
if check_password(password):
  print("valid password!!")
else:
  print("not valid password!!")