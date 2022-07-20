<details>
<summary>Table of Content</summary>

# Table of Content

- [Table of Content](#table-of-content)
  - [The Pythonic Way](#the-pythonic-way)
  - [PEP8: Python Best Practice](#pep8-python-best-practice)
  - [TLDR](#tldr)

</details>

## The Pythonic Way

As it was mention in the first chapter, the purpose of Python is to make things easier to read. In this chapter we are going to talk about some general things that can be done in a more pythonic way. Before that let me introdue you to an easter egg in Python, a poem that encapsulate the mindset of the maker of this programming language

```python
import this
# Output:
#
# The Zen of Python, by Tim Peters
# 
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
```

Here we go with some examples that might get you a glimpse of the "Pythonic Way"

- Swapping variable

  ```python
  # Non Pythonic Way
  a = 10
  b = 20
  temp = 0
  
  temp = a
  a = b
  b = temp

  # Pythonic Way
  a , b = b, a
  ```

- Iterating on an array

  ```python
  # Non Pythonic Way
  x = [1,5,2,6,3,5,5,1]
  
  i = 0
  while i < len(x):
    print(x[i])
    i = i + 1

  for i in range(len(x)):
    print(x[i])

  # Pythonic Way
  for i in x:
    print(i)
  ```

- Searching max number in array

  ```python
  # Non Pythonic Way
  x = [1,5,2,6,3,5,5,1]
  temp_max = 0
  for i in range(len(x)):
    if temp_max < x[i]:
        temp_max = x[i]
  print(temp_max)

  # Pythonic Way
  print(max(x))
  ```

- Iterating over dictionary

  ```python
  # Non Pythonic Way
  x = ["a":1,"b":1,"c:3]
  
  for key in x.keys():
    print(key, x[key])

  # Pythonic Way
  for key, values in x.items():
    print(key,values)
  ```

This is only the glimpse of the capability of Python, I learn new things everyday and you'll do to. If this is your first language to learn, please learn about the rough edges first, you'll have better understanding in programming in general. If this isn't your first language, engage with the Pythonic Way more, you're going to find things easier to learn.

## PEP8: Python Best Practice

[PEP8](https://peps.python.org/pep-0008/) or Python Enhancement Proposal is long proposal with a lot of things that help to enhance your experience programming in Python. Ranging from convention such as how to name a variable, the amount of character in a line, until how to import things out.

It's not something that you must follow, but following it will make it easier for you and other people to read and understand your code.

To make it a little bit easier for you to follow these convention, I recommend that you use a formatter such as autopep8, black or yapf, to install it you can just google "How to install (your formatter) in (your IDE)". Install it and let it do the work.

## TLDR

- You can do things easier in Python using the Pythonic Way, there are a lot of things that you can do, search it in the internet and you'll find cool new way to write the code.
- If Python is your first programming language, it's okay to learn things the hard way so that you can get the basic of computing paradigm. If Python is not your first programming language, learning the Pythonic Way will make you easier to code in Python.
- PEP8 is your go to guide for the best practice in writing your code, with the vast things to see there I recommend that you just use a formatter for your IDE ranging from autopep8, black and yapf
