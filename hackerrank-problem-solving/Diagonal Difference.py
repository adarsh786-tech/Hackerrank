def diagonal_sum(n, matrix):
    right_diagonal = 0
    left_diagonal = 0
    for i in range(0, n):
        for j in range(0, n):
            if ((i+j) == n-1):
                left_diagonal += matrix[i][j]

    for i in range(0, n):
        for j in range(0, n):
            if (i==j):
                right_diagonal += matrix[i][j]
    print(abs(right_diagonal-left_diagonal))


if __name__ == '__main__':
    n = int(input())
    r = n
    c = n
    a = [[0]*r for _ in range(c)]
    for i in range(n):
        a[i] = [int(j) for j in input().strip().split(" ")]
    diagonal_sum(n, a)
