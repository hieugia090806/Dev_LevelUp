# -- Open File. -- #
file = open("Practice.txt", "rt")
print(file.read())
file.close()

# -- Different Location. -- #
file02 = open(r"D:\Dev_LevelUp\Day02\Description.txt", "rt")
print(file02.read())
file02.close()

# -- Using with statement. -- #
with open(r"D:\Dev_LevelUp\Day03\Description.txt", "rt") as file03:
    # Read all lines
    print(file03.readlines())

# Re-open file to demonstrate readline()
with open(r"D:\Dev_LevelUp\Day03\Description.txt", "rt") as file03:
    print(file03.readline())

# Re-open file to demonstrate read(5)
with open(r"D:\Dev_LevelUp\Day03\Description.txt", "rt") as file03:
    print(file03.read(5))

# -- Write to file. -- #
with open(r"D:\Dev_LevelUp\Day06\Practice.txt", "a") as file06:
    file06.write("\nNow the file has more content!")

# -- Read updated file. -- #
with open(r"D:\Dev_LevelUp\Day06\Practice.txt", "rt") as newfile:
    print(newfile.readlines())