def check(n):
    if not isinstance(n, int):
        print(f"The value {n} is not an integer value")
        return None
    if n:
        if n % 2 == 1: 
            return (n, 'odd')
        return (n, 'even')
    return (n, 'undefined')
