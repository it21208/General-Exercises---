/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package asksiseis;

import java.util.Scanner;

public class AskForPassword_1 {
    
    //  Δήλωση αριθμού ψηφίων password.
    public static final int PASSWORD_LENGTH = 6;
    
    // αρχικοποίηση την main  μεθόδου
    public static void main(String[] args) {
        
        // δηλώνω την μεταβλητή που θα έχει τον κωδικό
        String password;
        
        // δήλωση και αρχικοποίηση της μεταβλητής που θα χρησιμοποιηθεί ως ένδειξη
        // για τον αν ο χρήστης έβαλε σωστό κωδικό και άρα μπορούμε να βγούμε από 
        // τον επαναληπτικό βρόγχο στον οποίο θα εισέλθουμε από κάτω
        boolean flag = false;
        
        // εισέρχομαι στον επαναληπτικό βρόγχο
        do {
            // διαβάζω τον κωδικό που πληκτρολογεί ο χρήστης και ίσως χρειαστεί 
            // να ξαναδιαβάσω τον κωδικό που πληκτρολογεί ο χρήστης αν αρχικά είναι λάθος 
            // ο οποίος θα ελεγχθεί εκ νέου για την ορθότητά του
            password = readInput();
            
            // Ελέγχω αν ο κωδικός είναι σωστός με βάση τα κριτήρια που έχω εκτυπώσει 
            // στην μέθοδο readInput()
            if (is_Password_correct(password)) {
                // εκτυπώνω μήνυμα ότι είναι σωστός ο κωδικός            
                System.out.println("Password is correct: " + password);
                // δίνω στην μεταβλητή flag τέτοια λογική τιμή έτσι ώστε να βγει
                // από τον βρόγχο από την στιγμή που είναι σωστός ο κωδικός
                flag = true;
            } else {
                // εκτυπώνω μήνυμα ότι είναι σωστός ο κωδικός
                System.out.println("Not a valid password: " + password);
                // από την στιγμή που δεν είναι σωστός ο κωδικός η μεταβλητή παραμένει
                // με την ίδια τιμή αφού θα πρέπει να ξανα ζητήσω από τον χρήστη να βάλει έναν σωστό κωδικό 
                flag = false;
            }
          // από κάτω γίνεται ο έλεγχος του επαναληπτικού βρόγχου για να δούμε 
          // αν ο κωδικός που πληκτρολογήθηκε είναι σωστός ή αν είναι λάθος και 
          // πρέπει να επαναλάβουμε το από πάνω κομμάτι κώδικα.
        } while (flag == false); 
    
    }
    
    public static String readInput() {
        // χρησιμοποιώ την κλάση Scanner για να διαβάσω από τον χρήστη τον κώδικο
        Scanner input = new Scanner(System.in);
        // εκτυπώνω στον χρήστη τα επιτρεπτά κριτήρια για εισαγωγή κωδικού        
        System.out.print(
                "==================================================\n" +
                "1. A password must have at least six characters.\n" +
                "2. A password consists of only numbers, capital letters and lowercase letters.\n" +
                "3. A password must contain at least 1 number.\n" +
                "4. A password must contain at least 2 capital letters.\n" +
                "5. A password must contain at least 3 lowercase letters.\n" +
                "Please, input a password: ");
        
        // Διαβάζω από τον χρήστη τον κωδικό        
        String s = input.nextLine();
        // επιστρέφω τον κωδικό στην main
        return (s);
    }
    
    
    public static boolean is_Password_correct(String password) {
        
        // ελέγχω το μέγεθος του κωδικού αν έχει τουλάχιστον 6 ψηφία όπως ζητάει η άσκηση
        if (password.length() < PASSWORD_LENGTH) {
            System.out.println("Error: Password must have at least 6 characters!");
            return false;
        }
        
        
        // δήλωση και αρχικοποίηση 3 ακέραιων μεταβλητών με μηδέν
        // αυτή η μεταβλητή/μετρητής μετράει τον αριθμό των πεζών γραμμάτων του κωδικού
        int lowercaseCount = 0;
        // αυτή η μεταβλητή μετράει τον αριθμό των κεφαλαίων γραμμάτων του κωδικού
        int capitalcaseCount = 0;
        // αυτός ο μετρητής μετράει τον αριθμό των ψηφίων/νούμερων του κωδικού
        int numCount = 0;
        
        // μπαίνουμε σε ένα επαναληπτικό βρόγχο και εξετάζουμε το κάθε γράμμα ή
        // νούμερο του κωδικού
        for (int i = 0; i < password.length(); i++) {
            // παίρνουμε το κάθε ψηφίο του κωδικού
            char ch = password.charAt(i);
            // εξετάζουμε αν είναι αριθμός το κάθε ψηφίο του κωδικού και εφόσον
            // είναι αυξάνουμε τον αντίστοιχο μετρητή 
            if (is_Numeric(ch)) {
                numCount++;
            }
            // μετράω πόσα κεφαλαία υπάρχουν στον κωδικό
            else if (Character.isUpperCase(ch)) {
                 capitalcaseCount++;
            }
            // μετράω πόσα μικρά γράμματα υπάρχουν στον κωδικό
            else if (Character.isLowerCase(ch)) {
                 lowercaseCount++;
            }  
        }
        
        // εξετάζω αν ο κωδικός έχει τουλάχιστον έναν αριθμό αν δεν έχει τον ενημερώνω για το
        if (numCount < 1) {
            System.out.println("Error: Password must have at least 1 number!");
            return false;
        }
        // εξετάζω αν ο κωδικός περιλαμβάνει τουλάχιστον 2 κεφαλαία γράμματα
        if (capitalcaseCount < 2) {
            System.out.println("Error: Password must have at least 2 capital case numbers!");
            return false;
        }
        // εξετάζω αν ο κωδικός περιλαμβάνει τουλάχιστον 3 πεζά γράμματα
        if (lowercaseCount < 3) {
            System.out.println("Error: Password must have at least 3 lower case numbers!");
            return false;
        }
        
        // αφού ο κωδικός είναι σύμφωνος με τα κριτήρια επιστρέφουμε το οκ
        return true;
    }


    public static boolean is_Numeric(char ch) {
        return (ch >= '0' && ch <= '9');
    }
    
}
