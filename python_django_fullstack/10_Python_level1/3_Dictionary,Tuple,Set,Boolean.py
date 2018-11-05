"""
Dictionary is Python's version of Hash Tables(Objects back in JS)
-> But don't have methods inside like JS
It allows us to ceate a "mapping" with key-value pairs.
It doesn't retain any order(No orders)
"""
my_stuff = {"key1":"value", "key2":"value2", "key":{"123":[1,2,'grab me']}}
print(my_stuff["key"]['123'][2].upper())

food_dict = {"lunch":"pizza", "bfast":"cereal"}
#add new key and value
food_dict["dinner"] = 'pasta'

#change the value of the key
food_dict["lunch"] = "steak"

print(food_dict)



#Tuple is immutable sequences
#Set is unordered collections of unique elements
#->goot to get rid of redundant elements
#Booleans (True and False)

t = (1,2,3)
#t[0] = 5
print(t[0])

x = set()

x.add(1)
x.add(4)
x.add(3)
x.add(2)
print(x) #{1, 2, 3, 4} No order, not hold same elements, only unique

converted = set([1,1,2,2,3,3,3,3,4,4,4,4])
print(converted) #{1, 2, 3, 4}
