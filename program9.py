# Print list in reverse order using a loop
lst=[1,2,3,4,5,6,7]
n=len(lst)
for x in range(n-1,-1,-1):
  print(lst[x],end=" ")