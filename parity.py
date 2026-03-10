def parity(n):
  if not isinstance(n, int):
    print("The number is not an integer value")
    return
  if n:
    if n % 2 == 0:
      return (n, "even")
    else:
      return (n, "odd")
  else:
    return (n, "undefined")
    
