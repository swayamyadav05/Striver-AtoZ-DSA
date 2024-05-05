/*
Problem statement
Functions - Take this coding challenge to test your coding skills to



-define a function

-pass arguments by value to a function

-pass arguments by reference to a function



This coding challenge is organized in the following way:



First line of input reads an integer to select the coding challenge:



-Reading value '1' selects the coding-challenge 1 ( tests the ability to define a function and pass arguments by value.)



-Reading value '2' selects the coding challenge 2 (tests the ability to pass arguments by reference to a function)



Coding Challenge -1

Define a function named "Maximum" that accepts two integers (pass by value) as arguments and returns the greatest of the two arguments.



Coding Challenge -2

Define a function named "Swap" that accepts two integers (pass by reference) as arguments and swaps their value.
*/


#include <iostream>
using namespace std;
int Maximum(int x, int y)
{
	// Write your code here.
	if (x > y) return x;
	else return y;
}
void Swap(int &x, int &y)
{
	// Write your code here.
	int temp;
	temp = x;
	x = y;
	y = temp;
	// cout << x << " " << y;
}
int main()
{
	int test, a, b, r;
	cin >> test;
	cin >> a >> b;
	switch (test)
	{
	case 1:
		r = Maximum(a, b);
		cout << r;
		break;
	case 2:
		Swap(a, b);
		cout << a << " " << b;
		break;
	default:
		cout << "Invalid test option";
	}
	return 0;
}