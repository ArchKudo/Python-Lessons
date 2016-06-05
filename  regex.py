import re
'''
REGEX MATCHING:

• ^ matches the beginning of a string.
• $ matches the end of a string.
• \b matches a word boundary.
• \d matches any numeric digit.
• \D matches any non-numeric character.
• x? matches an optional x character (in other words, it matches an x zero or one times).
• x* matches x zero or more times.
• x+ matches x one or more times.
• x{n,m} matches an x character at least n times, but not more than m times.
• (a|b|c) matches exactly one of a , b or c .
• (x) in general is a remembered group. You can get the value of what matched by using the groups() method
of the object returned by re.search .

'''
s = '100 NORTH MAIN ROAD'
print(s.replace('ROAD', 'RD.')) # Replace using methods
print(s[:-4] + s[-4:].replace('ROAD', 'RD.'))
print(re.sub('ROAD$', 'RD.', s)) # Replacing using regex module

s = '100 NORTH BROAD ROAD'
print(s.replace('ROAD', 'RD.')) # Replacing using method doesn't work here
print(s[:-4] + s[-4:].replace('ROAD', 'RD.')) # Gets COmplex
print(re.sub('ROAD$', 'RD.', s)) # $ is used to denote ROAD present at end of string

s = '100 BROAD'
print(re.sub('ROAD$', 'RD.', s))
print(re.sub('\\bROAD', 'RD.', s)) # \b sets word boundary
print(re.sub(r'\bROAD', 'RD.', s)) # r prefix makes it a raw string, no more need to escape characters

s = '100 BROAD ROAD APT. 3'
print(re.sub(r'\bROAD\b', 'RD.', s)) #Word boundaries at both end


