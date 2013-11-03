from random import randint

def hailstone(n):
	while n != 1:
		print(n)
		if n % 2 == 0:
			n = n / 2
		else:
			n = n * 3 + 1
	print(n)
	return "done"

def rec_h(n):
	if n == 1:
		print(n)
		return "done"
	else:
		print(n)
		if n % 2 == 0:
			return rec_h(n / 2)
		else:
			return rec_h(n * 3 + 1)

def extra_end(str):
	if len(str) >= 2:
		return str[len(str) - 2: len(str)] * 3

def tell_me(phrase):
	if "please" in phrase and "tell me" not in phrase:
		return "No."
	elif phrase != "tell me please":
		return "You must learn to say 'Please'"
	else:
		return randint(0, 1000)

def equals(lst1, lst2):
	return lst1 == lst2
