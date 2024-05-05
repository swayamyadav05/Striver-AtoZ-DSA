"""
Problem statement
Programming languages have some conditional / decision-making statements that execute when some specific condition is fulfilled.



Switch-case is one of the ways to implement them.



In a menu-driven program, the user is given a set of choices of things to do (the menu) and then is asked to select a menu item.



There are 2 choices in the menu:



Choice 1 is to find the area of a circle having radius 'r'.

Choice 2 is to find the area of a rectangle having dimensions 'l' and 'b'.



You are given the choice 'ch' and an array 'a'.



If 'ch' is 1, 'a' contains a single number 'r'. If 'ch' is 2, 'a' contains 2 numbers, 'l' and 'b'.



Consider the choice and print the appropriate area.



Example :
Input: 'ch' = 2 and 'a' = [3, 2]

Output: area = 6

Explanation: Since the choice 'ch' is 2, we have to print the area of the rectangle having 'l' = 3 and 'b' = 2, which is 6.
"""


def areaMatchCase(ch: int, a: list[float]):
    match ch:
        case 1:
            r = a
            area = 3.14 * r**2
            print(area)
        case 2:
            l, b = a
            area = l * b
            print(area)
        case _:
            print("Invalid choice")


ch = int(input("Enter choice: "))
a = list(map(float, input("Enter dimension/s: ").split(",")))

areaMatchCase(ch, a)
