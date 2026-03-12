# parity
The number is an odd or an even integer?

```Python
me@amadeus:~$ python3 -q
>>> def check(n):
...     if not isinstance(n, int):
...             print(f"The value {n} is not an integer value")
...             return None
...     if n:
...             if n % 2 == 1:
...                     return (n, 'odd')
...             return (n, 'even')
...     return (n, 'undefined')
... 
>>> check(0)
(0, 'undefined')
>>> check(10)
(10, 'even')
>>> check(-10)
(-10, 'even')
>>> check(11)
(11, 'odd')
>>> check(-11)
(-11, 'odd')
>>> check(10.5)
The value 10.5 is not an integer value
>>> check(-11.5)
The value -11.5 is not an integer value
>>> check(-0)
(0, 'undefined')
>>> 
me@amadeus:~$ 
```
