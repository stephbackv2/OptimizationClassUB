from scipy.optimize import linprog

c1 = [-8, -9, -5]
A1 = [[1,1,2], [2,3,4], [6,6,2]]
b1 = [2,3,8]
res = linprog(c1, A_ub=A1, b_ub=b1)
print(res.fun, res.x)