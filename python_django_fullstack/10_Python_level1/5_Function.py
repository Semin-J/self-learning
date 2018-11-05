#Name of function in Python : Using ' _ ' e.g) my_funtion
#Name of function in JS : Using camelcase e.g) myFuntion
#function can have default parametre. e.g)def hello(num = 3):
#To check the type -> type()


#Lambda Expresion(Anonymous function)
#->function used only once in quick

#Using full function
#filter(function, sequence of source)
#-> the sequence of source can be list, tuple, set or any container of any iterator
#-> it filters only elements which meet the function's condition 
mylist = [1, 2, 3, 4, 5, 6, 7, 8]

def even_bool(num):
    return num%2 == 0


evens = filter(even_bool, mylist)
print(list(evens)) #have to cast as list()


#Using lambda
evens = filter(lambda num:num%2==0, mylist)
print(list(evens))


# Methods -> built in functions in objects

# for dictionary
d = {'k1':10, 'k2':20}
print(d.keys()) # dict_keys(['k1', 'k2'])
print(d.values()) # dict_values([10, 20])
print(d.items()) # dict_items([('k1', 10), ('k2', 20)])


# 'in' operator
print('x' in [1,2,3]) #returns boolean: False
print('x' in ['x','y','z']) #returns boolean: True
