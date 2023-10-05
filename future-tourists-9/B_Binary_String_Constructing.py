def fibonacci(n):
    """
    Calculates the Fibonacci sequence up to the given number.

    Parameters:
        n (int): The number up to which the Fibonacci sequence should be calculated.

    Returns:
        list: The Fibonacci sequence up to the given number.
    """
    fib_sequence = [0, 1]
    
    if n <= 1:
        return fib_sequence[:n+1]
    
    for i in range(2, n+1):
        fib_num = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(fib_num)
    
    return fib_sequence