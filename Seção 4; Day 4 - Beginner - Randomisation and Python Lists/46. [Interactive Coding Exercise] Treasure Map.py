# ð¨ Don't change the code below ð
row1 = ["â¬ï¸","â¬ï¸","â¬ï¸"]
row2 = ["â¬ï¸","â¬ï¸","â¬ï¸"]
row3 = ["â¬ï¸","â¬ï¸","â¬ï¸"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# ð¨ Don't change the code above ð

#Write your code below this row ð

# Coluna primeiro, Linha por Ãºltimo
map[int(position[1])-1][int(position[0])-1] = "X"

#Write your code above this row ð

# ð¨ Don't change the code below ð
print(f"{row1}\n{row2}\n{row3}")