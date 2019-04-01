nums = [int(a) for a in raw_input()]
count = 0
while True:
    swaps = False
    for i in range(len(nums)):
        if i < len(nums)-1:
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swaps = True
                count += 1

    if not swaps:
        break

print count
