# Print the number of zeroes encountered between 0 and 1000.
zero_count = 0
for number in range(1001):
	zero_count += str(number).count("0")
print(zero_count)
 