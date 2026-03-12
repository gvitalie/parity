def check(n):
    if not isinstance(n, int):
        print(f"The value {n} is not an integer value")
        return None
    if not n: return (n, 'undefined')
    if n & 1: return (n, 'odd')
    return (n, 'even')


def check_(n):
    match n:
        case _ if not isinstance(n, int):
            print(f"The value {n} is not an integer value")
            return None
        case 0:
            return (n, 'undefined')
        case n if n % 2 == 1:  
            return (n, 'odd')
        case _:  
            return (n, 'even')
