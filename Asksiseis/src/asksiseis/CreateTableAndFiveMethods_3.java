/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package asksiseis;

import static java.lang.Integer.sum;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class CreateTableAndFiveMethods_3 {
    
    
    public static void main(String[] args) {
        int[] table_of_ints = {1, -2, 43, 6, -15, 10, 25, 342};
        printTable(table_of_ints);
        printTableReverse(table_of_ints);
        printTableSum(table_of_ints);
        printTableSmallerNumbers(table_of_ints);
        printTableBiggerNumbers(table_of_ints);
    }
    
    
    
    // εμφάνιση στοιχείων του πίνακα
    public static void printTable(int [] table_of_ints) {
            System.out.println("Array with numbers: " + Arrays.toString(table_of_ints));
    }
    
    // εμφάνιση στοιχείων του πίνακα με αντίστροφη σειρά 
    public static void printTableReverse(int [] rev_table_of_ints) {
            // μπαίνω σε επαναληπτικό βρόγχο
            for(int i = 0; i < rev_table_of_ints.length / 2; i++)
            {
                // με τις 3 ακόλουθες εντολές αλλάζω τα αντικείμενα του πίνακα 
                // μέχρι να φτάσω στο μεσαίο σημείο 
                int temp = rev_table_of_ints[i];
                rev_table_of_ints[i] = rev_table_of_ints[rev_table_of_ints.length - i - 1];
                rev_table_of_ints[rev_table_of_ints.length - i - 1] = temp;
            }
            // εμγανίζω τα στοιχεία του πίνακα με αντίστροφη σειρά
            System.out.println("Flipped Array: " + Arrays.toString(rev_table_of_ints));
    }
    
    // υπολογισμός και εμφάνιση αθροίσματος στοιχείων του πίνακα
    public static void printTableSum(int [] sum_table_of_ints) {
        // δήλωση και αρχικοποίηση αθροιστή 
        int sum = 0; 
        // μπαίνω σε επαναληπτικό βρόγχο. γραμμένος με εναλακτικό τρόπο
        for (int value : sum_table_of_ints) {
           // αθροίζω τα στοιχεία
           sum += value;
        }
        // εμφανίζω το άθροισμα των στοιχείων του πίνακα
        System.out.println("Sum of array numbers: " + sum);
    }
    
    public static void printTableSmallerNumbers(int [] s_table_of_ints) {
            // δήλωση 1 array λίστας με ακέραιους για τους μικρότερους αριθμούς
            List<Integer> list_smaller = new ArrayList<Integer>();
            // χρησιμοποιώ την κλάση Scanner για να διαβάσω από τον χρήστη τον αριθμό
            Scanner input = new Scanner(System.in);
            // προτρέπω τον χρήστη να εισάγει έναν αριθμό
            System.out.print("Please, input a number: ");
            // Διαβάζω από τον χρήστη τον αριθμό για να βρω ποιοί αριθμοί είναι μικρότεροι       
            String s = input.nextLine();
            // μπαίνω στον βρόγχο
            for (int i = 0; i <  s_table_of_ints.length; i++) {
                // ελέγχω αν ο αριθμός είναι μικρότερος από τον αριθμό που έχει  
                // εισάγει ο χρήστης και αν είναι τον αποθηκεύω
                if (s_table_of_ints[i] < Integer.parseInt(s)){
                    list_smaller.add(s_table_of_ints[i]);
                }
            }
            // εμφάνιση αριθμών πίνακα που είναι μικρότεροι από τον αριθμό που έχει εισάγει ο χρήστης 
            System.out.println("Smaller array numbers from the number you entered: " + Arrays.toString(list_smaller.toArray()));
    }
   
    public static void printTableBiggerNumbers(int [] b_table_of_ints) {
            // δήλωση 1 array λίστας με ακέραιους για τους μεγαλύτερους αριθμούς
            List<Integer> list_bigger = new ArrayList<Integer>();
            // χρησιμοποιώ την κλάση Scanner για να διαβάσω από τον χρήστη τον αριθμό
            Scanner input = new Scanner(System.in);
            // προτρέπω τον χρήστη να εισάγει έναν αριθμό
            System.out.print("Please, input a number: ");
            // Διαβάζω από τον χρήστη τον αριθμό για να βρω ποιοί αριθμοί είναι μεγαλύτεροι        
            String b = input.nextLine();
            // μπαίνω στον βρόγχο
            for (int i = 0; i <  b_table_of_ints.length; i++) {
                // ελέγχω αν ο αριθμός είναι μεγαλύτερος από τον αριθμό που έχει  
                // εισάγει ο χρήστης και αν είναι τον αποθηκεύω
                if (b_table_of_ints[i] > Integer.parseInt(b)){
                    list_bigger.add(b_table_of_ints[i]);
                }
            }
            // εμφάνιση αριθμών πίνακα που είναι μεγαλύτεροι από τον αριθμό που έχει εισάγει ο χρήστης 
            System.out.println("Bigger array numbers from the number you entered: " + Arrays.toString(list_bigger.toArray()));
    }
    
}
