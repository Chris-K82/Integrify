---
title: 04 - Sets
root: '/modules/module-1/module-1-2-non-primitive-data-types'
tree: '01 - Python Basics|02 - Non-primitive data types'
module: module-1
---

# 04. Sets

_Sets_ in Python are data structure similar to _list_. Biggest difference being sets only contain _unique values_. Sets are also unordered, which means we cannot access a single element of a set by giving an index.

Set can contain any _immutable_ (non-changeable) data type: a number, a string, a tuple. Notice also that another set cannot be an element of a set.

Let's dig in:

Sets can be created by using either the `set`-function and giving it a _list_ as an argument:

```bash
>>> our_set = set(["first", "second", "third", "third", "fourth"])
```

or by using curly-braces:

```bash
>>> our_set = {"first", "second", "third", "third", "fourth"}
```

Notice how we accidentally added twice the _"third"_-string? No worries, as said before the sets contain only unique values:

```bash
>>> print(our_set)
{'first', 'second', 'fourth', 'third'}
```

Duplicates were removed. This will be highly useful in our future endeavours.

## Set methods

**Add single to set:**

```bash
>>> our_set.add("fifth")
>>> print(our_set)
{'fifth', 'fourth', 'second', 'first', 'third'}
```

**Adding multiple items to set:**

```bash
>>> our_set.update(['sixth', 'seventh']) # Update accepts lists...
>>> our_set.update({'eight', 'ninth'}) # ...and sets
>>> print(our_set)
{'eight', 'ninth', 'fifth', 'fourth', 'sixth', 'seventh', 'second', 'first', 'third'}
```

**Removing items from a set:**

```bash
>>> our_set.remove("fifth")
>>> print(our_set)
{'eight', 'ninth', 'fourth', 'sixth', 'seventh', 'second', 'first', 'third'}
```

If the item is not present, the `remove()`-method will throw an error:

```bash
>>> our_set.remove("fifth")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'fifth'
```

So it's better to use `discard()` instead which will remove the item if present and dismiss if not found:

```bash
>>> our_set.discard("fifth")
>>> print(our_set)
{'eight', 'ninth', 'fourth', 'sixth', 'seventh', 'second', 'first', 'third'}
```

**Set union**:

Unionizing two sets:

```bash
>>> a_set = {1, 2, 3, 4}
>>> b_set = {5, 6, 7, 8}
>>> print(a_set.union(b_set))
{1, 2, 3, 4, 5, 6, 7, 8}
```

**Set intersection**

Getting common element from two sets:

```bash
>>> a_set = {1, 2, 3, 4}
>>> b_set = {3, 4, 5, 6}
>>> print(a_set.intersection(b_set))
{3, 4}
```

**Set difference**

Getting non-common element from two sets:

```bash
>>> a_set = {1, 2, 3, 4}
>>> b_set = {3, 4, 5, 6}
>>> print(a_set.difference(b_set))
{1, 2}
```

**Set symmetric Difference**

Getting elements in both sets except those that are present in both:

```bash
>>> a_set = {1, 2, 3, 4, 5}
>>> b_set = {3, 4, 5, 6, 7}
>>> print(a_set.symmetric_difference(b_set))
{1, 2, 6, 7}
```

That's it. Now we know almost everything (being sarcastic here...) about python data-types and it's time to move on to _control structures_.
