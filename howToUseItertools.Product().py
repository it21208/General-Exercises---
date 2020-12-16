from itertools import product 

def cartesian_product(arr1, arr2): 

	# return the list of all the computed tuple 
	# using the product() method 
	return list(product(arr1, arr2)) 
	
# Driver Function 
if __name__ == "__main__": 
	arr1 = [1, 2, 3] 
	arr2 = [5, 6, 7] 
	print(cartesian_product(arr1, arr2)) 

''' Output: '''
# [(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]

# ===================

from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))

''' Sample Input '''
# 3 1000
# 2 5 4
# 3 7 8 9 
# 5 5 7 8 9 10 
''' Sample Output '''
# 206
