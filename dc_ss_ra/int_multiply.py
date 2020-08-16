import math

def zero_pad(numStr, zeros):
	for i in range(zeros):
		numStr = str(numStr) + '0'

	return numStr

def int_multiply(x, y):
	n = len(str(x))
	print(x,y)
	if n == 1:
		return int(x) * int(y)

	else:

		m = int(n/2) 
		a = str(x)[0:m]
		b = str(x)[m:]
		c = str(y)[0:m]
		d = str(y)[m:]
		ac = int_multiply(a, c)
		bd = int_multiply(b, d)
		ad = int_multiply(a, d)
		bc = int_multiply(b, c)
		A = int(zero_pad(ac, n))
		B = int(zero_pad(ad + bc, m))
		product = A + B + bd 
		return product


if __name__ == '__main__':
	x =3141592653589793238462643383279502884197169399375105820974944592
	y =2718281828459045235360287471352662497757247093699959574966967627
	#x = 31237587578
	#y = 27188757857
	res = int_multiply(x, y)
	print(res)
