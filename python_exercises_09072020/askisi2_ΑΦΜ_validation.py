
# δημιουργία ορισμού συνάρτησης ελέγχου ΑΦΜ
def checkAFM(AFM):
    
    # δήλωση αρχικοποίησης ενός αθροιστή 
    sum_var = 0
    
    # δήλωση και αρχικοποίηση του εκθέτη που θα υψώσουμε στην δύναμη
    counter = 8
    
    # διαβάζω ένα ένα τα ψηφία του ΑΦΜ
    for character in AFM:
        
        if counter == 0:
            # αυτό θα σώσει το τελευταίο ψηφίο του ΑΦΜ στην τελευταία επανάληψη
            a9 = character
            
            # έξοδος από τον βρόγχο
            break
        
        # μετατρέπω κάθε χαρακτήρα σε ακέραιο
        sum_var += sum_var + int(character)*pow(2, counter)
        
        # μειώνουμε τον counter κατά ένα
        counter -= 1

        
    
    # υπολογισμός υπολοίπου
    ipoloipo = sum_var % 11
    
    if a9 == ipoloipo:
        decision = 'valid (έγκυρος)'
    else:
        decision = 'not valid (μη έγκυρος)'
        
    # return decision
    return(decision)



# από εδώ ξεκινάει το πρόγραμμα
if __name__ == '__main__':
    #  ρωτάμε τον χρήστη να εισάγει το ΑΦΜ της επιλογής του
    print("Please enter your the ΑΦΜ: ", end="")
    # διαβάζουμε το ΑΦΜ
    AFM = input()
    
    # καλούμε την συνάρτηση για τον έλεγχο ΑΦΜ 
    decision = checkAFM(AFM)
    
    # εκτύπωση μυνήματος
    print('The ΑΦΜ you entered is {}'.format(decision))
