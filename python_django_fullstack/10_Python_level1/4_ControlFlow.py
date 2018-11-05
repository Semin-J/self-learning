#Range generator
#range(10)-> range(0, 10, 1) 0 and 1 are default. Start from 0 to 10, leap by 1
#range(0, 100, 2) -> Even number generator till 100
#can use it for loop
#for i in range(10)

#List comprehension(for loop)

x = [1,2,3,4]
out = []
for num in x:
  out.append(num**2)
print(out)

# These are same

y = [1,2,3,4]
out2 = [num**2 for num in y]
print(out2)
  
