---
title: 04 - Booleans
root: '/modules/module-1/module-1-1-primitive-data-types'
tree: '01 - Python Basics|01 - Primitive data types'
module: module-1
---

# 04. Booleans

> _"To be or not to be..."_

Boolean (`bool`) is a _binary_ type which means it holds either _falsy_ (`False`, `0`, `None`, etc.) or _truthy_ (`True`, `1`, "foobar", etc.) values. In numeric contexts (e.g. when used as the argument to an
arithmetic operator), they behave like the integers 0 and 1.

Let's dig in:

```bash
>>> truthy = 1 # truthy is True
>>> falsy = 0 # falsy is False
```

```bash
>>> bool(truthy) # here we cast the truthy variable as a boolean and it confirms that it surely is True
True
>>> bool(falsy) # Casting the falsy to boolean tells us that it is False
False
```

Pretty predictable results, right? What about casting strings to booleans?

```bash
>>> truthy_str = "Yiha!"
>>> falsy_str = "" # This is still a string although it's empty
>>> bool(truthy_str)
True
>>> bool(falsy_str) # Python
False
```

As we suspected, casting string to booleans work logically: If the string is not empty, it's _truthy_ and if it's empty => it's _falsy_.

## Congratulations!

It's time to give a high-five to ourselves as we completed the first module and know _almost_ everything what Python has to offer.

...Just kidding. We just took a quick look at the _primitive_ types. Next module will introduce `lists`, `tuples`, `dicts` and `sets` which all can hold _multiple_ values instead of just one and are the building blocks of Data Science.
