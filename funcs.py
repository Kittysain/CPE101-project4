# Project 4
#
# Name: Kitty Zhuang and Josh Zhang
# Instructor: S. Einakian
# Section: CPE101_01
####################################################

# this function checks if any of the rows has repeated values and returns false if there is, otherwise, it returns true
# list ---> boolean
def validate_rows(grid):
    list = []
    for col in range(5, 30, 5):
        list.append(grid[(col - 5):col])
    for rows in list:
        newList = []
        for num in rows:
            if num in newList:
                return False
            newList.append(num)
    return True


# This transpose function change the original rows to columns, and columns to rows.
# list -> list
def transpose(grid):
    new_list = [0 for x in range(25)]
    for index in range(len(grid)):
        row = index // 5
        col = index % 5
        new_index = col * 5 + row
        new_list[new_index] = grid[index]
    return new_list


# This validate_cages function checks if the sum of the cage is equal to the required sum to the cage. Returns wheh they are equal.
# list, list -> boolean
def validate_cages(grid, cages):
    for item in cages:
        list = []
        requiredsum = item[0]
        indexes = item[1:]
        for index in indexes:
            num = grid[int(index)]
            list.append(int(num))
        sum = 0
        for value in list:
            sum += value
        if 0 in list and sum < int(requiredsum) or 0 not in list and sum == int(requiredsum):
            continue
        elif 0 in list and sum >= int(requiredsum) or 0 not in list and sum != int(requiredsum):
            return False
    return True


# This function validate_cols checks if the columns of the grid has repeating values, returns false when there is repeating value, and returns true when there is not.
# list -> boolean
def validate_cols(grid):
    new_grid = transpose(grid)
    return validate_rows(new_grid)


# This function validate_all checks the cols, rows for repeating value, and the sum of the grid. Returns true when all three condition are validate.
# list,list ->boolean
def validate_all(grid, cages):
    res = validate_cages(grid, cages) == validate_cols(grid) == validate_rows(grid) == True
    return res
