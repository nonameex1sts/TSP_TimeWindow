import numpy
from ortools.linear_solver import pywraplp

# Input
n, m = map(int, input().split())
b = {}
A = []

c = list(map(int, input().split()))

identityMatrix = [[0 for j in range(m)] for i in range(m)]

for i in range(m):
    for j in range(m):
        if i == j:
            identityMatrix[i][j] = 1

for i in range(m):
    A.append(list(map(int, input().split())) + list(identityMatrix[i]))

b = list(map(int, input().split()))

# Create the mip solver with the SCIP backend.
solver = pywraplp.Solver.CreateSolver("SCIP")
if not solver:
    print("Fail")

x = {}
# x are integer non-negative variables.
for i in range(n + m):
    x[i] = solver.IntVar(0, solver.infinity(), "x[%i]" % i)

# Constraints
for i in range(m):
    constraint = solver.RowConstraint(0, b[i], "")
    for j in range(n + m):
        constraint.SetCoefficient(x[j], A[i][j])

# Maximize x + 10 * y.
solver.Maximize(sum(c[i] * x[i] for i in range(n)))

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print(n)
    for i in range(n):
        print(x[i].solution_value(), end=' ')
else:
    print("UNBOUNDED")