---
title: 01 - Lists
root: '/modules/module-1/module-1-2-non-primitive-data-types'
tree: '01 - Python Basics|02 - Non-primitive data types'
module: module-1
---

# 01. Lists

In our previous section we talked about _types_ and _variables_ and how to assign values to them. Now it's time to say hello to `list` - a _sequential_ datatype which is propably one of the most powerful and versatily of the types Python has to offer.

Sequential means we can assign multiple values to single variable by adding a comma-separated sequence of items inside square-brackets:

```bash
our_list = ["first", "second", "third"]
```

Above we assigned three _string_ types to `our_list`-variable.

Items of a list dont't need to be the same type:

```bash
our_second_list = [1, "second", 3.0, False]
```

If we now print them out, we can see that the forms are not that useful:

```bash
>>> print(our_list, our_second_list) # Oh, we can print multiple variables within one print-function by separating them with comma
['first', 'second', 'third'] [1, 'second', 3.0, False]
```

The english translation of `our_list` is _"The first item with zeroeth index is 'first', second item with index 1 is 'second', the third item with index 2 is 'third'"_ and `our_second_list` is something like "The first item with zeroath index is 1, second item with index 1 is 'second', third item with index 2 is 3.0 and fourth item with index 3 is False". List stores items with zero-index which means the counting starts at 0.


## Accessing list items

Picking out a single item from a list can be done by printing out the variable followed by the _index_ of the item inside square brackets:

```bash
>>> print(our_list[2]) # This prints out the index 2 (third) item
third
```

Picking a _range_ from a list is done by giving a _start index_ and an _end index_ separated by colon:

```bash
>>> print(our_second_list[1:3])
['second', 3.0]
```

Picking the last item means we're giving an _negative index_ so the counting will start from the end and goes towards the start:

```bash
>>> print(our_second_list[-1])
False
```

What about getting every second element starting from index 2 and ending in 10?

```bash
# Let's create a list with more items in it
>>> bigger_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
>>> print(bigger_list[2:10:2])
[3, 5, 7, 9]
```

The only difference from getting a range is introducing a new colon-separated integer which represents a _step_.

In the previous example we defined start and end indexes. What if we simply want to get every second element of a list, from start till the end?

```bash
>>> print(bigger_list[::2])
[1, 3, 5, 7, 9, 11, 13]
```

It works just by omitting the start and end indexes! We can omit any of the three (start index, end index, step) and Python will automatically use the default:

```bash
>>> print(bigger_list[:10:2]) # End in index 10. The start is by default 0.
[1, 3, 5, 7, 9]
>>> print(bigger_list[1::2]) # Start from index 1. The end is by default the last item.
[2, 4, 6, 8, 10, 12]
```

## List methods

Adding items to list:

```bash
>>> bigger_list.append(14) # Appends the item to the end of the list
>>> print(bigger_list)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
```

Inserting item at a given index:

```bash
>>> bigger_list.insert(0, 0) # insert integer 0 to the zeroeth index
>>> print(bigger_list)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
```

Reversing the order:

```bash
>>> bigger_list.reverse()
>>> print(bigger_list)
[14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

Remove item:

```bash
>>> bigger_list.remove(14)
>>> print(bigger_list)
[13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

Sorting the values:

```bash
>>> bigger_list.sort()
>>> print(bigger_list)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
```

Checking if some item exists in list:

```bash
>>> print(13 in bigger_list)
True
```

Concatinating two lists:

```bash
>>> huge_list = bigger_list + our_list
>>> print(huge_list)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'first', 'second', 'third']
```

There's still many more things we can do with lists, but will focus on those a bit later.

**NOTE!** Lists are propably the most powerful feature of Python in Data-science context so it's highly important we know lists by heart!
