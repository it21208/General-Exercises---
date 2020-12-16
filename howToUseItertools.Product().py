from itertools import product 

def cartesian_product(arr1, arr2): 
	''' It returns the list of all the computed tuples using the product() method. '''
	return list(product(arr1, arr2))


def cartesian_product2(arr1, times):
	''' It returns the cartesian product of the provided itrable with itself for the number of times specified by the optional keyword “repeat”. '''
	return list(product(*arr1, repeat=times)
	
# Driver Function 
if __name__ == "__main__": 
	arr1 = [1, 2, 3] 
	arr2 = [5, 6, 7]
	times = 3
	print(cartesian_product(arr1, arr2))
        print(cartesian_product2(arr1, 3))

''' Output: '''
# [(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]

# ===================

from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
# in this case N is a list i.e. [1, 3, 14] 
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))

''' Sample Input '''
# 3 1000
# 2 5 4
# 3 7 8 9 
# 5 5 7 8 9 10 
''' Sample Output '''
# 206
