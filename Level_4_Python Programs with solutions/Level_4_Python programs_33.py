count = 0
for n in range(1000, 10000):
  s = str(n)
  if s[0] <= s[1] <= s[2] <= s[3]:
    count += 1

print("Total non-decreasing numbers from 1000 to 9999:", count)