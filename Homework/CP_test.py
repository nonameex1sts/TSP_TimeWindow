from ortools.sat.python import cp_model

model = cp_model.CpModel()

x = {}
# x0 = A, x1 = B, x2 = C, x3 = D, x4 = E, x5 = F, x6 = G, x7 = H

for i in range(8):
    x[i] = model.NewIntVar(1, 8, "x[%i]" % i)

for i in range(7):
    for j in range(i+1, 8):
        model.Add(x[i] != x[j])

# AB
model.Add(x[0] - x[1] != 1)
model.Add(x[1] - x[0] != 1)

# AG
model.Add(x[0] - x[6] != 1)
model.Add(x[6] - x[0] != 1)

# AF
model.Add(x[0] - x[5] != 1)
model.Add(x[5] - x[0] != 1)

# BC
model.Add(x[1] - x[2] != 1)
model.Add(x[2] - x[1] != 1)

# BG
model.Add(x[1] - x[6] != 1)
model.Add(x[6] - x[1] != 1)

# BH
model.Add(x[1] - x[7] != 1)
model.Add(x[7] - x[1] != 1)

# GH
model.Add(x[6] - x[7] != 1)
model.Add(x[7] - x[6] != 1)

# GC
model.Add(x[6] - x[2] != 1)
model.Add(x[2] - x[6] != 1)

# GE
model.Add(x[6] - x[4] != 1)
model.Add(x[4] - x[6] != 1)

# GF
model.Add(x[6] - x[5] != 1)
model.Add(x[5] - x[6] != 1)

# FE
model.Add(x[5] - x[4] != 1)
model.Add(x[4] - x[5] != 1)

# FH
model.Add(x[5] - x[7] != 1)
model.Add(x[7] - x[5] != 1)

# CH
model.Add(x[2] - x[7] != 1)
model.Add(x[7] - x[2] != 1)

# CD
model.Add(x[2] - x[3] != 1)
model.Add(x[3] - x[2] != 1)

# HE
model.Add(x[4] - x[7] != 1)
model.Add(x[7] - x[4] != 1)

# HD
model.Add(x[7] - x[3] != 1)
model.Add(x[3] - x[7] != 1)

# ED
model.Add(x[4] - x[3] != 1)
model.Add(x[3] - x[4] != 1)

# G<H
model.Add(x[6] < x[7])

# B<F
model.Add(x[1] < x[5])

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(solver.Value(x[0]), end=" ")
    print(solver.Value(x[1]), end=" ")
    print(solver.Value(x[2]), end=" ")
    print(solver.Value(x[3]), end=" ")
    print(solver.Value(x[4]), end=" ")
    print(solver.Value(x[5]), end=" ")
    print(solver.Value(x[6]), end=" ")
    print(solver.Value(x[7]), end=" ")
else:
    print("")