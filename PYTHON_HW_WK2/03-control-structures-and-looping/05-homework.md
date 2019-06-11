---
title: 05 - Homework
root: '/modules/module-1/module-1-3-control-structures'
tree: '01 - Python Basics|03 - Control structures'
module: module-1
---

# 05. Homework

1. Given a list `[1,2,3,4,5,6,7,8,9]`
    1. Print item in index 4 using bracket notation
    2. Print item in index 5 using negative [-1] index
    3. Print every second item from the list
    4. Print items from 3rd to 5th

2. Given a dict `{'foo': {'name': 'Foo', 'lastname': 'Fooer'}, 'bar': {'name': 'Bar', 'lastname': 'Baer'}, 'Baz': None}`
    1. Print all the keys
    2. Print `bar`s `name` and lastname in format "Firstname is [NAME], and lastname is [LASTNAME]". Hint: Use string formatting & placeholders
    3. Loop over all keys and print the name as mentioned in the previous step IF the keys value is not empy.

3. Create a function named `summer` which takes two parameters: `a` and `b`
    1. Make the function return sum of the parameters. Note: Do NOT modify the original parameters
    2. Refactor the function to have default values to parameters
    3. Refactor the function to have `**kwargs` and if alternate parameter `negatove` is `True` return the value as a negative sum.

4. Given a list `['python', 'and', 'data', 'science', 'is', 'awesome']`
    1. Create a new list from the given list using list comprehension and include item only if it's length is greater than 5
    2. Create a dict from the given list using comprehension where list index is the key and value is the actual value
    3. Add item to the dict where the key is the next integer and value is "!"

5. Create a function which takes a list-type parameter and returns a new list containing only integers from the parameter list in an descending order. e.g. if the function receives parameter `['x', -0.1, 'foo', True, 'bar', 10, 1.1, '8', 5, None, 12]`, it should return `[12, 10, 5]`. Note: Do not modify the original parameter and use list comprehension.
