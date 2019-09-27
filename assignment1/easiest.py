def digitsum(num):
	# gets sum of digits of num
	sum=0
	while num != 0:
		sum += num%10
		num=int(num/10)
	return sum

while True:
	num = int(input())
	if num == 0:
		break

	target = digitsum(num)
	# answer is bounded from below by 11 and bounded above by 100
	# hence iterate in this range
	for factor in range(11, 101):
		product = factor*num
		if digitsum(product) == target:
			print(factor)
			break