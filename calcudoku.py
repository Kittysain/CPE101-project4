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

    grid = [0]*25

    print(grid)
    print(cage)

    all_check = validate_all(grid,cage)
    cage_check = validate_cages(grid,cage)
    row_check = validate_rows(grid)

    print (all_check)
    print (cage_check)



    while row_check == False:

        i = 0
        while i < 25:
            if cage_check == True and grid[i] <= 5:
                grid[i] += 1
                if grid[i] > 5:
                    grid[i] = 0
                    i -= 1
                cage_check = validate_cages(grid, cage)
                i += 1

            elif cage_check == False:
                grid[i-1] = 0
                i -= 2
                cage_check = validate_cages(grid, cage)

        print(grid)

        row_check = validate_rows(grid)


# Run the unit tests.
if __name__ == '__main__':
    main()


