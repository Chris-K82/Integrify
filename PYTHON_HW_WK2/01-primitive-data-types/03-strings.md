---
title: 03 - Strings
root: '/modules/module-1/module-1-1-primitive-data-types'
tree: '01 - Python Basics|01 - Primitive data types'
module: module-1
---

# 03. Strings and string formatting

Strings are the second stop in our journey through the _primitive_ data-types in Python, so let's dig in.

```bash
# lets declare our variable per as usual
>>> our_string = "This is going to awesome!"
```

Note that the variable is now enclosed between _quotes_. Python doesn't care if we use single (`'`) or double (`"`) quotes but for clarity & consistency => we're going to use double quotes from now on.

What would happen if we try to "add" something to our variable?

```bash
>>> print(our_string + 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
```

Python is smart enough to figure out we're trying to mix two different types and responds by throwing an error.

Let's try again with corrected type:

```bash
>>> print(our_string + str(1)) # str(1) means, that we're casting number one as a string.
This is going to awesome!1
```

This is called _string concatination_ and will be used very often in the near future when we're dealing more with data. Also, there's more about strings in the coming module.

Let's see a couple more concatination methods Python offers. First one is by using `%`-operator:

```bash
>>> second_string = "And beyond." # Let's declare another variable...
>>> print("%s %s" % (our_string, second_string)) # ...and print out the result of the concatenation
This is going to awesome! And beyond.
```

As can be seen from the above, Python is replacing the placeholders `%s` inside the quotes with variables listed within the brackets in the same order. Note, that there always needs to be equal number of placeholders and variables. If not => we get greeted by an error:

```bash
>>> print("%s %s" % (our_string, second_string, "foobar"))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: not all arguments converted during string formatting
```

Another way to deal with strings is by using `.format()` method of a string (variable `our_string` is a string-type which has a builtin methods). The `.format()` method has similarities with `%`-operator but is more flexible:

```bash
>>> print("{} {}".format(our_string, second_string))
This is going to awesome! And beyond.
```

Above the `.format()` works just like `%`-operator by replacing `{}` placeholders with variables within the brackets in the same order. What if we'd like the change the order? `.format()` gives a simple way of doing this by simply:

```bash
>>> print("{1} {0}".format(our_string, second_string))
And beyond. This is going to awesome!
```

Above we just had to give a corresponding index-number inside the placeholder and Python is smart enough to replace the first placeholder with the second variable inside the branckets and the second with the first! By default there's no need to define the index-number but if for some reason it seems necessary => it's possible.

Again, it doesn't matter which one to use but for consistency => we're going to go with the latter.
