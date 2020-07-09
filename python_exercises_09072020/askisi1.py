# δημιουργία ορισμού συνάρτησης υπολογισμού BMI
def calculateBMI(weight, height):
    BMI = weight/pow(height, 2)
    return(BMI)

# από εδώ ξεκινάει το πρόγραμμα
if __name__ == '__main__':
    # Ρωτάμε τον χρήστη να εισάγει το βάρος του
    print("Please enter your weight in kilos (metric unit) (e.g. 75): ", end="")
    # διαβάζουμε το βάρος
    weight = input()
     
    while True:
        # Ρωτάμε τον χρήστην να εισάγει το ύψος του
        print("Please enter your height in meters (metric unit): (e.g. 1.75): ", end="")
        #  διαβάζουμε το ύψος του μέτρα
        height = input()
        # εδώ πρέπει να ελέγξουμε αν ο χρήστης εισάγει το ύψος χρησιμοποιώντας το σωστό σύμβολο την τελεία και όχι το κόμμα για τα δεκαδικά
        # εάν ο χρήστης εισάγει με σωστό τρόπο το ύψος το πρόγραμμα προχωραέι αλλιώς συνεχίζει να ρωτάει τον χρήστη να εισάγει σωστά το ύψος  
        if ',' not in height:
            break
        print('Use . instead of , to denote decimals')
    
    # κλήση της συνάρτησης υπολογισμού του BMI και περνάω ως παραμέτρους το βάρος και ύψος αφού τα κάνω cast από string σε πραγματικούς αριθμούς 
    BMI = calculateBMI(float(weight), float(height))
    print('You entered {} kgs and {} m. Your BMI is {}'.format(weight, height, BMI))

    if BMI <= 18.4:
        print('ελλιποβαρής')
    elif BMI <= 24.9: 
        print('φυσιολογικού βάρους')
    elif BMI < 29.9:
        print('υπέρβαρος')
    else:
        print('παχύσαρκος')
