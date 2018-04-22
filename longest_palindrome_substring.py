import numpy as np

S = "ACGCTGTCAA"

table = np.zeros((len(S), len(S)), dtype=int)

for i in range(table.shape[0]):
    table[i,i] = 1

for i in range(table.shape[0]-1):
    if S[i] == S[i+1]:
        table[i,i+1] = 2

for s in range(1, len(table)-1):
    for i in range(0, len(table)-s):
        j = i + s
        if S[i] == S[j]:
            if table[i+1,j-1]:
                table[i,j] = table[i+1,j-1] + 2
        else:
            table[i, j] = 0

print(table)
print(np.max(table))