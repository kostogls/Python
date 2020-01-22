""" An Armstrong number is a number that is equal to the sum of the cubes of its digits.
For example, 370 is an Armstrong number because 3*3*3 + 7*7*7 + 0*0*0 = 370.
An Armstrong number is often called Narcissistic number.
"""


def armstrong_number(n):
    """
        This function checks if a number is Armstrong or not.

        >>> armstrong_number(153)
        153 is an Armstrong number
        >>> armstrong_number(200)
        200 is not an Armstrong number
        >>> armstrong_number(1634)
        1634 is an Armstrong number
        """
    # Initialization of sum and number of digits.
    sum = 0
    number_of_digits = 0
    temp = n
    # Calculation of digits of the number
    while temp > 0:
        number_of_digits += 1
        temp //= 10
    # Dividing number into separate digits and find Armstrong number
    temp = n
    while temp > 0:
        rem = temp % 10
        sum = sum + (rem ** number_of_digits)
        temp //= 10
    if n == sum:
        print(n, "is an Armstrong number")
    else:
        print(n, "is not an Armstrong number")


# In main function user inputs a number to find out if it's an Armstrong or not. Th function armstrong_number is called.
def main():
    num = int(input("Enter a number to check if it is Armstrong or not: ").strip())
    armstrong_number(num)


if __name__ == '__main__':
    main()
    import doctest

    doctest.testmod()
