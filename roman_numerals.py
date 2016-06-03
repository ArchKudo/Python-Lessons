import re

# ^ - Marks beginning of regex pattern
# $ - Marks end of regex pattern
# ? - Makes preceding token optional
# a | b - Match either a, b
# C{a,b} - Match a to b cc of C
# (a|b) - Applies alternation only to the group defined inside ()

pattern = '^M?M?M?$'
print(re.search(pattern, 'M'))
print(re.search(pattern, 'MM'))
print(re.search(pattern, 'MMM'))
print(re.search(pattern, ''))
print(re.search(pattern, 'MMMM'))

pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
print(re.search(pattern, 'MCM'))
print(re.search(pattern, 'MD'))
print(re.search(pattern, 'MMMCCC'))
print(re.search(pattern, 'MCMC')) #No pattern found
print(re.search(pattern, ''))

# Alternate pattern
pattern = '^M{0,3}$'
print(re.search(pattern, 'M'))
print(re.search(pattern, 'MM'))
print(re.search(pattern, 'MMM'))
print(re.search(pattern, ''))

pattern = '^M{0,3}(CM|CD|D?C{0,3})$'
print(re.search(pattern, 'MCM'))
print(re.search(pattern, 'MD'))
print(re.search(pattern, 'MMMCCC'))
print(re.search(pattern, 'MCMC')) #No pattern found
print(re.search(pattern, ''))

pattern = '^M?M?M?(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
print(re.search(pattern, 'IX'))
print(re.search(pattern, 'MCIX'))

# Verbose regex
pattern = '''

^									# Beginning of string
M{0,3}						# Thousands -	(M) - Occurences 0 - 3

(CM|CD|D?C{0,3})	# Hundreds - 	900 (CM), 400 (CD), 0 - 300 (0 - 3 C)
									#							500 - 800 (D, followed by 0 - 3 C)

(XC|XL|L?X{0,3})	# Tens - 			90 (XC), 40(XL),
									#							50 - 80 (L, followed by 0 - 3 X)

(IX|IV|V?I{0,3})	# Ones - 			9 (IX), 4(IV),
									#							5 - 8 (V, followed by 0 - 3 I)

$									# End of string

'''

print(re.search(pattern, 'M', re.VERBOSE))
print(re.search(pattern, 'MCMLXXXIX', re.VERBOSE))
print(re.search(pattern, 'MMMCLXIII', re.VERBOSE))

