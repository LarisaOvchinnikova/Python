n = int(input("Enter number of sportsmen: "))
results = []
for i in range(1, n+1):
    res = int(input(f"Enter result of {i} swimmer: "))
    results.append(res)
print(f"Results of competition: {results}")
print(f"Result of winner: {min(results)}")
