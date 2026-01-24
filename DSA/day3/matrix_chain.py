def matrix_chain(dimensions):
    n = len(dimensions) - 1
    m = {(i, j): float("inf") for i in range(1, n+1) for j in range(i, n+1)}

    for i in range(1, n+1):
        m[(i,i)] = 0
    
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i == j:
                m[(i,j)] = 0
            else:
                for k in range(i,j):
                    cost = m[(i,k)] + m[(k+1,j)] + (dimensions[i-1] * dimensions[k] * dimensions[j])
                    m[(i,j)] = min(cost, m[(i,j)])
    return m[(1,n)]

dimensions = [5, 20, 10, 50]
min_cost = matrix_chain(dimensions)
print(f"Minimum number of multiplications is {min_cost}")



