# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:33:49 2020

@author: Logan Rowe

Given a rectangular matrix containing only digits, calculate the number of 
different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.

Here are all 6 different 2 × 2 squares:

1 2
2 2
2 1
2 2
2 2
2 2
2 2
1 2
2 2
2 3
2 3
2 1
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer matrix

Guaranteed constraints:
1 ≤ matrix.length ≤ 100,
1 ≤ matrix[i].length ≤ 100,
0 ≤ matrix[i][j] ≤ 9.

[output] integer

The number of different 2 × 2 squares in matrix.
"""

import numpy as np

def identical_matrices(m1,m2):
    '''
    check if matrix 1 (m1) and matrix 2 (m2) are identical
    '''
    for (row1,row2) in zip(m1,m2):
        for (elem1,elem2) in zip(row1,row2):
            if elem1!=elem2:
                return False
    return True

def differentSquares(matrix):
    matrix=np.array(matrix)
    height,width=matrix.shape
        
    #track all unique matrices with a list
    square_matrices=[]
    
    for column in range(height-1):
        for row in range(width-1):
            add_matrix=True
            sub_matrix=matrix[column:column+2,row:row+2]
            
            #ensure no previous occurrences of the sub_matrix exist
            for existing_submatrix in square_matrices:
                if identical_matrices(existing_submatrix,sub_matrix):
                    add_matrix=False
            
            #add the sub_matrix to our list only if it is not already in the list
            if add_matrix:
                square_matrices.append(sub_matrix)
        
    return(len(square_matrices))
    
    
if __name__=='__main__':
    matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
    print(differentSquares(matrix))