
def q4(reshima):
    for i in range(len(reshima)):
        for j in range(i + 1, len(reshima)):
            so(reshima, i, j)
    return reshima

def so(l, i, j):
    if l[i] > l[j]:
        l[i], l[j] = l[j], l[i]


z = [19, 15, 70, 32, 13, 9, 81, 3, 52, 140, 100, 20]
print(q4(z))
