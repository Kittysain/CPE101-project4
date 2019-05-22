#Project4 - Calcudoku
#Name: Kitty Zhuang and Joshua Zhang
#Instructor: Einakian
#Section: 1

from funcs import *

def main():
    numcages = int(input())
    cage = []
    for num in range(numcages):
        cagevalue = input()
        listcage = cagevalue.split()
        cage.append(listcage)
    grid = 25 * [0]
    cell = 0
    while cell < 25:
        grid[cell] += 1
        if validate_all(grid, cage) == True:
            cell += 1
        elif grid[cell] > 5:
            grid[cell] = 0
            cell -= 1

    newgrid = ""
    for rows in range(5):
        for col in range(5):
            index = (rows * 5) + col
            numbers = grid[index]
            newgrid += " ".join(str(numbers))
        newgrid += "\n"

    print(newgrid)




# Run the unit tests.
if __name__ == '__main__':
    main()
