#  a function that read a text file and converts certain words in that text and captures the number of changes

def myfunction(infile, convert, outfile):
    cnt_changes = 0
    tempList = []
    try:
        f = open(infile, 'r')
        for idx, line in enumerate(f):
            newLine = line.strip('\n')
            newLineList = newLine.split(" ")
            tempSentenceList = []
            for i in newLineList:
                if i in convert.keys():
                    tempSentenceList.append(convert[i])
                    cnt_changes += 1
                else:
                    tempSentenceList.append(i)
            tempList.append(''.join([word for word in tempSentenceList]))
    except Exception as e:
        print(e)
    print("Πλήθος αλλαγών που έγιναν {}".format(cnt_changes))
    
    try:
        with open(outfile, 'w') as f:
            for item in tempList:
                f.write("%s\n" % item)
    except Exception as e:
        print(e)