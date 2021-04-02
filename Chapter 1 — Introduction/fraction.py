# Fraction implementation

# calculate GCD
def gcd(x, y):
	while x % y != 0:
		x, y = y, x % y
	return y

class Fraction:
	def __init__(self, top, bottom):
		if top < 0:
			raise RuntimeError('Numerator must be non negative')
		elif bottom < 0:
			raise RuntimeError('Denominator must be non negative')
		else:
			common = gcd(top, bottom)
			self.num = top // common
			self.den = bottom // common

	def show(self):
		print(f'{self.num}/{self.den}')

	def __str__(self):
		return f'{self.num}/{self.den}'

	def __add__(self, other):
		new_numerator = self.num * other.den + self.den * other.num
		new_denominator = self.den * other.den
		return Fraction(new_numerator, new_denominator)
		
	__radd__ = __add__

	def __sub__(self, other):
		new_numerator = self.num * other.den - self.den * other.num
		new_denominator = self.den * other.den
		return Fraction(new_numerator, new_denominator)

	def __mul__(self, other):
		new_numerator = self.num * other.num
		new_denominator = self.den * other.den
		return Fraction(new_numerator, new_denominator)

	def __truediv__(self, other):
		new_numerator = self.num * other.den
		new_denominator = self.den * other.num
		return Fraction(new_numerator, new_denominator)

	# check ==
	def __eq__(self, other):
		first = self.num * other.den
		second = self.den * other.num
		return first == second

	# check <
	def __lt__(self, other):
		first = self.num * other.den
		second = self.den * other.num
		return first < second

	# check >
	def __gt__(self, other):
		first = self.num * other.den
		second = self.den * other.num
		return first > second

	def get_num(self):
		return self.num

	def get_den(self):
		return self.den

my_fraction = Fraction(1, 4)
my_fraction.show() # 1/4
print(my_fraction) # 1/4
other_fraction = Fraction(1, 2)
print(my_fraction + other_fraction) # 3/4
print(other_fraction - my_fraction) # 1/4
print(my_fraction * other_fraction) # 1/8
print(my_fraction / other_fraction) # 1/2
print(my_fraction == other_fraction) # False
print(my_fraction < other_fraction) # True
print(my_fraction > other_fraction) # False
