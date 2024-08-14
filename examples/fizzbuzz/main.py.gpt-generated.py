@auto('\nReturn fizz if the number is divisible by 3, buzz if the number is divisible by 5, \nand fizzbuzz if the number is divisible by both 3 and 5. Otherwise, just return\nthe number itself.\n')
def fizzbuzz(n: int) -> str:
    """
    Returns 'fizz' if the number is divisible by 3, 'buzz' if the number is divisible by 5, 
    and 'fizzbuzz' if the number is divisible by both 3 and 5. Otherwise, returns the number itself.
    
    Args:
        n (int): The number to evaluate.

    Returns:
        str: The result of the FizzBuzz logic.
    """
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    else:
        return str(n)


