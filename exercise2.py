from operator import itemgetter

def mymethod(pleiadaLists):
    saveResults = []
    for lst in pleiadaLists:
        result = 1
        for x in lst:
            result = result * x
        saveResults.append(result)
    
    print('Τα γινόμενα των στοιχείων των λιστών είναι τα ακόλουθα: ', saveResults)
    
    def minimum(x):
        minim = x[0]
        for i in x[0:]:
            if i < minim:
                minim = i
        return(minim)

    for lst in pleiadaLists:
        print(minimum(lst))

if __name__ == '__main__':
    print('Παρακαλώ εισάγετε την πλειάδα')
    n = input()
    pleiada = []
    for i in range(0, int(n)):
        tmp = int(input())
        pleiada.append(tmp)
        
    pleiada_lists = []
    for i in pleiada:
        lst = []
        for j in range(0, i):
            tmp = float(input())
            lst.append(tmp)
        pleiada_lists.append(lst)
    
    mymethod(pleiada_lists)
