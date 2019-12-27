import random
import math 
from random import randrange

def reverse_element(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return x

def random_number_generator(k):
	array = "1234567890"
	number = 0
	sequence = ""
	for i in range(0, 39):
		a = str(random.choice(array))
		sequence += str(a)
	number = int(sequence)
	if number % 2 == 0 or number <= 2:
		return random_number_generator(100)
	elif len(str(number)) == 38:
		return random_number_generator(100)
	else:
		t = number - 1
		s = 0
		while t % 2 != 0:
			t /= 2
			s += 1
		for i in range(0, k):
			a = randrange(2, number - 2)
			x = pow(a, int(t), number)
			if x == 1 or x == number - 1:
				continue
			for j in range(1, s - 1):
				x = (x ** 2) % number
				if x == 1:
					return random_number_generator(100)
				elif x == number - 1:
					break
			if x != number - 1:
				return random_number_generator(100)
	return(number)

def algorythm():
	p = random_number_generator(100)
	q = random_number_generator(100)
	p1 = random_number_generator(100)
	q1 = random_number_generator(100)
	if p * q <= p1 * q1:
		print("p of the first user: " + str(p))
		print("q of the first user: " + str(q))
		print("----------------------------------------------")
		print("p of the second user: " + str(p1))
		print("q of the second user: " + str(q1))
		print("----------------------------------------------")
	else:
		return algorythm()
	f = (p - 1) * (q - 1)
	f1 = (p1 - 1) * (q1 - 1)
	print("Oiler function for the first user is: " + str(f))
	print("Oiler function for the second user is: " + str(f1))
	print("----------------------------------------------")
	for i in range(0, f):
		e = randrange(2, f - 1)
		if math.gcd(e, f) == 1:
			print("The pair of open keys for the first user: " + str(p * q) + ", " + str(e))
			break
		else:
			continue
	for i in range(0, f1):
		e1 = randrange(2, f1 - 1)
		if math.gcd(e1, f1) == 1:
			print("The pair of open keys for the second user: " + str(p1 * q1) + ", " + str(e1))
			break
		else:
			continue
	print("----------------------------------------------")
	d = reverse_element(e, f)
	d1 = reverse_element(e1, f1)
	if d < 0:
		d = d * (-1)
	if d1 < 0:
		d1 = d1 * (-1)
	print("The secret key for the first user: " + str(d))
	print("The secret key for the second user: " + str(d1))
	print("----------------------------------------------")
	M = randrange(0, p * q - 1)
	M1 = randrange(0, p1 * q1 - 1)
	print("Open message for the first user: " + str(M))
	print("Open message for the second user: " + str(M1))
	print("----------------------------------------------")
	C = pow(M, e1, p1 * q1)
	C1 = pow(M1, e, p * q)
	print("Ciphered message for the first user: " + str(C))
	print("Ciphered message for the second user: " + str(C1))
	print("----------------------------------------------")
	m = pow(C1, d, p * q)
	m1 = pow(C, d1, p1 * q1)
	if m == M1 and m1 == M:
		print("Deciphered message for the first user: " + str(m))
		print("Deciphered message for the second user: " + str(M))
		print("----------------------------------------------")
	else:
		return "Nope"
	S = pow(M, d, p * q)
	print("Signature for the first user: " + str(S))
	R = pow(S, e, p * q)
	if M == R:
		print("The signature was checked successfully!")
	S1 = pow(M1, d1, p1 * q1)
	print("Signature for the second user: " + str(S1))
	R1 = pow(S1, e1, p1 * q1)
	if M1 == R1:
		print("The signature was checked successfully!")


print(algorythm())



