import humansize
string = "Arch"
print("{0}".format(string))
string_2 = 'Kudo' # ' ' or " " are allowed for declaring string
print("{0} {1}".format(string, string_2))

suffixes = humansize.SUFFIXES
print(suffixes)
print(suffixes[1000])
print("1000 {0[0]} equals 1 {0[1]}".format(suffixes[1000]))

#splitting lines
string_3 = """Robb is a good boy
							He does all his work on his own
							He is intelligent
							Compassionate
							and a few other good adjectives you
							could think off
					 """
list_1 = string_3.splitlines()
print(list_1)

#tolower
print(string_3)
print(string_3.lower())

#count instances

print(string_3.lower().count('f'))
print(string_3.count('Girish'))

a = '''Finished files are the re-
... sult of years of scientif-
... ic study combined with the
... experience of years.'''

print(a.lower().count('f'))

#Convert string into dict
arr = "ab, dc; cd, ja; kk, as; as, qq"
arr_list = arr.split('; ')
# arr.split('x', 1) -> limits the split to 1
arr_list = [arr.split(', ', 1) for arr in arr_list if ',' in arr]
print(arr_list)
arr_dict = dict(arr_list)
print(arr_dict)

#Slicing a string
string_4 = "This is an example text"
print(string_4)
print(string_4[10:-1])
print(string_4[-5:-3])

#bytes
byte_1 = b'abcd\x65' #b in start determines type byte
print(byte_1)
print(type(byte_1))
print(len(byte_1))
byte_1 += b'xff'
print(byte_1)
print(len(byte_1))
print(byte_1[0]) #accesing byte elements
#Re-assigning doesn't work
# byte_1[0] = 102

#cat two bytestrings
byte_2 = b'fghi'
byte_1 += byte_2
print(byte_1)

print(byte_1.decode().count('f')) # Convert to string to find instances of 'f'


