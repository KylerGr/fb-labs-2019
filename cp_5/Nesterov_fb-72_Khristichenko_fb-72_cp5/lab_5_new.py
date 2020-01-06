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
	array = "01"
	number_line = ""
	global number
	number = 0
	for i in range(0, 256):
		a = str(random.choice(array))
		number_line += a
	number = int(number_line)
	simple = 0
	j = 255
	i = 0
	while j != -1 and i != len(number_line):
		simple += int(number_line[j]) * (2 ** i)
		j -= 1
		i += 1
		if j == -1 or i == len(number_line):
			break
	if simple % 2 == 0 or simple <= 2:
		return random_number_generator(100)
	else:
		t = simple - 1
		s = 0
		while t % 2 != 0:
			t /= 2
			s += 1
		for i in range(0, k):
			a = randrange(2, simple - 2)
			x = pow(a, int(t), simple)
			if x == 1 or x == simple - 1:
				continue
			for j in range(1, s - 1):
				x = (x ** 2) % simple
				if x == 1:
					return random_number_generator(100)
				elif x == simple - 1:
					break
			if x != simple - 1:
				return random_number_generator(100)
	return(simple)

def generate_():
	global p
	p = random_number_generator(100)
	return p

def generate_one():
	global q
	q = random_number_generator(100)
	return q

def generate__():
	global p1
	p1 = random_number_generator(100)
	return p1

def generate_two():
	global q1
	q1 = random_number_generator(100)
	return q1

def open_key_one():
	global p
	global q
	f = (p - 1) * (q - 1)
	global e
	for i in range(0, f):
		e = randrange(2, f - 1)
		if math.gcd(e, f) == 1:
			break
		else:
			continue
	return e

def open_key_two():
	global p1
	global q1
	f1 = (p1 - 1) * (q1 - 1)
	global e1
	for i in range(0, f1):
		e1 = randrange(2, f1 - 1)
		if math.gcd(e1, f1) == 1:
			break
		else:
			continue
	return e1

def secret_key_one():
	global p
	global q
	global e
	global d
	d = reverse_element(e, (p - 1) * (q - 1))
	if d < 0:
		d = d * (-1)
	return d

def secret_key_two():
	global p1
	global q1
	global e1
	global d1
	d1 = reverse_element(e1, (p1 - 1) * (q1 - 1))
	if d1 < 0:
		d1 = d1 * (-1)
	return d1

def message_one():
	global M
	M = randrange(0, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
	return M

def message_two():
	global M1
	M1 = randrange(0, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
	return M1

def cipher_message_one():
	global p1
	global q1
	global M
	global e1
	global C
	C = pow(M, e1, int(p1 * q1))
	return C

def cipher_message_two():
	global p
	global q
	global M1
	global e
	global C1
	C1 = pow(M1, e, int(p * q))
	return C1


def decipher_message_one():
	global p
	global q
	global C1
	global d
	m = pow(C1, d, int(p * q))
	return m

def decipher_message_two():
	global p1
	global q1
	global C
	global d1
	m1 = pow(C, d1, int(p1 * q1))
	return m1

def signature_one():
	global p
	global q
	global S
	global M
	global d
	S = pow(M, d, int(p * q))
	return S

def signature_two():
	global p1
	global q1
	global S1
	global M1
	global d1
	S1 = pow(M1, d1, int(p1 * q1))
	return S1

def check_signature_one():
	global p
	global q
	global S
	global e
	global R 
	global M
	R = pow(S, e, int(p * q))
	if R == M:
		return "Successfully checked for the first user!"

def check_signature_two():
	global p1
	global q1
	global S1
	global e1
	global R1
	global M1
	R1 = pow(S1, e1, int(p1 * q1))
	if R1 == M1:
		return "Successfully checked for the second user!"

def first_key_to_send():
	global p1
	global q1
	global p
	global q
	global e1
	global d
	global k
	global s
	global k1
	global s1 
	k = randrange(0, p * q)
	k1 = pow(k, e1, p1 * q1)
	s = pow(k, d, p * q)
	s1 = pow(s, e1, p1 * q1)
	print("Here is the secret: " + str(k))
	print("Here is k1 value: " + str(k1))
	print("Here is s value: " + str(s))
	print("Here is s1 value: " + str(s1))
	return "Well done!"

def receive_key():
	global p1
	global q1
	global p
	global q
	global d1
	global e
	global k1
	global s1 
	k = pow(k1, d1, p1 * q1)
	s = pow(s1, d1, p1 * q1)
	c = pow(s, e, p * q)
	print("Here is the deciphered secret: " + str(k))
	print("Here is s value: " + str(s))
	print("Authentication checked: " + str(c))
	return "Well done!"


def main():
	print("0. Generate the simple numbers for the users!")
	print("1. Create the open keys for users!")
	print("2. Create the secret keys for users!")
	print("3. Generate the messages for the users!")
	print("4. Cipher the created messages!")
	print("5. Decipher the created messages!")
	print("6. Create the signatures!")
	print("7. Check the signatures!")
	print("8. Send the key!!")
	print("9. Exit!")
	s = input("Select an option: ")
	if s == "0":
		print("The p value for the first user is: " + str(generate_()))
		print("The q value for the first user is: " + str(generate_one()))
		print("----------------------------------------------")
		print("The p value for the second user is: " + str(generate__()))
		print("The q value for the second user is: " + str(generate_two()))
		if generate_() * generate_one() >= generate__() * generate_two():
			print("Please, generate another pair!")
			return main()
		return main()
	elif s == "1":
		print("Open key for the first user: " + str(open_key_one()))
		print("Open key for the second user: " + str(open_key_two()))
		return main()
	elif s == "2":
		print("Secret key for the first user: " + str(secret_key_one()))
		print("Secret key for the second user: " + str(secret_key_two()))
		return main()
	elif s == "3":
		print("Message for the first user: " + str(message_one()))
		print("Message for the second user: " + str(message_two()))
		return main()
	elif s == "4":
		print("Ciphered message for the first user: " + str(cipher_message_one()))
		print("Ciphered message for the second user: " + str(cipher_message_two()))
		return main()
	elif s == "5":
		print("Deciphered message for the first user is: " + str(decipher_message_two()))
		print("Deciphered message for the second user is: " + str(decipher_message_one()))
		return main()
	elif s == "6":
		print("Signature for the first user: " + str(signature_one()))
		print("Signature for the second user: " + str(signature_two()))
		return main()
	elif s == "7":
		print(check_signature_one())
		print(check_signature_two())
		return main()
	elif s == "8":
		print("Here goes the key to send :)")
		print(first_key_to_send())
		l = input("To check everything, type 1: ")
		if l == "1":
			print(receive_key())
			return main()
		else:
			print("Wrong input!")
			return main()

	elif s == "9":
		return "Have a good one!"
	else:
		print("No such option! Please try again!")
		return main()


print(main())
