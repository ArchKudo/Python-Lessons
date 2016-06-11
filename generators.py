def make_counter(x):
	print('Entering make counter')
	while True:
		yield x # Pauses
		print('Incrementing x')
		x += 1

counter = make_counter(2)
print(counter)
print(next(counter)) # Resumes until next yield statment
print(next(counter))
print(next(counter))

def fib(max):
	a, b = 0, 1
	while a < max:
		yield a
		a, b = b, a + b
# Iterators call next internally
for f in fib(100):
	print(f, end=' ')
print()
print(list(fib(1000)))
