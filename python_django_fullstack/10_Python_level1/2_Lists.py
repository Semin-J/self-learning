# Print List shows [ , , ,]
# + (concatenation), temporary
#.append() add item to end of the list
hi = [1, 2, 3, "hi"]
hi.append("hooo") #only One Argument
print(hi)

#.pop() remove very last index as a default. (3)->remove [3]rd element
go= hi.pop(3)
print(hi)
# hi[10], index out of range


li = ['a', 'e', 'b', 'g']
#can use li[::-1] for temporary reverse
print(li[::-1]) #['g', 'b', 'e', 'a']
print(li) #['a', 'e', 'b', 'g']
#.reverse() and .sort() is permanent.
#should be done before print. Inside of print(), isn't working
li.reverse()
li.sort() 
print(li)

## List Comprehension ##
# "for" loop, flattened out into a list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_column = [row[0] for row in matrix]
print(first_column) #[1, 4, 7]




