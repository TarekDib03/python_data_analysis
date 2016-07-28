# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''Write a function which accepts a 2D list of numbers and returns the sum 
of all the number in the list You can assume that the number of columns in 
each row is the same.'''

def sum_of_2D_list(arr):
    
    lst = []
    
    for l in arr:
        for num in l:
            lst.append(num)
        my_sum = 0
        for n in lst:
            my_sum = my_sum + n
    return my_sum
    
    
def avg_of_2D_list(arr):
    cnt = 0
    for l in arr:
        for n in l:
            cnt += 1
    return float(sum_of_2D_list(arr) / cnt)
    

# OR
def avg_of_2D_list2(arr):
    lst = []
    
    for l in arr:
        for num in l:
            lst.append(num)
        my_sum = 0
        for n in lst:
            my_sum = my_sum + n
    return float(my_sum/len(lst))
    
# OR
def _average_of_a_2d_list_sample_(sample_2d_list):
    # Initialize total sum to be 0
    total_sum = 0
    number_of_items=0
    # Get the length of rows and columns. This is a 2D matrix. So need 
    # to get all the elements in the matrix.
    for row_index in range(len(sample_2d_list)):
        for col_index in range(len(sample_2d_list[row_index])):
            total_sum=total_sum+sample_2d_list[row_index][col_index]
            number_of_items=number_of_items+1
    return total_sum/number_of_items

    
# OR
def _sum_of_a_2d_list_sample_(sample_2d_list):
    # Initialize total sum to be 0
    total_SUM = 0
    # Get the length of rows and columns
    number_of_rows = len(sample_2d_list)
    number_of_columns = len(sample_2d_list[0])
    # Initialize row index to 0
    rows = 0
    # Produce row indices 0, 1, 2, ...number_of_rows
    while rows < number_of_rows:
        # for each row, initialize the column index to 0
        columns = 0
        # Produce column indices 0, 1, 2, ... number_of_columns
        while columns < number_of_columns:
            # Added the element i.e. list[row][column] to total sum
            total_SUM = total_SUM + sample_2d_list[rows][columns]
            # Increment to the next column index
            columns = columns + 1
        # increment to the next row index
        rows = rows + 1
    # Finally return the total sum
    return total_SUM
    
    
'''Write a function that accepts a 2D list of integers and returns the 
maximum EVEN value for the entire list. You can assume that the number of 
columns in each row is the same. Your function should return None if the 
list is empty or all the numbers in the 2D list are odd. Do NOT use 
python's built in max() function.'''

# First let me create a function to find the maximum in a 1D list. Return the 
# maximum if it is even, otherwise return None
def max_even_1D_list(my_list):
    # Initialize maximum value
    my_max = float('-Inf')
    for num in my_list:
        if num%2 == 0:
            if num > my_max:
                my_max = num
    if my_max%2 == 0:
        return my_max

# Now with a 2D list
def max_even_2D_list(my_list):
    my_max = float('-Inf')
    
    for row_index in range(len(my_list)):
        for col_index in range(len(my_list[row_index])):
            if my_list[row_index][col_index] % 2 == 0:
                if my_list[row_index][col_index] > my_max:
                    my_max = my_list[row_index][col_index]
    if my_max % 2 == 0:
        return my_max
        

def sum_of_each_row(my_list):
    LIST = []
    for i in range(len(my_list)):
        LIST.append((sum(my_list[i])))
    return LIST
        

def list_2D_to_1D(MY_LIST):
    LIST = []    
    for i in range(len(MY_LIST)):
        for j in range(len(MY_LIST[i])):
            LIST.append(MY_LIST[i][j])
    return sorted(LIST)
    
# OR use extend method
def list_2D_to_1D2(MY_LIST):
    LIST = []
    for lst in MY_LIST:
        LIST.extend(lst)
    return sorted(LIST)
    
# Matrix multiplication using numpy module
def matrix_multiplication(a, b):
    import numpy as np    
    #if len(a[0]) == len(b):
    if len(a[0]) != len(b):
        raise Warning("Number of columns in a is not equal to number of rows")
    else:
        m = np.dot(a,b)
    return m.tolist()

# Matrix multiplication not using numpy module, but rather an algorithm to
# multiply two matrices
def matrix_mult(a, b):
    # Initialize the output matrix
    C = [[0 for y in range(len(a[0]))] for x in range(len(a))]
    #inner_list = len(a[0])*[0]
    #for r in range(len(a)):
     #   C.append(inner_list[:])  
    
    # Number of rows of matrix a    
    for i in range(len(a)):
        # Number of columns of matrix b
        for j in range(len(b[0])):
            # Initialize the sum
            my_sum = 0
            # Multiply corresponding elements in the two matrices
            for k in range(len(a[0])):
                my_sum = my_sum + a[i][k]*b[k][j]
            # Set the multiplied elements into matrix C
            C[i][j] = my_sum
    return C
    
    

def list_to_tuples(MY_LIST):
    
    for LIST in MY_LIST:
        # Reverse each of the inner lists
        LIST = LIST.reverse()
    
    for i in range(0, len(MY_LIST)):
        # Convert each of the inner list into tuple
        MY_LIST[i] = tuple(MY_LIST[i])
    return tuple(MY_LIST)