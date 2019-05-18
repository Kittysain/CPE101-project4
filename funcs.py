# Project 4
#
# Name: Kitty Zhuang and Josh Zhang
# Instructor: S. Einakian
# Section: CPE101_01
####################################################

def validate_rows(grid):

  
# This transpose function change the original rows to columns, and columns to rows. 
# list -> list
def transpose(grid):
    new_list= [0 for x in range(25)]
    for index in range (len(grid)):
        row =  index // 5
        col = index % 5
        new_index = col * 5 + row
        new_list[new_index]= grid[index]
    return new_list

# This validate_cages function checks if the sum of the cage is equal to the required sum to the cage. Returns wheh they are equal.
# list, list -> boolean
def validate_cages(grid, cages):
    sum_list = []
    validate_list = [item[0] for item in cages]
    for item in cages:
        new_list = item[1:]
        sum = 0
        for index in new_list:
            sum += grid[index]
        sum_list.append(sum)

    if sum_list == validate_list:
        return True
    else:
        return False
      
# This function validate_cols checks if the columns of the grid has repeating values, returns false when there is repeating value, and returns true when there is not.
# list -> boolean
def validate_cols(grid):
    new_grid = transpose(grid)
    return validate_rows(new_grid)

# This function validate_all checks the cols, rows for repeating value, and the sum of the grid. Returns true when all three condition are validate.
# list,list ->boolean
def validate_all(grid,cages):
    res = validate_cages(grid,cages) == validate_cols(grid) == validate_rows(grid) == True
    return res
