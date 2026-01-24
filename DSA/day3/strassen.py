import numpy as np
def strassen(A, B):
    n = len(A)
    mid = n // 2
    if len(A) <= 2:
        return A * B
    
    a, b, c, d = split_matrix(A)
    e, f, g, h = split_matrix(B)
    p1 = strassen(a+d, e+h)
    p2 = strassen(d, g-e)
    p3 = strassen(a+b, h)
    p4 = strassen(b-d, g+h)
    p5 = strassen(a, f-h)
    p6 = strassen(c+d, e)
    p7 = strassen(a-c, e+f)

    c11 = p1 + p2 - p3 + p4
    c12 = p5 + p3
    c21 = p6 + p2
    c22 = p5 + p1 - p6 - p7
    C = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return C

def split_matrix(M):
    n = len(M)
    middle = n//2
    return M[:middle, :middle], M[:middle, middle:], M[middle:, :middle], M[middle:, middle:]


A = [[1, 2, 3, 4], 
     [5, 6, 7, 8], 
     [9, 10, 11, 12], 
     [13, 14, 15, 16]]
B = [[17, 18, 19, 20], 
     [21, 22, 23, 24], 
     [25, 26, 27, 28], 
     [29, 30, 31, 32]]
C = strassen(np.array(A), np.array(B))
print(C)