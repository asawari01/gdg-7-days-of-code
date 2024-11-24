m, n = map(int, input("Enter rows and columns: ").strip().split())

mat = []

for i in range(m):
    mat.append(list(map(int, input("Enter: ").split())))

zero_col = set()
zero_row = set()

for i in range(m):
    for j in range(n):

        if mat[i][j] == 0:
            zero_row.add(i)
            zero_col.add(j)

for i in zero_row:
    for j in range(n):
        mat[i][j] = 0

for j in zero_col:
    for i in range(m):
        mat[i][j] = 0

print("Updated Matrix:")
for row in mat:
    print(*row)


