with open("file1.txt") as file1_data:
    content1 = [int(data) for data in file1_data.read().split()]
with open("file2.txt") as file2_data:
    content2 = [int(data) for data in file2_data.read().split()]

result = [number for number in content1 if (number in content2)]

# Write your code above 👆

print(result)
