import re
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


