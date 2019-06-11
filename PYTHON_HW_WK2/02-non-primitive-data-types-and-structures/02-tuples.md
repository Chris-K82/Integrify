---
title: 02 - Tuples
root: '/modules/module-1/module-1-2-non-primitive-data-types'
tree: '01 - Python Basics|02 - Non-primitive data types'
module: module-1
---

# 02. Tuples

In previous chapter we deald with _lists_. Tuples are pretty similar with lists and the main differences are that tuples are _immutable_ (which mean they cannot be changed) and tuples use parenthesis.

Let's dig in!

```bash
our_tuple = ("first", "second", "third")
```

Above we declared a variable of type tuple. We can get a single value from the variable like we would do with lists: By _bracket-notation_:

```bash
>>> our_tuple[1]
'second'
```

As said before: Tuples are immutable so what would happen if we try to change a value inside the tuple?

```bash
>>> our_tuple[1] = "another"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Python greet us with error which confirms that Tuple is indeed immutable. But, how do we update a value in tuple then? Answer: We don't. We always create a new tuple instead of updating ones value. That's the price of immutability.

We can use the exact same methods on accessing tuple items, picking out a range etc. as we did with lists. That's the reason we need to know lists by heart!

Tuples can be created also without parentheses but from now on we'll always use parentheses for the sake of clarity.

## Functions and methods

Lists can be converted to tuples by using builtin `tuple`-function:

```bash
>>> our_list = ["first", "second", "third"]
>>> our_tuple = tuple(our_list)
>>> type(our_tuple)
<class 'tuple'>
```

Tuples can be seen as "things we can trust" because they're not going to change by accident.
