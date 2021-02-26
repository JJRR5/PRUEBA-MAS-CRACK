
P = [[10,2,4],[2,3,6],[6,4,2]]
print(len(P))
L = P
print(P)
print(L)

for i in range(len(P)):
    for o in range(len(P)):
        L[i][o] = 5*P[i][o]
print(L)

        