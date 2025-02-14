import os
import numpy as np
import sympy as sp
from collections import deque

# solution can be in the interval
# how to extract solution (x1, x2, ..., xn) the final_matrix
# 1 appended if 'ge' or 'greater' and -1 is appended when 'le' or 'less'


class Matrix:
    def __init__(self, mat):
        self.mat = np.array(mat)
        self.rows = len(self.mat)
        self.cols = len(self.mat[0])

    def print_mat(self):
        print(self.mat)

    def pivot_column(self):
        matrix = self.mat
        target_row = matrix[0]
        maximum = max(target_row)
        for i in range(len(target_row)):
            if target_row[i]==maximum:
                return i


    def pivot_row(self, pivot_column):
        matrix = self.mat
        col_of_const = len(matrix[-1])-1
        ratios = []
        for i in range(1, len(matrix)):
            if matrix[i][pivot_column]!=0:
                ratios.append(matrix[i][col_of_const]/matrix[i][pivot_column])
            else:
                ratios.append(1000000000)

        minimum = 1000000000
        for x in ratios:
            if x>=0 and x<minimum:
                minimum=x

        for i in range(len(ratios)):
            if ratios[i]==minimum:
                return i+1


    def find_pivot(self):
        matrix = self.mat
        j = self.pivot_column()
        i = self.pivot_row(j)
        # print(f"PIVOT IS {matrix[i][j]} at {[i,j]}")
        return [matrix[i][j], [i,j]]


 
    def columnRREF(self):
        matrix = np.array(self.mat, float)
        rows, columns = matrix.shape
        pivot, indices = self.find_pivot()
        pRow, pCol = indices

        # make pivot = 1 by dividing the whole row by pivot's value
        matrix[pRow] = matrix[pRow]/pivot

        # make nonpivotal elements in the column = 0
        for i in range(rows):
            if i == pRow: 
                if i+1<rows: i+=1
                else:break
            matrix[i] -= matrix[i][pCol]*matrix[pRow]

        return matrix
    
    def location(self):
        rows, columns = self.mat.shape
        n = columns - 1  

        obj_f = ''
        for i in range(n):  
            if i == 0:
                obj_f += f'({self.mat[0][i]})x_{i+1}'
            else:
                obj_f += f' + ({self.mat[0][i]})x_{i+1}'
        obj_f += f' = ({self.mat[0][-1]})' 

        constants = [self.mat[i][-1] for i in range(1, rows)]

        basics = []
        pRows = []
        non_basics = []

        for j in range(n):  
            zeros = 0
            one = 0
            negative_one = 0
            pRow = -1  
            for i in range(1, rows):  
                if self.mat[i][j] == 0:
                    zeros += 1
                elif self.mat[i][j] == 1:
                    one += 1
                    pRow = i
                elif self.mat[i][j] == -1:
                    negative_one += 1
                    pRow = i

            if zeros == rows - 2 and one == 1:  
                basics.append((f"x_{j+1}", float(self.mat[pRow][-1])))  
                pRows.append(pRow)
            elif zeros == rows - 2 and negative_one == 1:
                basics.append((f"x_{j+1}", float(-self.mat[pRow][-1])))  
                pRows.append(pRow)   

        for j in range(n):  
            if j + 1 not in [int(b[0][2:]) for b in basics]: 
                non_basics.append((f"x_{j+1}", 0))  

        return f"Objective function: {obj_f}\nBasic solutions: {basics}; Non-Basic solutions: {non_basics}"

    


    # continue process of modifying matrix until all elements in the 1st row <= 0
    def final_matrix(self, num): # num is numner of variables needed to output current point
        point = []
        step = 0
        for _ in range(num):
            point.append(0)

        step = 0
        print(f'\nStep {step}')
        print(self.location())
        while not all(x <= 0 for x in self.mat[0]):
            self.mat  = self.columnRREF()
            step += 1
            print(f'\nStep {step}')
            print(self.location())


        print("\nFinal Matrix: ")
        return self.print_mat()
    


# Nessesary Info
i = int(input('Enter the test file to open (integer input): '))

with open(f'C:/Users/DELL/Desktop/tests/test{i}.txt', 'r') as file:
    content = file.readlines()

content = [line.strip() for line in content]

n = int(content[0])
m = int(content[1]) 

objective_function = list(map(float, content[2].split()))

constrains = deque()

for i in range(m):
    constrain = []
    type_of_constrain = content[3 + 2 * i]  # The constraint type is on its own line
    coeffs_and_const = list(map(float, content[4 + 2 * i].split()))  # The next line contains coefficients and constant

    for j in range(n+m+1): # total number of coefficients of basic and slack variables, as well as constant result 
        if j < n: # index of basic variables
            coeffs_and_const[j] = float(coeffs_and_const[j])
            constrain.append(coeffs_and_const[j])
        elif j == n+i and (type_of_constrain == 'ge' or type_of_constrain == 'greater'): # index of slack=1 when column = num of constrain + basic variables 
            constrain.append(-1.0)
        elif j == n+i and (type_of_constrain == 'le' or type_of_constrain == 'less'): # index of slack=1 when column = num of constrain + basic variables 
            constrain.append(1.0)
        elif j <= n+m-1 or type_of_constrain == 'equal': # all other slack variables values = 0 (identity matrix)
            constrain.append(0.0)
        if j == n+m: # index in which const value is after basic and slack variables
            constrain.append(float(coeffs_and_const[-1]))

    constrains.append(constrain)

matrix = deque(constrains)
row1 = []
objective_function = deque(objective_function)
for _ in range(len(constrains[-1])):
    if objective_function:
        row1.append(objective_function.popleft())
    else: row1.append(0.0)
matrix.appendleft(row1)

matrix = Matrix(matrix) # we make matrix a class of Matrix only here because we used deque attribute above
print("Initial Matrix:")
matrix.print_mat()

# print(matrix.columnRREF())
matrix.final_matrix(n)


