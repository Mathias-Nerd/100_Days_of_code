#100 Days of code with python
#Author: Mathias Nerd
#PLacing a treasure in a grid
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
grid = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to pt the treasure? ")
column = int(position[0])-1
row = int(position[1])-1
grid[row][column] = "*"
for i in range(len(grid)):
    print(grid[i])