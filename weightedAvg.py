def weighted_avg_m2(distribution, weights):
    weighted_sum = []
    for salary, weight in zip(distribution, weights):
        weighted_sum.append(salary * weight)    
    return(round(sum(weighted_sum) / sum(weights),2))
		
input()
distribution = [int(x) for x in input().split()]
weights = [int(x) for x in input().split()]
print(round(weighted_avg_m2(distribution, weights),1))
