---
title: 02 - Floats
root: '/modules/module-1/module-1-1-primitive-data-types'
tree: '01 - Python Basics|01 - Primitive data types'
module: module-1
---

# 02. Floats

Now that we've decided to go "all-in" on learning Python, it's time to actually crunch the numbers so let's introduce ourselves to the _fractional_ part of the magigal thing called _Math_:

## Floats

```python
# Our variable is this
#
# ...and oh! This is a comment. It's something we write as a note to outself & to our successor as a guideline how to actually read our code...
float_var = 0.513513
```

Now we can check the type of our variable by typing:

```bash
>>> type(float_var)
```

which confirms that we're dealing with a `float`-type. `type()` is a _builtin_ function in Python. We'll discuss about builtins a little later.

```bash
>>> type(float_var)
<class 'float'>
```

We can use the same _arithmetic_ operators with `floats` as with `integers`:

```bash
>>> float_var + 12
12.513513
>>> float_var - 0.1
0.413513
>>> float_var * 2
1.027026
>>> float_var / 2
0.2567565
>>> float_var ** 2
0.263695601169
>>> float_var % 2
0.513513
```

Let's introduce a second _builtin_: `round()`. As we've might suspected, the `round()` function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.

The default number of decimals is 0, meaning that the function will return the nearest integer:

```bash
>>> round(float_var)
1
```

If we specify a number of decimals, we get a different result:

```bash
>>> round(float_var, 2)
0.51
```

We can also use _builtin_ `float()` & `int()`-functions to convert different types:

```bash
>>> int(1.23) # convert a floating point number 1.23 to integer
1
>>> float(24) # convert an integer 24 to float
24.0
>>> float(1.1234) # convert float to float. This is redundand as the parameter is already a floating point number.
1.1234
```
