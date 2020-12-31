import numpy

N = int(input())
lst = [] 

for i in range(N):
    t = [float(j) for j in input().split()]  
    lst.append(t)

# computes the determinant of an array
print(str(round(numpy.linalg.det(lst), 2)))
# computes the eigenvalues and right eigenvectors of a square array
print(str(round(numpy.linalg.eig(lst), 2)))
# computes the multiplicative inverse of a matrix
print(str(round(numpy.linalg.inv(lst), 2)))
