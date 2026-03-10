# parity
The number is an odd or an even integer?

```Python
me@amadeus:~$ python3 -q
>>> def parity(n):
...     if not isinstance(n, int):
...             print("The number is not an integer value")
...             return
...     if n:
...             if n % 2 == 0:
...                     return (n, 'even')
...             else:
...                     return (n, 'odd')
...     else:
...             return (n, 'undefined')
... 
>>> parity(0)
(0, 'undefined')
>>> parity(-10)
(-10, 'even')
>>> parity(10)
(10, 'even')
>>> parity(11)
(11, 'odd')
>>> parity(-11)
(-11, 'odd')
>>> parity(-11.5)
The number is not an integer value
>>> parity(10.5)
The number is not an integer value
>>> parity(-0)
(0, 'undefined')
>>> 
me@amadeus:~$ 
```
