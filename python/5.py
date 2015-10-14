#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def isDivisible(num):
	for n in range(1,20):
		if num % n != 0:
			return False
	return num

number = 0
result = False
while result == False:
	number += 1
	good = isDivisible(number)
	if good != False:
		result = good


print result