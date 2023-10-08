import random

def fitness(route, e, l, d, t):
    time = 0
    total_time = 0
    for i in range(len(route) - 1):
        a, b = route[i], route[i+1]
        travel_time = t[a][b]
        time = max(time + travel_time + d.get(a, 0), e.get(b, 0))
        total_time += time - e.get(b, 0) + d.get(b, 0)
    return total_time

def crossover(parent1, parent2):
    cut = random.randint(1, len(parent1) - 1)
    child1 = parent1[:cut] + [x for x in parent2 if x not in parent1[:cut]]
    child2 = parent2[:cut] + [x for x in parent1 if x not in parent2[:cut]]
    return child1, child2

def mutate(route):
    i, j = random.sample(range(len(route)), 2)
    route[i], route[j] = route[j], route[i]

N = int(input())
e, l, d = {}, {}, {}
t = []

# Initialize warehouse values
e[0] = l[0] = d[0] = 0

for i in range(1, N+1):
    e[i], l[i], d[i] = map(int, input().split())

for _ in range(N+1):
    t.append(list(map(int, input().split())))

population = [random.sample(range(1, N+1), N) for _ in range(100)]

for generation in range(20):
    population.sort(key=lambda route: fitness([0] + route + [0], e, l, d, t))
    new_population = population[:20]

    while len(new_population) < 100:
        parent1, parent2 = random.choices(population[:20], k=2)
        child1, child2 = crossover(parent1, parent2)
        if random.random() < 0.1:
            mutate(child1)
        if random.random() < 0.1:
            mutate(child2)
        new_population += [child1, child2]

    population = new_population

best_route = population[0]
print(N)
print(" ".join(map(str, best_route)))
