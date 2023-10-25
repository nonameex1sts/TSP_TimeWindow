from ortools.sat.python import cp_model

model = cp_model.CpModel()

x = {}
# x0 = c, x1 = p, x2 = i, x3 = s, x4 = f, x5 = u, x6 = n, x7 = t, x8 = r, x9 = e

for i in range(10):
    x[i] = model.NewIntVar(0, 9, "x[%i]" % i)

model.Add(x[0] != 0)
model.Add(x[2] != 0)
model.Add(x[4] != 0)
model.Add(x[7] != 0)
# model.Add(x[0] != 6)

for i in range(10):
    for j in range(i+1, 10):
        model.Add(x[i] != x[j])

model.Add(10 * x[0] + x[1] + 10 * x[2] + x[3] +
          100 * x[4] + 10 * x[5] + x[6] ==
          1000 * x[7] + 100 * x[8] + 10 * x[5] + x[9])

solver = cp_model.CpSolver()
solutions = cp_model.VarArraySolutionPrinter([x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9]])
solver.SearchForAllSolutions(model, solutions)

# solver = cp_model.CpSolver()
# status = solver.Solve(model)
#
# if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
#     print(f"c: {solver.Value(x[0])}")
#     print(f"p: {solver.Value(x[1])}")
#     print(f"i: {solver.Value(x[2])}")
#     print(f"s: {solver.Value(x[3])}")
#     print(f"f: {solver.Value(x[4])}")
#     print(f"u: {solver.Value(x[5])}")
#     print(f"n: {solver.Value(x[6])}")
#     print(f"t: {solver.Value(x[7])}")
#     print(f"r: {solver.Value(x[8])}")
#     print(f"e: {solver.Value(x[9])}")
# else:
#     print("No solution")