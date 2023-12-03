from ortools.sat.python import cp_model

n = int(input())
dist_matrix = {}
for i in range(n):
    dist_matrix[i] = {}
    data = input().split(" ")
    for j in range(n):
        dist_matrix[i][j] = int(data[j])

model = cp_model.CpModel()

x = {}
t = {}
for i in range(n):
    t[i] = model.NewIntVar(0, 1000000000, 't[%i]' % i)
    for j in range(n):
        x[i, j] = model.NewIntVar(0, 1, 'x[%i, %i]' % (i, j))

for i in range(n):
    model.Add(x[i, i] == 0)
    model.Add(sum(x[i, j] for j in range(n)) == 1)
    model.Add(sum(x[j, i] for j in range(n)) == 1)

model.Add(t[0] == 0)
for i in range(n):
    for j in range(n):
        if i != j and j != 0:
            model.Add(t[j] == t[i] + 1).OnlyEnforceIf(x[i, j])

model.Minimize(sum(dist_matrix[i][j] * x[i, j] for i in range(n) for j in range(n)))

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL:
    print(n)

    current_city = 0
    while 1:
        for i in range(n):
            if solver.Value(x[current_city, i]) == 1:
                print(i + 1, end=" ")
                current_city = i
                break
        if current_city == 0:
            break
