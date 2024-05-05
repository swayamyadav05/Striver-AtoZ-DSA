"""
Problem statement
Data type refers to the type of value a variable has and the way the computer interprets it.



Each data type has a different size. You’ve studied 5 different data types and the sizes of the data types:

Integer: 4 bytes
Long: 8 bytes
Float: 4 bytes
Double: 8 bytes
Character: 1 byte


You’re given a data type. Print its size in bytes.



Example :
Input: Long

Output: 8

Explanation: The size of a Long variable is given as 8 bytes.
"""

# def data_type_size(data_type):
#     sizes = {"Integer": 4, "Long": 8, "Float": 4, "Double": 8, "Character": 1}
#     return sizes.get(data_type, -1)


# # Example usage:
# input_data_type = input().strip()  # Remove leading/trailing whitespace from input
# print(data_type_size(input_data_type))


def dataTypes(type):
    if type == "Integer":
        return 4
    elif type == "Long":
        return 8
    elif type == "Float":
        return 4
    elif type == "Double":
        return 8
    elif type == "Character":
        return 1
    else:
        return -1


input_data_type = input()
result = dataTypes(input_data_type)
print(result)
