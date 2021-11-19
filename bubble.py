nums = [1,3,5,2,4,9,8,6,7]
swaps = True

print(nums)

while swaps:
    swaps=False
    for j in range(len(nums)-1):
        if nums[j] > nums[j+1]:
            swaps=True
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)

help(range)