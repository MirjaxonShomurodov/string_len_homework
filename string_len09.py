def main(num1, num2):
    """
    Given two non-negative integers, num1 and num2 represented as string.
    Return the sum of num1 and num2 as a string.

    Args:
        num1: str
        num2: str
    Returns:
        str: answer
    """
    num1=3
    num2=4
    s="{}+{}={}".format(num1,num2, num1+num2)
    return s
print(main(3,4))