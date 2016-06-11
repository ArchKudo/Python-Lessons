import re
# [abc]$ - Either one of a, b, c at end
# [^abc] - (^ - Negation) Neither one of a, b, c

# Using Conditionals
def plural(noun):
	if re.search('[sxz]$', noun):
		return re.sub('$', 'es', noun)
	elif re.search('[^aeioudgkprt]h$', noun):
		return re.sub('$', 'es', noun)
	elif re.search('[^aeiou]y$', noun):
		return re.sub('y$', 'ies', noun)
	else:
		return noun + 's'

print(plural('fish'))

# # Using functions
def match_sxz(noun):
	return re.search('[sxz]$', noun)
def apply_sxz(noun):
	return re.sub('$', 'es', noun)
def match_h(noun):
	return re.search('[^aeioudgkprt]h$', noun)
def apply_h(noun):
	return re.sub('$', 'es', noun)
def match_y(noun):
	return re.search('[^aeiou]y$', noun)
def apply_y(noun):
	return re.sub('y$', 'ies', noun)
def match_default(noun):
	return True
def apply_default(noun):
	return noun + 's'

rules = ((match_sxz, apply_sxz),
         (match_h, apply_h),
         (match_y, apply_y),
         (match_default, apply_default))

def plural(noun):
	for match_rule, apply_rule in rules:
		if match_rule(noun):
			return apply_rule(noun)

print(plural('fish'))

# Using Closures
def build_match_apply_functions(pattern, search, replace):
	def match_rule(noun):
		return re.search(pattern, noun)
	def apply_rule(noun):
		return re.sub(search, replace, noun)
	return (match_rule, apply_rule)

patterns = (
           ('[sxz]$', '$', 'es'),
           ('[^aeioudgkprt]h$', '$', 'es'),
           ('qu|[^aeiou]y$', 'y$', 'ies'),
           ('$', '$', 's'),
          )


rules = [build_match_apply_functions(pattern, search, replace)
					for (pattern, search, replace) in patterns]

def plural(noun):
	for match_rule, apply_rule in rules:
		if match_rule(noun):
			return apply_rule(noun)

print(plural('fish'))

# Using Files

rules = []
with open('plural-rules', encoding='utf-8') as pattern_file:
	for line in pattern_file:
		pattern, search, replace = line.split(None, 3)
		rules.append(build_match_apply_functions(pattern, search, replace))

print(plural('fish'))

def rules(rule_filename):
	with open(rule_filename, encoding='utf-8') as pattern_file:
		for line in pattern_file:
			pattern, search, replace = line.split(None, 3)
			yield build_match_apply_functions(pattern, search, replace)

def plural(noun, rule_filename='plural-rules'):
	for match_rule, apply_rule in rules(rule_filename):
		if match_rule(noun):
			return apply_rule(noun)
	raise ValueError('No matching rule for {0}'.format(noun))

print(plural('fish'))
