# Pattern-1: Rectangular Star Pattern
def pattern1(n: int):
    for row in range(n):
        for col in range(n):
            print("*", end=" ")
        print()


# Pattern-2: Right-Angled Triangle Pattern
def pattern2(n: int):
    for row in range(n):
        for col in range(row + 1):
            print("*", end=" ")
        print()


# Pattern-3: Right-Angled Number Pyramid
def pattern3(n: int):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()


# Pattern - 4: Right-Angled Number Pyramid - II
def pattern4(n: int):
    for row in range(n):
        for col in range(row + 1):
            print(row + 1, end=" ")
        print()


# def pattern4(n: int):
#     for row in range(1, n + 1):
#         for col in range(i):
#             print(i, end=" ")
#         print()


# Pattern-5: Inverted Right Pyramid
def pattern5(n: int):
    for row in range(n):
        for col in range(n):
            if col < (n - row):
                print("*", end=" ")
        print()


# Pattern - 6: Inverted Numbered Right Pyramid
def pattern6(n: int):
    for row in range(n):
        for col in range(n):
            if col < (n - row):
                print(col + 1, end=" ")
        print()


# Pattern - 7: Star Pyramid
def pattern7(n: int):
    for row in range(n):
        for col in range(n - row - 1):
            print(" ", end="")
        for col in range(2 * row + 1):
            print("*", end="")
        print()


# Pattern - 7: Star Pyramid
def nStarTriangle(n: int) -> None:
    gap = n - 1
    stars = 1
    for row in range(n):
        for col in range(gap):
            print(" ", end="")
        for col in range(gap, gap + stars):
            print("*", end="")
        print()
        gap -= 1
        stars += 2


# Pattern - 8: Inverted Star Pyramid
def pattern8(n: int):
    for row in range(n):
        for col in range(row):
            print(" ", end="")
        for col in range(2 * (n - row) - 1):
            print("*", end="")
        print()


# Pattern - 8: Inverted Star Pyramid
def nStarTriangleReverse(n: int) -> None:
    gap = 0
    stars = 2 * n - 1
    for row in range(n):
        for col in range(gap):
            print(" ", end="")
        for col in range(gap, gap + stars):
            print("*", end="")
        print()
        gap += 1
        stars -= 2


# Pattern - 9: Diamond Star Pattern
def pattern9(n: int):
    pattern7(n)
    pattern8(n)


# Pattern - 10: Half Diamond Star Pattern
# def pattern10(n: int):
#     pattern2(n)
#     pattern5(n - 1)


def pattern10(n: int):
    for row in range(1, 2 * n):
        stars = row
        if row > n:
            stars = 2 * n - row
        for col in range(stars):
            print("* ", end="")
        print()


# Pattern - 11: Binary Number Triangle Pattern
def pattern11(n: int):
    start = 1
    for row in range(n):
        if row % 2 == 0:
            start = 1
        else:
            start = 0
        for col in range(row + 1):
            print(start, end=" ")
            start = 1 - start
        print()


# Pattern - 12: Number Crown Pattern
def pattern12(n: int):
    space = 2 * (n - 1)
    for row in range(1, n + 1):
        # Number
        for col in range(1, row + 1):
            print(col, end=" ")

        # Space
        for columns in range(1, space + 1):
            print(" ", end=" ")

        # Number
        for col in range(row, 0, -1):
            print(col, end=" ")

        print()
        space -= 2


# Pattern - 13: Increasing Number Triangle Pattern
def pattern13(n: int):
    num = 1
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(num, end=" ")
            num += 1
        print()


# Pattern-14: Increasing Letter Triangle Pattern
def pattern14(n: int):
    for row in range(n):
        for ch in range(row + 1):
            print(chr(ord("A") + ch), end=" ")
        print()


# Pattern-15: Reverse Letter Triangle Pattern
def pattern15(n: int):
    for row in range(n):
        for ch in range(n - row):
            print(chr(ord("A") + ch), end=" ")
        print()


# Pattern - 16: Alpha-Ramp Pattern
def pattern16(n: int):
    for row in range(n):
        for ch in range(row + 1):
            print(chr(ord("A") + row), end=" ")
        print()


# Pattern - 17: Alpha-Hill Pattern
def pattern17(n: int):
    for row in range(n):
        # Space
        for col in range(n - row - 1):
            print(" ", end=" ")

        # Character
        char = ord("A")
        breakpt = (2 * row + 1) / 2
        for col in range(1, row * 2 + 2):
            print(chr(char), end=" ")
            if col <= breakpt:
                char += 1
            else:
                char -= 1
        print()


# Pattern-18: Alpha-Triangle Pattern
def pattern18(n: int):
    char = ord("A") + n - 1
    for row in range(n):
        for col in range(row + 1):
            print(chr(char - col), end=" ")
        print()


# Pattern-18: Alpha-Triangle Pattern
def pattern18_1(n: int):
    char = ord("A") + n - 1
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print(chr(char - row + col), end=" ")
        print()


def pattern19(n: int):
    for row in range(n):
        # Stars
        for col in range(n - row):
            print("*", end=" ")
        # Space
        for col in range(row * 2):
            print(" ", end=" ")
        # Stars
        for col in range(n - row):
            print("*", end=" ")
        print()
    for row in range(n):
        # Stars
        for col in range(row + 1):
            print("*", end=" ")
        # Space
        for col in range((n - row) * 2 - 2):
            print(" ", end=" ")
        # Stars
        for col in range(row + 1):
            print("*", end=" ")
        print()


def pattern20(n: int):
    # For first 5 rows (first part)
    for row in range(n):
        # Stars
        for col in range(row + 1):
            print("*", end=" ")
        # Space
        for col in range((n - row) * 2 - 2):
            print(" ", end=" ")
        # Stars
        for col in range(row + 1):
            print("*", end=" ")
        print()
    # For rest 4 rows i.e., 5 - 1 rows (second part)
    for row in range(n - 1):
        for col in range(row, n - 1):
            print("*", end=" ")
        for col in range(row * 2 + 2):
            print(" ", end=" ")
        for col in range(row, n - 1):
            print("*", end=" ")
        print()


def pattern21(n: int):
    for row in range(n):
        for col in range(n):
            if row == 0 or row == n - 1 or col == 0 or col == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def pattern22(n: int):
    for row in range(2 * n - 1):
        for col in range(2 * n - 1):
            top = row
            left = col
            right = (2 * n - 2) - col
            down = (2 * n - 2) - row
            print(n - min(min(top, down), min(left, right)), end=" ")
        print()


n = int(input("Enter size: "))

pattern1(n)
print()

pattern2(n)
print()

pattern3(n)
print()

pattern4(n)
print()

pattern5(n)
print()

pattern6(n)
print()

pattern7(n)
print()

nStarTriangle(n)
print()

pattern8(n)
print()

nStarTriangleReverse(n)
print()

pattern9(n)
print()

pattern10(n)
print()

pattern11(n)
print()

pattern12(n)
print()

pattern13(n)
print()

pattern14(n)
print()

pattern15(n)
print()

pattern16(n)
print()

pattern17(n)
print()

pattern18(n)
print()

pattern18_1(n)
print()

pattern19(n)
print()

pattern20(n)
print()

pattern21(n)
print()

pattern22(n)
print()
