import re

nums = []
hand = open('actual_data.txt')
for line in hand:
	line = line.rstrip()
	numbers = re.findall('[0-9]+', line)
	if len(numbers) == 1:
		nums.append(int(numbers[0]))
	if len(numbers) == 2:
		nums.append(int(numbers[0]))
		nums.append(int(numbers[1]))
	if len(numbers) == 3:
		nums.append(int(numbers[0]))
		nums.append(int(numbers[1]))
		nums.append(int(numbers[2]))

print(sum(nums))
