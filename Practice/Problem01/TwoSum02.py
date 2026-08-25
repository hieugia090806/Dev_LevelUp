nums = list(map(int, input("Please enter list of number: ").split()))
target = int(input("Please enter the target: "))
results = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            results.append(i)
            results.append(j)

print(results)