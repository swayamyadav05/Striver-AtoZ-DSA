/*Problem statement
Write a program that takes a character as input and prints 1, 0, or -1 according to the following rules.



1, if the character is an uppercase alphabet (A - Z).
0, if the character is a lowercase alphabet (a - z).
-1, if the character is not an alphabet.


Example:
Input: The character is 'a'.

Output: 0

Explanation: The input character is lowercase, so our answer is 0.
*/

#include <iostream>
using namespace std;

int character_check(char ch){
    if (ch >= 'A' && ch <= 'Z') {
        return 1;
    }
    else if (ch >= 'a' && ch <= 'z') {
        return 0;
    }
    else {
        return -1;
    }
}

int main() {
    char input_char;
    // cout << "Enter a character: ";
    cin >> input_char;

    int result = character_check(input_char);
    cout << result;
    
    return 0;
}