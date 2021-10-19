row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

user_input = input("Where do you want to put your treasure?")

row = int(user_input[0])
column = int(user_input[1])

target_row = map[row]
target_row[column] = "x"
map[row] = target_row

print(f"{row1}\n{row2}\n{row3}")

