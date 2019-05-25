#Project4 - Calcudoku
#Name: Kitty Zhuang and Joshua Zhang
#Instructor: Einakian
#Section: 1

from funcs import *

def main():
    num_cages = int(input())
    cage = []
    for num in range(num_cages):
        cage_value = input()
        list_cage = cage_value.split()
        cage.append(list_cage)

    grid = 25 * [0]
    index = 0
    while index < 25:
        grid[index] += 1
        if validate_all(grid, cage) == True:
            index += 1
        elif grid[index] > 5:
            grid[index] = 0
            index -= 1


    new_grid = ""
    for rows in range(5):
        for col in range(5):
            index = (rows * 5) + col
            numbers = grid[index]
            new_grid += "".join(str(numbers)+' ')
        new_grid += "\n"

    print(new_grid)

if __name__ == '__main__':
    main()