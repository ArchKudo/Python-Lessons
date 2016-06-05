import re

'''
Checks phone nos. having following pattern:
• 800-555-1212
• 800 555 1212
• 800.555.1212
• (800) 555-1212
• 1-800-555-1212
• 800-555-1212-1234
• 800-555-1212x1234
• 800-555-1212 ext. 1234
• work 1-(800) 555.1212 #1234

print(re.search(phonePattern, '800-555-1212').groups())
print(re.search(phonePattern, '800 555 1212').groups())
print(re.search(phonePattern, '800.555.1212').groups())
print(re.search(phonePattern, '(800) 555-1212').groups())
print(re.search(phonePattern, '1-800-555-1212').groups())
print(re.search(phonePattern, '800-555-1212-1234').groups())
print(re.search(phonePattern, '800-555-1212x1234').groups())
print(re.search(phonePattern, '800-555-1212 ext. 1234').groups())
print(re.search(phonePattern, 'work 1-(800) 555.1212 #1234').groups())

'''
# \d{N} - Match any N numeric digits
# \d+ - Match one or more numeric digits
# \d* - Match zero or more numeric digits
# \D - Match any character which is non-numeric
# \D+ - Match one or more non-numeric character
# \D* - Match zero or more non-numeric characters


phonePattern = r'^(\d{3})-(\d{3})-(\d{4})$'
print(re.search(phonePattern, '800-555-1212').groups())
# print(re.search(phonePattern, '800 555 1212').groups())
# print(re.search(phonePattern, '800.555.1212').groups())
# print(re.search(phonePattern, '(800) 555-1212').groups())
# print(re.search(phonePattern, '1-800-555-1212').groups())
# print(re.search(phonePattern, '800-555-1212-1234').groups())
# print(re.search(phonePattern, '800-555-1212x1234').groups())
# print(re.search(phonePattern, '800-555-1212 ext. 1234').groups())
# print(re.search(phonePattern, 'work 1-(800) 555.1212 #1234').groups())
print('-----------------------------')
# OR compile phonePattern as pattern object
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
print(re.search(phonePattern, '800-555-1212').groups())
print('-----------------------------')
# ONLY WORKS ON FIRST PATTERN
# print(re.search(phonePattern, '800 555 1212').groups())
# print(re.search(phonePattern, '800.555.1212').groups())
# print(re.search(phonePattern, '(800) 555-1212').groups())
# print(re.search(phonePattern, '1-800-555-1212').groups())
# print(re.search(phonePattern, '800-555-1212-1234').groups())
# print(re.search(phonePattern, '800-555-1212x1234').groups())
# print(re.search(phonePattern, '800-555-1212 ext. 1234').groups())
# print(re.search(phonePattern, 'work 1-(800) 555.1212 #1234').groups())
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
# print(re.search(phonePattern, '800-555-1212').groups())
# print(re.search(phonePattern, '800 555 1212').groups())
# print(re.search(phonePattern, '800.555.1212').groups())
# print(re.search(phonePattern, '(800) 555-1212').groups())
# print(re.search(phonePattern, '1-800-555-1212').groups())
print(re.search(phonePattern, '800-555-1212-1234').groups())
# print(re.search(phonePattern, '800-555-1212x1234').groups())
# print(re.search(phonePattern, '800-555-1212 ext. 1234').groups())
# print(re.search(phonePattern, 'work 1-(800) 555.1212 #1234').groups())
print('-----------------------------')
phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D+(\d+)$')
# print(re.search(phonePattern, '800-555-1212').groups())
# print(re.search(phonePattern, '800 555 1212').groups())
# print(re.search(phonePattern, '800.555.1212').groups())
# print(re.search(phonePattern, '(800) 555-1212').groups())
# print(re.search(phonePattern, '1-800-555-1212').groups())
print(re.search(phonePattern, '800-555-1212-1234').groups())
print(re.search(phonePattern, '800-555-1212x1234').groups())
# print(re.search(phonePattern, '800-555-1212 ext. 1234').groups())
# print(re.search(phonePattern, 'work 1-(800) 555.1212 #1234').groups())
print('-----------------------------')
phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(re.search(phonePattern, '800-555-1212').groups())
print(re.search(phonePattern, '800 555 1212').groups())
print(re.search(phonePattern, '800.555.1212').groups())
# print(re.search(phonePattern, '(800) 555-1212').groups())
# print(re.search(phonePattern, '1-800-555-1212').groups())
print(re.search(phonePattern, '800-555-1212-1234').groups())
print(re.search(phonePattern, '800-555-1212x1234').groups())
print(re.search(phonePattern, '800-555-1212 ext. 1234').groups())
# print(re.search(phonePattern, 'work 1-(800) 555.1212 #1234').groups())
print('-----------------------------')
phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)')
print(re.search(phonePattern, '800-555-1212').groups())
print(re.search(phonePattern, '800 555 1212').groups())
print(re.search(phonePattern, '800.555.1212').groups())
print(re.search(phonePattern, '(800) 555-1212').groups())
# print(re.search(phonePattern, '1-800-555-1212').groups())
print(re.search(phonePattern, '800-555-1212-1234').groups())
print(re.search(phonePattern, '800-555-1212x1234').groups())
print(re.search(phonePattern, '800-555-1212 ext. 1234').groups())
# print(re.search(phonePattern, 'work 1-(800) 555.1212 #1234').groups())
print('-----------------------------')
# DOES NOT CHECK FOR BEGINING
phonePattern = phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)')
print(re.search(phonePattern, '800-555-1212').groups())
print(re.search(phonePattern, '800 555 1212').groups())
print(re.search(phonePattern, '800.555.1212').groups())
print(re.search(phonePattern, '(800) 555-1212').groups())
print(re.search(phonePattern, '1-800-555-1212').groups())
print(re.search(phonePattern, '800-555-1212-1234').groups())
print(re.search(phonePattern, '800-555-1212x1234').groups())
print(re.search(phonePattern, '800-555-1212 ext. 1234').groups())
print(re.search(phonePattern, 'work 1-(800) 555.1212 #1234').groups())
print('-----------------------------')
# Verbose
phonePattern = re.compile(
'''
				# Do not start matching at beginning, Pattern can start anywhere
(\d{3}) # Area Code 3-Digits long
\D*			# Seperator
(\d{3}) # Trunk Code 3-Digits long
\D*			# Seperator
(\d{4}) # Rest Number 4-Digits long
\D*			# Seperator
(\d*)   # Extension Code
$
'''
, re.VERBOSE)
print(re.search(phonePattern, '800-555-1212').groups())
print(re.search(phonePattern, '800 555 1212').groups())
print(re.search(phonePattern, '800.555.1212').groups())
print(re.search(phonePattern, '(800) 555-1212').groups())
print(re.search(phonePattern, '1-800-555-1212').groups())
print(re.search(phonePattern, '800-555-1212-1234').groups())
print(re.search(phonePattern, '800-555-1212x1234').groups())
print(re.search(phonePattern, '800-555-1212 ext. 1234').groups())
print(re.search(phonePattern, 'work 1-(800) 555.1212 #1234').groups())
print('-----------------------------')
