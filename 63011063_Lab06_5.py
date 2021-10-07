def asteroid_collision(asts,n = 1):
    if n >= len(asts):
        return asts
    if asts[n-1] > 0 and asts[n] < 0:
        if abs(asts[n-1]) > abs(asts[n]):
            asts.pop(n)
        elif abs(asts[n-1]) < abs(asts[n]):
            asts.pop(n-1)
        else:
            asts.pop(n-1)
            asts.pop(n-1)
        return asteroid_collision(asts,n-1)
    return asteroid_collision(asts,n+1)

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))