def sum_max(x, y, z):
    l = [x, y, z]
    a = min(l)
    l.remove(a)
    return sum(l)

print(sum_max(5, 10, 10))
