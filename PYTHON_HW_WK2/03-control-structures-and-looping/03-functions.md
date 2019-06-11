---
title: 03 - Functions
root: '/modules/module-1/module-1-3-control-structures'
tree: '01 - Python Basics|03 - Control structures'
module: module-1
---

# 03. Functions

The last part in our "basics of Python" deals with _functions_. We've introduced ourselves with the _builtins_ a few modules backbut now it's time to create some functions of our own.

## the most basic example

```bash
>>> def print_hello_world():
...     print("Hello, world!")
>>> hello_world() # let's call our newly created function and see what it does...
Hello, world!
```

The above function simply prints out "Hello, world!" and does not _return_ anything - it's called a _void_. Usually functions return something, so let's refactor the function to return the string instead of printing it:

```bash
>>> def hello_world():
...     return "Hello, world!"
>>> print(hello_world()) # Print out the returned value of the function
Hello, world!
```

## parameters

Functions usually digest some arguments and return values based on them:

```bash
>>> def greet(name):
...     return "Hello, {}!".format(name)
>>> print(greet("John Doe"))
Hello, John Doe!
```

What if we _don't_ pass the argument? Well...


```bash
>>> print(greet())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: greet() missing 1 required positional argument: 'name'
>>>
```

Solution to this is to use _default arguments_:

```bash
>>> def greet(name="Some Name"):
...     return "Hello, {}!".format(name)
>>> print(greet())
Hello, Some Name!
```

## *args and **kwargs

Propably the hardest part to figure out in functions are `*args` and `**kwargs`. To put simple: `*args` and `**kwargs` allow us to pass a variable number of arguments to a function. What this means in practise?

### *args

`*args` is a _non-keyworded_ variable length argument list:

```bash
>>> def args_fun(*args):
...     return "We passed {} arguments to the function!".format(len(args))
>>> args_fun("one", 2, "third")
'We passed 3 arguments to the function!'
```

So, Python knows we passed three arguments to the function and treats them as _list_. This means we have all the list-magic available inside the function with `args`!

### **kwargs

`**kwargs` is a _keyworded_ variable length of arguments which will be treated as a _dict_:

```bash
>>> def kwargs_fun(**kwargs):
...     if 'name' in kwargs:
...             return "kwargs had name {} in it!".format(kwargs.get("name"))
...     else:
...             return "kwargs didn't had a name in it!"
...
>>> kwargs_fun(name="John Dough")
'kwargs had name John Dough in it!'
```

Easy, right?

Let's refactor our `greet()` function  to use `**kwargs`:

```bash
>>> def greet(**kwargs):
...     return "Hello, {}!".format(kwargs.get("name") if kwargs.get("name") is not None else "")
>>> greet(name="John Dough") # Note that we need to give the parameter as keyworded for Python to pick it out.
'Hello, John Dough!'
```

## Conclusion

We've now scratched the surface of Python by learning the absolute basics. These skills will come handy in the future lessons so let's make sure these are in our heads!
