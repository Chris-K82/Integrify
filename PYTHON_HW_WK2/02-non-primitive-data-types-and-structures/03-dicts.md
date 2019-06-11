---
title: 03 - Dicts
root: '/modules/module-1/module-1-2-non-primitive-data-types'
tree: '01 - Python Basics|02 - Non-primitive data types'
module: module-1
---

# 03. Dicts

Unlike tuples and lists, dicts (short for _Dictionary_) are indexed by keys. This means we no longer need the access a value by a numerical index. Instead, we can use a _string_ index which we can also make up by ourselves.

Let's dig in!

Dicts can be created by using either the `dict`-function:

```bash
>>> our_dict = dict({"keyone": "First", "keytwo": "Second", "keythree": "Third"})
```

or by using curly-braces:

```bash
>>> our_dict = {"keyone": "First", "keytwo": "Second", "keythree": "Third"}
```

For the sake of clarity, we'll use the latter from now on.

The above can be translated to pure english as: _"The value of 'keyone' is 'First', the value of 'keytwo' is 'Second' and the value of 'keythree' is 'Third'"_

## Accessing dict items

As said before, "Dicts are indexed by keys" which means if we want to access the values from `our_dict` => we use the previously declared keys by either accessing them with _bracket-notation_:

```bash
>>> print(our_dict["keyone"])
First
```

...or by using dict-method named `.get`:

```bash
>>> print(our_dict.get("keyone"))
First
```

Again, for the sake of clarity (and to prevent some bad assignments in the future) we'll use the latter.

## Adding items

Items can be added to our dict by simply assigning a valu to a key. If the key doesn't exist yet => it will be created, otherwise the value will be updated.


```bash
>>> our_dict["keyfour"] = "Fourth"
>>> print(our_dict.get("keyfour"))
Fourth
```

## Updating items

Values in a dict can be updated either by using dedicated `.update()`-method:

```bash
>>> our_dict.update({"keyone": "First updated"})
>>> print(our_dict.get("keyone"))
First updated
```

...or by directly assigning a new value to a _key_:

```bash
>>> our_dict["keyone"] = "First updated again"
>>> print(our_dict.get("keyone"))
First updated again
```

For the sake of clarity, it really doesn't matter which one we use as long as we're being consistent.

## Removing items

Python offers a couple ways of removing an item from a dict, which are `.pop()`-method and a `del` -keyword:

```bash
>>> our_dict.pop("keyone") # This one also returns the value of the removed
'First updated again'
>>> print(our_dict)
{'keytwo': 'Second', 'keythree': 'Third'}
>>> del our_dict["keytwo"]
>>> print(our_dict)
{'keythree': 'Third'}
```

## Dictionary methods

`clear()`: Removes all the elements from the dictionary<br>
`copy()`: Returns a copy of the dictionary<br>
`keys()`: Returns a list containing the dictionary's keys<br>
`values()`:	Returns a list of all the values in the dictionary<br>
`items()`: Returns a list containing the a tuple for each key value pair


There's more dict-methods coming in the next chapter when we'll focus on _looping_ so stay tuned!
