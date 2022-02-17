# Absolute path: Specify the location from the ROOT directory.
with open("E:/Users/CLIENTE/Desktop/my_text.txt", "r") as absolute_path_file:
    content = absolute_path_file.read()
print(content)

with open("../../../../../../test.txt", "r") as absolute_path_file2:
    content2 = absolute_path_file2.read()
print(content2)

# Relative path: Specify the location from the CURRENT directory

with open("text.txt", "r") as relative_path_file:
    content3 = relative_path_file.read()
print(content3)
