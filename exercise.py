from numpy import loadtxt
import numpy as np
import math

# declaring path to data
pathToRead = '/home/pfb16181/nh_temperature.txt'
# read temperature data 
lines = loadtxt(pathToRead, dtype=str, comments="#", delimiter=",", unpack=False)

# print(lines[0])

# initialise 3 counters to count the number of years in the dataset falling into the three categories 
countYearsinCatA = 0
countYearsinCatB = 0
countYearsinCatC = 0
# initialise 3 variables to sum the March temperatures of each category
sumA = 0
sumB = 0
sumC = 0
# looping through all years
for line in lines:
    # split line on whitespace
    newLine = line.split()
    # get year from list
    CurYear = newLine[0]
    # get only year
    CurYear = CurYear.split('.')[0]
    
    # get temperatures for the 12 months of the current year
    temperaturesOfCurYear = newLine[1:]
    # get March temperature 
    MarchTemperature = temperaturesOfCurYear[2]
    
    # check in which category it belongs and increase the counter by 1 
    # and add the temperature to the corresponding aggregator
    if float(MarchTemperature) <= -0.5:
        countYearsinCatA += 1
        # cast string to float to do the calculation
        sumA += float(MarchTemperature)
    
    if float(MarchTemperature) >= 0.5:
        countYearsinCatB += 1
        # cast string to float to do the calculation
        sumB += float(MarchTemperature)
    
    if float(MarchTemperature) > -0.5 and float(MarchTemperature) < 0.5:
        countYearsinCatC += 1
        # cast string to float to do the calculation
        sumC += float(MarchTemperature)
        

print('{} years fall in category a. and the corresponding mean temperature is {}'.format(countYearsinCatA, sumA/countYearsinCatA))
print('{} years fall in category b. and the corresponding mean temperature is {}'.format(countYearsinCatB, sumB/countYearsinCatB))
print('{} years fall in category c. and the corresponding mean temperature is {}'.format(countYearsinCatC, sumC/countYearsinCatC))

# convert numpy array to list
listlines = list(lines)
newList = []
for line in listlines:
    newList.append([float(i) for i in line.split()])

data = np.asarray(newList)


# find subset of numpy array meeting the condition - get years only
yearsMeetingCondition = data[np.where(data[:, 3] > 0.5)][:, np.array([True, False, False, False, False, False, False, False, False, False, False, False, False])]

# find subset of numpy array meeting the condition - get temperatures only
dataMeetingCondition = data[np.where(data[:, 3] > 0.5)][:, np.array([False, True, True, True, True, True, True, True, True, True, True, True, True])]

# print median year of this subset
print('The median year of this subset is {}.'.format(int(yearsMeetingCondition[(math.ceil(len(yearsMeetingCondition)/2))])))

# show number of years in this subset
print('The number of years in this subset is {}.'.format(len(yearsMeetingCondition)))

# show mean and standard deviation of temperature for this subset
print('The mean and standard deviation of temperature for this subset is {} and {}.'.format(np.mean(dataMeetingCondition), np.std(dataMeetingCondition, dtype=np.float64)))
