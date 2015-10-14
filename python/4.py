#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99

#Find the largest palindrome made from the product of two 3-digit numbers.

result = 0

for n1 in range(0,999):
	for n2 in range(0,999):
		string = str(n1 * n2)
		if string[::-1] == string: #Check if the reverse is the same
			if result < int(string):
				result = int(string)

print result