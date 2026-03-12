def check(n):
    match n:
        case _ if not isinstance(n, int):
            print(f"The value {n} is not an integer value")
            return
        case n if n % 2 == 1:
            return (n, 'odd')
        case n if n % 2 == 0:
            return (n, 'even')
        case 0:
            return (n, 'undefined')
