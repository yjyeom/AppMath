# -*- coding: utf-8 -*-
"""
 2024. 4. 23.
@author: user
"""

#import numpy as np
from sympy import *


print('AppMath 2024 Midterm...')

#==[2] R-REF
print('==[Prob 2]==')
A = Matrix([[1, 2, 0, 2, 3], [1, 0, 2, 2, 0],[1, 1, 0, 3, 1],[1, 1, 2, 1, 2]])
print('R-REF(A) =', A.rref())

#- 문제용 RHS b-vec 만들기
xc = Matrix([[-2,-1,0,1,2]]).T
b = A*xc
print('b=',b)

x1, x2, x3, x4, x5 = symbols('x1, x2, x3, x4, x5')
print(linsolve((A, b), (x1, x2, x3, x4,x5)))


#==[3] Projection5
print('\n==[Prob 3]==')
b1 = Matrix([ [1], [1], [1] ])
b2 = Matrix([ [1], [-1], [0] ])
v = Matrix([[1, 0, 1]]).T
B = Matrix([[1,1], [1,-1], [1,0]])
print('b1 =', b1)
print('b2 =', b2)
print('v =', v)
print('B = [b1 b2] =', B)
BTB = B.T * B
print(BTB.inv())
P = B*BTB.inv()*B.T
Pv = P*v
coord = BTB.inv()*B.T*v
print('P =', P)
print('Pv =', Pv)
print('[alpha, beta] =', coord)




'''
#==[1] R-REF
print('==[Prob 1]==')
A = Matrix([[1,2,2], [2,1,2], [2,2,1]] )
B = Matrix([[A,A], [A,A]])
print('R-REF(A) =', A.rref())
print('R-REF(B) =', B.rref())

#- 문제용 RHS b-vec 만들기
xc = Matrix([[1,-1,2,-2,1,1]]).T
b = B*xc
print('b=',b)

x1, x2, x3, x4, x5, x6 = symbols('x1, x2, x3, x4,x5,x6')
print(linsolve((B, b), (x1, x2, x3, x4,x5,x6)))


#==[2]
print('\n==[Prob 2]==')
A2 = Matrix([[1,2],[2,5]])
e1 = Matrix([[1],[0]])
A2e1 = A2*e1
print('A2 =', A2)
print('e1 =', e1)
print('A3*e1 =', A2e1)

e2 = Matrix([[2],[-1]])
print('e2 =', e2)
norm_e2 = sqrt(e2.T*A2*e2)
print('norm-e2 =', norm_e2)
inner_e2e1 = e2.T*A2*e1
print('<e1,e2> =', inner_e2e1)


#==[4]
print('\n==[Prob 4]==')
b1 = Matrix([ [1], [1], [0] ])
b2 = Matrix([ [0], [1], [-1] ])
v = Matrix([[1, 1, 1]]).T
B = Matrix([[1,0], [1,1], [0,-1]])
print('b1 =', b1)
print('b2 =', b2)
print('v =', v)
print('B = [b1 b2] =', B)
BTB = B.T * B
print(BTB.inv())
P = B*BTB.inv()*B.T
Pv = P*v
coord = BTB.inv()*B.T*v
print('P =', P)
print('Pv =', Pv)
print('[alpha, beta] =', coord)

#==[5]
print('\n==[Prob 5]==')
A5 = [ [2,1], [2,2], [2,2], [1,2] ]
MA5 = Matrix(A5)
S = MA5.T*MA5
print('S = A^T*A =', S)
MA = np.array(A5).astype(np.float64)
U, s, V = np.linalg.svd(MA, full_matrices = True)
print(s)
print(U)
print(V)
'''

'''
#A = Matrix([[1,1,2], [2,1,1], [1,2,1]] )
A = Matrix([[1,1,2], [2,1,1]] )
print(A)
RA = A.rref()
print(RA)

AA = Matrix([[A,A], [A,A]])
RAA = AA.rref()
print(RAA)


b = Matrix([[1,2,3,4]]).T
x1, x2, x3, x4, x5, x6 = symbols('x1, x2, x3, x4,x5,x6')
print(linsolve((AA, b), (x1, x2, x3, x4,x5,x6)))
'''

'''
S = Matrix([[1,2, 2],[2,3, 2]])
c = Matrix([[1,1]]).T
print('S=',S)
print('c=',c)
a1, a2, a3 = symbols('a1, a2, a3')
print(linsolve((AA, c), (a1, a2, a3))) 
'''



'''
A = Matrix([ [1, 2, 1, 2, 1], [0, 1, -1, 0, 1] ])

AT = A.T
AAT = A*AT
print(AAT)
ATA = AT*A
print("ATA=",ATA)
R = ATA.rref()
print(R)
'''

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



from sympy import *
m = Matrix([
        [-.15, .8, -.4, -.25, 0],
        [-.1, -.1, .45, -.25, 0],
        [-.25, -.1, -.4, .75, 0]])
M_rref = m.rref()
print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))
'''

'''
from sympy.solvers.solveset import linsolve
x1, x2, x3, x4, x5 = symbols('x1, x2, x3, x4, x5')
print(linsolve(ATA, (x1, x2, x3, x4, x5)))

x = Matrix([ [1, 0, 1, 1, -1]])
xt = x.T
ATAx = ATA*xt
b = ATAx
print(ATA)
print(b)
print(linsolve((ATA, b), (x1, x2, x3, x4, x5))) 

#print(ATA.eigenvals())
#print(ATA.diagonalize())
'''

'''
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
'''