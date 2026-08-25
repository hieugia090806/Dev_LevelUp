nums = list(map(int, input("Please enter list of number: ").split()))
target = int(input("Please enter the target: "))
results = []
for i in range(len(nums)-1):
    if nums[i] + nums[i+1] == target:
        results.append([i, i+1])
print(results)