import random 

class Car:
    
    def __init__(self, GasAmount):
        self.GasAmount = GasAmount

    def getGasAmount(self):
        return(self.GasAmount)
    
class GasPump:
    
    def __init__(self, Periektikotita, carList):
        self.Periektikotita = Periektikotita
        self.carList = carList
        
    def car_in(self, new_car):
        return(self.carList.append(new_car))
    
    def car_out(self):
        return(self.carList.pop(0))
    
    def has_car_waiting(self):
        if not self.carList:
            return(False)
        else:
            return(True)
        
    def refuel(self, ncar):
        if self.Periektikotita >= ncar.getGasAmount():
            print('Can fuel car')
            self.Periektikotita -= ncar.getGasAmount()
            return(True)
        else:
            print('Can\'t fuel car')
            return(False)
        
    def get_gas_volume(self):
        return(self.Periektikotita)
    
    
def main():
    randnum = random.randint(0, 10000)
    randomcars = random.randint(0, 10)
    listOfCars = []
    adlia = GasPump()
    
    for i in range(randomcars):
        randomGasAmount = random.randint(0, 50)
        ncar = Car(randomGasAmount)
        listOfCars.append(ncar)
        
    for idx, i in enumerate(listOfCars):
        if adlia.refuel(i) == True:
            print('Proceed')
            listOfCars.pop(0)
        
        if not listOfCars:
            print(adlia.get_gas_volume())
