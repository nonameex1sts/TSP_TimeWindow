from ortools.sat.python import cp_model

model = cp_model.CpModel()

x = {}
# x0 = s, x1 = e, x2 = n, x3 = d, x4 = m, x5 = o, x6 = r, x7 = y

for i in range(8):
    x[i] = model.NewIntVar(0, 9, "x[%i]" % i)

model.Add(x[0] != 0)
model.Add(x[4] != 0)

for i in range(8):
    for j in range(i+1, 8):
        model.Add(x[i] != x[j])

model.Add(1000 * x[0] + 100 * x[1] + 10 * x[2] + x[3] +
          1000 * x[4] + 100 * x[5] + 10 * x[6] + x[1] ==
          10000 * x[4] + 1000 * x[5] + 100 * x[2] + 10 * x[1] + x[7])

solver = cp_model.CpSolver()
solutions = cp_model.VarArraySolutionPrinter([x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]])
solver.SearchForAllSolutions(model, solutions)

# solver = cp_model.CpSolver()
# status = solver.Solve(model)
#
# if status == cp_model.OPTIMAL:
#     print(f"s: {solver.Value(x[0])}")
#     print(f"e: {solver.Value(x[1])}")
#     print(f"n: {solver.Value(x[2])}")
#     print(f"d: {solver.Value(x[3])}")
#     print(f"m: {solver.Value(x[4])}")
#     print(f"o: {solver.Value(x[5])}")
#     print(f"r: {solver.Value(x[6])}")
#     print(f"y: {solver.Value(x[7])}")