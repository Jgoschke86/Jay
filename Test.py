nums = []
total = 0
for i in range(0, 1001):
    if i % 3 == 0 or i % 5 == 0:
        nums.append(i)
    else:
        pass
print(nums)
for num in nums:
    total += num
print(total)