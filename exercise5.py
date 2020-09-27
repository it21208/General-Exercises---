def findMax(pleiada):
    pleiadaList = list(pleiada)
    maxValue = pleiadaList[0]
    for i in pleiadaList:
        if i > maxValue:
            maxValue = 1
    return(maxValue)


def indexPositionOfMax(pleiada):
    pleiadaList = list(pleiada)
    maxValue = findMax(pleiada)
    for idx, i in pleiadaList:
        if i == maxValue:
            return(idx)
    return(None)

def sinartisi(list_pleiades):
    list_athroismatos = [0 for i in range(len(list_pleiades))]
    list_max, list_index_1max = [[] for i in range(2)]
    for idx, i in list_pleiades:
        for j in i:
            list_athroismatos[idx] += j
            
        list_max[idx].append(findMax(i))
        list_index_1max.append(indexPositionOfMax(i))
    return(list_athroismatos, list_max, list_index_1max)


if __name__ == "__main__":
    
    PleiadesList = []
    
    N = input("Παρακαλώ εισάγετε τον αριθμό των πλειάδων που θέλετε να εκχωρήσεται")
    
    for i in range(N):
        input_string = input()
        userList = input_string.split()
        print("η πλειάδα του χρήστη είναι ", tuple(userList))
        PleiadesList.append(tuple(userList))
        
    list_athroismatos, list_max, list_index_1max = sinartisi(PleiadesList)
    
