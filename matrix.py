#Matrix operations
import numpy as np
matrix_A=np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix_B=np.array([[14,13,12],[10,8,4],[9,7,5]])
matrix_C=np.array([[1,2,3],[4,5,6],[10,15,12]])
#Addition
def add_matrices(matrix_A,matrix_B):
    result=[[0 for _ in range(len(matrix_A[0]))]for _ in range(len(matrix_A[0]))]
    for i in range(len(matrix_A)):
        for j in range(len(matrix_A[0])):
            result[i][j]=matrix_A[i][j]+matrix_B[i][j]
    np_result=np.add(matrix_A,matrix_B)
    print("Manual Addition:\n",result)
    print("Numpy Addition:\n",np_result)

#Subtraction
def subtract_matrices(matrix_A,matrix_B):
    result=[[0 for _ in range(len(matrix_A[0]))]for _ in range(len(matrix_A))]
    for i in range(len(matrix_A)):
        for j in range(len(matrix_A[0])):
            result[i][j]=matrix_A[i][j]-matrix_B[i][j]
    np_result=np.subtract(matrix_A,matrix_B)
    print("Manual Subtraction:\n",result)
    print("Numpy Subtraction:\n",np_result)

#Multiplication
def multiply_matrices(matrix_A,matrix_B):
    if(len(matrix_A[0])!=len(matrix_B)):
        print("Matrices cannot be multiplied")
        return
    result=[[0 for _ in range(len(matrix_A))]for _ in range(len(matrix_B[0]))]
    for i in range(len(matrix_A)):
        for j in range(len(matrix_B[0])):
            for k in range(len(matrix_A[0])):
                result[i][j]+=(matrix_A[i][k]*matrix_B[k][j])
    np_product=np.dot(matrix_A,matrix_B)
    print("Manual multiplication:\n",result)
    print("Numpy muliplication:\n",np_product)

def determinant(matrix):
    if(len(matrix)!=len(matrix[0])):
        print("Matrix is not square")
        return
    if(len(matrix)==2):
        return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    det=0
    a,b,c=matrix[0]
    d,e,f=matrix[1]
    g,h,i=matrix[2]
    det=a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
    np_det=np.linalg.det(matrix)
    print("Manual Determinant:\n",det)
    print("Numpy Determinant:\n",np_det)
def inverse(matrix):
    if(len(matrix)!=len(matrix[0])):
        print("Matrix is not square")
        return
    if(np.linalg.det(matrix)==0):
        print("Matrix is singular")
        return
    
    #Find the determinant
    det=np.linalg.det(matrix)
    np_inverse=np.linalg.inv(matrix)
    inverse_matrix=[[0 for _ in range(matrix[0])]for _ in range(matrix)]
    if(len(matrix)==2):
        inverse_matrix[0][0] = matrix[1][1]
        inverse_matrix[1][1] = matrix[0][0]
        inverse_matrix[0][1] = -matrix[0][1]
        inverse_matrix[1][0] = -matrix[1][0]
        inverse_matrix*=(1/det)
        print("Manual Inverse:",inverse_matrix)
        print("Numpy inverse: ",np_inverse)
    else:
        a=(matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2])*(-1**(0+1+0+1))
        b=(matrix[1][0] * matrix[2][2] - matrix[2][0] * matrix[1][2])*(-1**(0+1+1+1))
        c=(matrix[1][0] * matrix[2][1] - matrix[2][0] * matrix[1][1])*(-1**(0+1+2+1))

        d=(matrix[0][1] * matrix[2][2] - matrix[2][1] * matrix[0][2])*(-1**(1+1+0+1))
        e=(matrix[0][0] * matrix[2][2] - matrix[2][0] * matrix[0][2])*(-1**(1+1+1+1))
        f=(matrix[0][0] * matrix[2][1] - matrix[2][0] * matrix[0][1])*(-1**(1+1+2+1))

        g=(matrix[0][1] * matrix[1][0] - matrix[1][1] * matrix[0][2])*(-1**(2+1+0+1))
        h=(matrix[0][0] * matrix[1][2] - matrix[1][0] * matrix[0][2])*(-1**(2+1+1+1))
        i=(matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1])*(-1**(2+1+2+1))
        inverse_matrix[0]=a,d,g
        inverse_matrix[1]=b,e,h
        inverse_matrix[2]=c,f,i
        inverse_matrix*=(1/det)
        print("Manual Inverse:",inverse_matrix)
        print("Numpy inverse: ",np_inverse)
        

                      


add_matrices(matrix_A=matrix_A,matrix_B=matrix_B)
subtract_matrices(matrix_A=matrix_A,matrix_B=matrix_B)
multiply_matrices(matrix_A=matrix_A,matrix_B=matrix_B)
determinant(matrix=matrix_C)
inverse(matrix_A)
inverse(matrix_B)
inverse(matrix_C)


    