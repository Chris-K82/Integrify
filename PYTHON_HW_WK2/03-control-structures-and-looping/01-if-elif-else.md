---
title: 01 - If, Elif, Else
root: '/modules/module-1/module-1-3-control-structures'
tree: '01 - Python Basics|03 - Control structures'
module: module-1
---

# 01. If, Elif, Else

Remember booleans from part _Primitive data types_? If, elif and else all require a boolean to deal with. Python offers six logical comparators:

* Equals: a == b
* Not Equals: a != b
* Less than: a < b
* Less than or equal to: a <= b
* Greater than: a > b
* Greater than or equal to: a >= b

What to do with these operators then? They basically execute code if the logic is _true_:

```bash
>>> if 1 > 0:
...     print("It's greater")
... else:
...     print("It's not greater")
...
It's greater
```

Above translates to: "If number one is greater than number zero (as it usually is...) => print out _It's greater_, otherwise print out _It's not greater_".

Easy, right?

Let's have some more logical example with _list_:

```bash
>>> snatch_list = ["I", "like", "dags"]
>>> if "dags" in snatch_list: # if string "dags" is included in the list
...     print("He likes dags!")
... else:
...     print("He must like cats then")
...
He likes dags!
```

```bash
>>> number_one = 1
>>> number_two = 2
>>> if number_one > number_two
...     print("Somehow 1 is greater than 2")
... else:
...     print("As expected: 1 is smaller than 2")
...
As expected: 1 is smaller than 2
```

## Elif

`Elif` extends if and else to have more than just one logical comparison:

```bash
>>> number_one = 1
>>> number_two = 2
>>> if number_one > number_two
...     print("Somehow 1 is greater than 2")
... elif number_one != 0:
...     print("Number 1 does definitely not equal to number 0. That's why we return early here")
... else:
...     print("As expected: 1 is smaller than 2")
...
Number 1 does definitely not equal to number 0. That's why we return early here
```

## And, Or

Python offers also a couple more keywords to test logic: `and` and `or`:

```bash
>>> if 1 > 0 and True:
...     print("It's greater")
... else:
...     print("It's not greater")
...
It's greater
```

Above didn't offer that much, we just checked if number 1 is greater than zero AND the second comparison was also True.

```bash
>>> number_one = 1
>>> number_two = 2
>>> if number_one > 0 or number_two == 2:
...     print("1 is greater than 0 and number_two equals to 2")
... else:
...     print("Something weird happened...")
...
1 is greater than 0 and number_two equals to 2
```

Above could be also simplified to a "one-liner":

```bash
>>> number_one = 1
>>> number_two = 2
>>> print("1 is greater than 0 and number_two equals to 2") if number_one > 0 or number_two == 2 else print("Something weird happened...")
1 is greater than 0 and number_two equals to 2
```

A good rule of thumb in one-liners is, that if the condition is simple and easy to read (and it really makes sense to use a one-liner) => use it. We should always think of the developer-experince when writing code!

We've now don with the basics of if, elif and else and there's plenty of these in the future so let's keep them in mind!
