/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package asksiseis;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class CreateTwoTables_2 {
    
    
    
    public static void main(String[] args) {
        // αρχικοποίηση πίνακα με ακεραίους
        int[] table_of_ints = {1, 2, 5, 6, 7, 10, 23, 32, 41};
        
        // δήλωση 2 array λιστών με ακέραιους μιας λίστας για τους ζυγούς και μίας για τους μονούς αριθμούς
        List<Integer> list_odd = new ArrayList<Integer>();
        List<Integer> list_even = new ArrayList<Integer>();
        
        // δήλωση βοηθητικής μεταβλητής
        int x;
        
        // μπαίνουμε σε επαναληπτικό βρόγχο
        for (int i = 0; i < table_of_ints.length; i++) {
            // εξετάζουμε ένα ένα τους ακεραίους του πίνακα
            x = table_of_ints[i];
            // ελέγχουμε αν ο ακέραιος είναι ζυγός και τον αποθηκεύουμε στην αντίστοιχη λίστα
            if ( (x & 1) == 0) {
                list_even.add(x);
            // ή αν είναι μονός και τον αποθηκεύουμε στην αντίστοιχη λίστα
            } else {
                list_odd.add(x);
            }
        }
        
        // μετατροπή των λιστών σε πίνακες
        
        // πρώτα για τους ζύγους
        // δηλώνω τον πίνακα με τους ζυγούς με το μέγεθος της λίστας των ζυγών
        int[] array_even = new int[list_even.size()];
        // μπαίνω σε βρόγχο
        for (int i = 0; i < list_even.size(); i++) {
            // βάζω τους ζυγούς αριθμούς από την λίστα των ζυγών στον πίνακα των ζυγών
            array_even[i] = list_even.get(i) ;
        }
        
        // για τους μονούς
        // δηλώνω τον πίνακα με τους μονούς με το μέγεθος της λίστας των μονών
        int[] array_odd = new int[list_odd.size()];
        // μπαίνω σε βρόγχο
        for (int i = 0; i < list_odd.size(); i++) {
            // βάζω τους μονούς αριθμούς από την λίστα των μονών στον πίνακα των μονών
            array_odd[i] = list_odd.get(i);
        }
        
        // εμφανίζω στον χρήστη τους 2 πίνακες
        System.out.println("Array with even numbers: " + Arrays.toString(array_even));
        System.out.println("Array with odd numbers: " + Arrays.toString(array_odd));
        
    }
}
