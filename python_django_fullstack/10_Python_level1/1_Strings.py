#Newly learned things (Compared to the already known)

s = "Hello World"
print(s[::2]) # '::' jump! ::1 is default
#Index rotates in slicing! [-1]-> very last inex
#[:-1] -> All elements but the very last one

#.split(), delimiter default is space. delimiter isn't shown. Shown as a list. Case sensitive.
print(s.split('W'))

#string.format()-> don't need to know the type of the variable
print("This is a {p}".format(p="hi"))

#c style formatting-> need to know the type
print("This is a %d"%(10))
