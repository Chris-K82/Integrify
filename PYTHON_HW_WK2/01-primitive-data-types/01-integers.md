---
title: 01 - Integers
root: '/modules/module-1/module-1-1-primitive-data-types'
tree: '01 - Python Basics|01 - Primitive data types'
module: module-1
---

# 01. Integers

In Python you declare a _variable_ by giving it a _meaningful_ name with letters and underscores. A variable can hold any _type_ of data and in this example we'll be focusing on Integers.

Open up your console and write `python` which will open the Python `REPL` (Read Evaluate Print Loop, interactive command shell). You should see something like:

```bash
Python 3.6.7
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.46.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Let's create our first variable and assign a value of `10` to it by writing to the REPL:

```python
our_first_variable = 6
```

Our variable is there even thought it cannot be seen yet. Let's fix this by _printing_ it to the screen:

```python
print(our_first_variable)
```

...and we'll observe

```bash
>>> print(our_first_variable)
6
```

Congratulations, our first application is done!

You can now add a _"Python unicorn"_ to your LinkedIn profile & apply for a job at the fanciest consulting agencies which brew their own coffee from soy beans and create _valuable solutions to their customers_.

Ok, let's get back to reality and learn a couple more tricks which will help us during the negotiations.

Let's create a second variable so we can test some of the _arithmetic_ operators in Python.

```python
our_second_variable = 9
```

### Addition

Can you guess the output of

```python
our_first_variable + our_second_variable
```

?

No, unfortunately it's not `69`, because we're not _concatenating_ the variables but instead doing a basic addition so it'll be approximately:

```python
>>> our_first_variable + our_second_variable
15
```

### Subtraction

Ok, so what about

```python
our_first_variable - our_second_variable
```

?

Yes, correct. It's `-3`.

### Multiplication

The multiplication goes the same way:

```python
our_first_variable * our_second_variable
```

And the result is the expected `54`

### Division

Division follows the same pattern and won't give us any surprises:

```python
our_first_variable / our_second_variable
```

```python
>>> 0.6666666666666666
```

### Modulus

Modulus is propably the first "odd" operator as it returns remainder of the division:

```python
our_second_variable % our_first_variable
```

```python
>>> 3
```

So, after the `9` gets divided by `6`, the remainder of the calculation is the _modulus_. Easy, right?

### Exponent

Exponent is declared with two _multiplication_ (asterisks) operators:

```python
our_first_variable ** our_second_variable
```

```python
>>> 10077696
```


## Congratulations!

We've scratched the surface of Python variables, operators and integers. We now know how to declare, print and change variables inside the Python REPL. You can now shut the REPL by pressing `Ctrl + D`.
