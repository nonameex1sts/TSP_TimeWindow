from ortools.linear_solver import pywraplp

N = 8

V = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
E = [('A', 'B'), ('A', 'G'), ('A', 'F'), ('B', 'C'), ('B', 'G'), ('B', 'H'), ('G', 'H'), ('G', 'C'),
     ('G', 'E'), ('G', 'F'), ('F', 'E'), ('F', 'H'), ('C', 'H'), ('C', 'D'), ('H', 'E'), ('H', 'D'), ('E', 'D')]

# Create the solver
model = pywraplp.Solver.CreateSolver('SCIP')

# Define the variables and constraints
X = []

# X[i][j] = 1 if the i vertex has the value j+1
for i in range(8):
    X.append([])
    for j in range(8):
        X[i].append(model.IntVar(0, 1, f'X[{i}][{j}]'))

for i in range(8):
    model.Add(sum(X[i][j] for j in range(8)) == 1)

for i in range(8):
    model.Add(sum(X[j][i] for j in range(8)) == 1)

for (x, y) in E:
    for i in range(7):
        # x and y cannot be consecutive (i and i+1)
        # if vertex x has value i, vertex y cannot have value i+1 and vice versa
        model.Add(X[V[x] - 1][i] + X[V[y] - 1][i + 1] <= 1)
        # if vertex x has value i+1, vertex y cannot have value i and vice versa
        model.Add(X[V[x] - 1][i + 1] + X[V[y] - 1][i] <= 1)

model.Add(sum((j + 1) * X[6][j] for j in range(8)) - sum((j + 1) * X[7][j] for j in range(8)) <= -1)
model.Add(sum((j + 1) * X[1][j] for j in range(8)) - sum((j + 1) * X[5][j] for j in range(8)) <= -1)

status = model.Solve()

if status == pywraplp.Solver.OPTIMAL:

    # Print the schedule
    for i in range(8):
        for j in range(8):
            val = X[i][j].solution_value()
            if val == 1:
                print(j + 1, end=" ")
else:
    print('')
