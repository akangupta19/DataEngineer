N = 3


def scalarProductMat(mat, k):
    for i in range(N):
        for j in range(N):
            mat[i][j] = mat[i][j] * k


if __name__ == "__main__":
   mat = [[12, 7, 3],
           [4, 5, 6],
           [7, 8, 9]]
   k = 9

   scalarProductMat(mat, k)

   print("Scalar Product Matrix is : ")
   for i in range(N):
        for j in range(N):
           print(mat[i][j], end=" ")
        print()



