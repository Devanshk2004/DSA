def zigzag_sum(matrix, rows, cols):
    total = 0
    for i in range(rows):
        if i % 2 == 0:
            for j in range(cols):
                total += matrix[i][j]
        else:
            for j in range(cols - 1, -1, -1):
                total += matrix[i][j]
    return total

rows, cols = map(int, input().split())
matrix = []

for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print(zigzag_sum(matrix, rows, cols)) #zig