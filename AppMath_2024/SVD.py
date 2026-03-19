# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 03:19:55 2022

@author: user
"""
# SVD example

import numpy as np

'''
####################
# SVD 예제
####################
A = [ [1, 1, 0 ], [0,-1,1]]
MA = np.array(A).astype(np.float64)
U, s, V = np.linalg.svd(MA, full_matrices = True)

S = np.zeros(MA.shape)
for i in range(len(s)):
    S[i][i] = s[i]
     
print(U)
print(S)
print(V)

#MA_rec = U*S*V
MA_rec = np.dot(U, np.dot(S,V))
print(MA_rec)
'''

'''
A = [ [1, 2, 1, 2, 1], [0, 1, -1, 0, 1] ]
MA = np.array(A).astype(np.float64)
MAT = MA.transpose()
MAAT = np.dot(MA, MAT)
'''

'''
from sympy import *
m = Matrix([
        [-.15, .8, -.4, -.25, 0],
        [-.1, -.1, .45, -.25, 0],
        [-.25, -.1, -.4, .75, 0]])
M_rref = m.rref()
print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))
'''

from sympy import *

A = Matrix([ [1, 2, 1, 2, 1], [0, 1, -1, 0, 1] ])
AT = A.T
AAT = A*AT
print(AAT)
ATA = AT*A
print("ATA=",ATA)
R = ATA.rref()
print(R)

from sympy.solvers.solveset import linsolve
x1, x2, x3, x4, x5 = symbols('x1, x2, x3, x4, x5')
print(linsolve(ATA, (x1, x2, x3, x4, x5)))

x = Matrix([ [1, 0, 1, 1, -1]])
xt = x.T
ATAx = ATA*xt
b = ATAx
print(b)
print(linsolve((ATA, b), (x1, x2, x3, x4, x5))) 

print(ATA.eigenvals())
print(ATA.diagonalize())


D2 = Matrix([[2, 0], [0, 3]])
P2 = Matrix([[1,-1], [1,1]])
P2inv = P2.inv()
A2 = P2*D2*P2inv
print(A2)
print(A2.diagonalize())


b1 = Matrix([ [1], [-1], [2] ])
b2 = Matrix([ [0], [1], [-1] ])
rhs = Matrix([1, 0, 1])
B = Matrix([[1,0], [1,1], [-2,-1]])
BTB = B.T * B
print(BTB)
print(BTB.inv())
P = B*BTB.inv()*B.T
x_sol = BTB.inv()*B.T*rhs
print(P)
print(P*rhs)
print("x=", x_sol)


AA = [ [1, 1, 0 ], [0,1,1]]
MA = np.array(AA).astype(np.float64)
U, s, V = np.linalg.svd(MA, full_matrices = True)
print(s)
print(U)
print(V)
