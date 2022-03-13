from os import major


nums = [3,2,3]

candidate, count = nums[0], 0
for num in nums:
    if num == candidate:
        count += 1
    elif count == 0:
        candidate, count = num, 1
    else:
        count -= 1
print(candidate)