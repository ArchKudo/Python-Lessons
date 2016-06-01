import fractions
#Data type bool True = 1, False = 0
a = True
#Data type int
b = 2*a
print(b)
#True+True(bool) = 2(int) bools get coerced to ints
if b != 2:
	raise ValueError("True Not 1.")
#isinstance checks whether a given object is of given type
print(isinstance(a, bool))
print(isinstance(b, bool))
#type returns the data type of an object
print(type(a)) #bool
print(type(b)) #int
#coercion
c = 1
print(isinstance(c, int))
c = 1 + 1.0
print(isinstance(c, float))
print(isinstance(c, int))
#explicitly convert a number
a = float()
print(isinstance(a, float))

#Numbers as bools
#0 is false all others are true
def is_it_true(x):
	if x:
		print("Yes, true")
	else:
		print("No, not True")

is_it_true(1)
is_it_true(-1)
is_it_true(0)
is_it_true(-0)
is_it_true(fractions.Fraction(1, 3))

#Lists
a_list = ['a', 'b', 'c', 'd', 'e']
print(a_list)
#Accesing single elements
#First Element
print(a_list[0])
#Last Element
print(a_list[-1])
print(type(a_list[-1]))
#Previous to Last Element
print(a_list[-2])
#a_list[-n] == a_list[len(a_list) - n]
print(a_list[len(a_list) - 1])
print(a_list[-1])
if a_list[-1] == a_list[len(a_list) - 1]:
	print("a_list[-n] == a_list[len(a_list) - n]")

#slicing a list

print(a_list[0:3]) #Prints 0(inclusive) to 3rd element exclusive {x = [a, b)}
print(a_list[0:-1])
print(a_list[:]) #Prints complete list
if a_list[0:2] == a_list[:2]:
	print("a_list[0:n] == a_list[:n]")

#Adding to a list
a_list += [2, 100, 13, True] #Not necessarily of same data type
print(a_list)
a_list.append(False)
print(a_list)
a_list.extend(['ə', '°', 'ə', 'ə'])
print(a_list)

#searching for values in a list
print(a_list.count('ə'))
print('°' in a_list)
print(a_list.index(True))

#removing items from a list
del a_list[0] #using index
print(a_list)

a_list.remove('ə') #Removes first instance, and not all
print(a_list)

a_list.pop() #Remove the last element
print(a_list)
a_list.pop()
print(a_list)

a_list.pop(0) #Remove first element
print(a_list)

a_list.pop(3)
print(a_list)

print(a_list.pop(5)) #Removes 5th element and returns that value
print(a_list)

"""
1. In a boolean context, an empty list is false.
2. Any list with at least one item is true.
3. Any list with at least one item is true. The value of the items is irrelevant.
"""

#Tuples
a_tuple = (1, 2, 3, 4, 5) ##Cannot be modified
print(a_tuple[1:3]) #slicing is allowed since it creates new lists

# print(a_tuple.pop()) Does not work Nor does any other

#Finding
print(2 in a_tuple)
print(a_tuple.index(2))

# a_tuple = list()
# a_tuple.append(12) #Destroys the tuple
# print(a_tuple)

s_tuple = (False , ) #the comma is important
print(s_tuple[0])

#Assigning multiple values at once
v = ('a', 'b', 'c')
(x, y, z) = v
print(x, y, z)
(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) = range(7)
print(Monday)

#sets
a_set = {1, 2, 3}
b_set = {3, 4, 5}
print(type(a_set), type(b_set))
print(type({})) #Empty Dict not Set
a_set.update(b_set) #Add values to set
print(a_set)
a_set.discard(4) #Discard a value
print(a_set)
# a_set.remove(4) #Remove gives error on missing element discard doesn't
a_set.pop() #Undordered hence any element gets removed
print(a_set)
a_set.pop()
print(a_set)
print(a_set.intersection(b_set), '\n', a_set.union(b_set), '\n', a_set.symmetric_difference(b_set))

#dictionaries

a_dict = {'name': 'girish', 'age': 20}
print(a_dict['name'])
print(a_dict)
a_dict['gender'] = 'male'
a_dict['age'] = '21'
print(a_dict)

SUFFIXES = {1000: [ 'iB, KiB, GiB, TiB, Pi'],
						1024: ['B, Mi']}
print(len(SUFFIXES))
print(1000 in SUFFIXES)
print(SUFFIXES[1000][0])
