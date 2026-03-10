def check(n):
  if not isinstance(n, int):
    print(f"The number {n} is not an integer value")
    return
  if n:
    if n % 2 == 0:
      return (n, "even")
    else:
      return (n, "odd")
  else:
    return (n, "undefined")
    
