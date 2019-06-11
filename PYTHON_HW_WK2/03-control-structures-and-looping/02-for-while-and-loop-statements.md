---
title: 02 - For, While
root: '/modules/module-1/module-1-3-control-structures'
tree: '01 - Python Basics|03 - Control structures'
module: module-1
---

# 02. For, While and loop statements

_Looping_ in programming means executing a statement `n` times. Python offers basically a two loop-types:

**`while`**

> Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body.

**`for`**

> Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.

## For

```bash
>>> our_list = [1, 2, 3, 4, 5]
>>> for i in our_list: # translates to "For i as current item in our list do stuff"
...     print(i) # i is a variable and commonly used as i in iterations
1
2
3
4
5
```

Above we _iterated_ through every item in our list and printed out the current item.

```bash
>>> our_list = ["one", "two", "three", "four", "five"]
>>> for num in our_list:
...     print(num)
one
two
three
four
five
```

As can be seen, the iterable (_list_ in the example above) can contain any values and `i` doesn't always need to be called `i`.

Let's declare a dictionary for a bit more sophisticated examples:

```bash
>>> our_dict = {"key_1": "value_1", "key_2": "value_2", "key_3"}
```

Dicts can be iterated by `keys`:

```bash
>>> for key in our_dict.keys():
...     print(key)
...
key_1
key_2
key_3
key_4
key_5
```

Or by `values`:

```bash
>>> for val in our_dict.values():
...     print(val)
...
value_1
value_2
value_3
value_4
value_5
```

Or by both:

```bash
>>> for k, v in our_dict.items():
...     print("Key {} has a value {}".format(k, v))
...
Key key_1 has a value value_1
Key key_2 has a value value_2
Key key_3 has a value value_3
Key key_4 has a value value_4
Key key_5 has a value value_5
```

### list comprehension

List comprehensions provide a concise way to create lists on a one-liner. Let's have an example:

```bash
# instead of doing this...
>>> for i in range(5):
...     new_list.append(i)

# ...we can shorten the list creation to a one-liner: Take each item from the for-loop and append it to our variable using bracket-notation
>>> new_list = [i for i in range(5)]

# Conditional example
>>> for i in range(5):
...     if i % 2 == 0:
...         new_list.append(i)

# Take only the even numbers from the range
>>> new_list = [i for i in range(5) if i % 2 == 0]
```

List comprehension syntax follows patter `[expression for i in iterable [if condition]` which means we can do pretty much everything within the expression.

Let's have another example with the `expression` part in mind:

```bash
# Take only the even numbers from the range and multiply them by two
>>> new_list = [i * 2 for i in range(5) if i % 2 == 0]
```

Same kind of comprehension can be used with `dicts` also:

```bash
>>> our_dict = {1: "value_1", 2: "value_2", 3: "value_3", 4: "value_4", 5: "value_5"}
>>> new_list = [v for k, v in our_dict.item()] # create a list from dict values
>>> new_list = [v for k, v in our_dict.item() if k % 2 == 0] # create a list from dict values if key is even number
```

We can even create a `dict` using the same form of comprehension:

```bash
>>> our_dict = {1: "value_1", 2: "value_2", 3: "value_3", 4: "value_4", 5: "value_5"}
>>> new_dict = {k:v for k, v in our_dict.items() if k % 2 == 0} # create a dict if key is even number
```

## While

While loops repeat as long as a certain boolean condition is met, so beware **not** to create an _infinite loop_!

```bash
>>> current_count = 0 # declare a variable with value 0
>>> while current_count < 5: # Loop until current_count is no more smaller than 5
...     print("Current count is {}".format(current_count))
...     current_count += 1 # increment current_count in each iteration. Highly important as otherwise we'll create the infamous infinite loop and never get out of the office :(
...
Current count is 0
Current count is 1
Current count is 2
Current count is 3
Current count is 4
```

## Loop statements

Sometimes it's redundand to loop over all items and that's where loop statements will help us.

**break**

Break is used to exit the loop under some circumstances:

```bash
>>> for i in range(5):
...     print(i)
...     if i == 3:
...         print("Exiting at {}...".format(i))
...         break
0
1
2
3
Exiting at 3...
```

**continue**

Continue skips the current iteration-block:

```bash
>>> for i in range(5):
...     if i == 3:
...             continue # let's skip if we're at three
...     print(i)
...
0
1
2
4
```

If lists were the most important part in the basics, the looping techniques will definitely come in second!
