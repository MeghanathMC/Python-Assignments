# Print the following pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

for x in range(5,0,-1):
  for i in range(x,0,-1):
    print(i,end=" ")
  print()
