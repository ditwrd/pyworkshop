<details>
<summary>Table of Content</summary>

# Table of Content

- [Table of Content](#table-of-content)
  - [Let's Talk About Data Type](#lets-talk-about-data-type)
    - [But what is data anyway?](#but-what-is-data-anyway)
    - [Why don't you assign the data type like other programming language?](#why-dont-you-assign-the-data-type-like-other-programming-language)
    - [So, what data type can you store in Python?](#so-what-data-type-can-you-store-in-python)
      - [**Numerical Types**](#numerical-types)
      - [**Sequential Types**](#sequential-types)
      - [**Mapping Types**](#mapping-types)
      - [**Text Types**](#text-types)
    - [That's a lot, whats next?](#thats-a-lot-whats-next)
  - [Let's Talk About Condition, Loops and Control Flow](#lets-talk-about-condition-loops-and-control-flow)
    - [Condition?](#condition)
    - [Loop? Loop? Loop?](#loop-loop-loop)
  - [TLDR](#tldr)

</details>

## Let's Talk About Data Type

We've spent a lot of time talking about setting things up but we haven't talk about python so let's start now and make it as quick and simple as possible.

### But what is data anyway?

Data, to put it simply is basic information. So data type is basically just the type of information. This data type is then stored in something called a ***variable***. This is you assign a data into a variable using Python

```python
im_a_variable = "I'm a data"
```

### Why don't you assign the data type like other programming language?

If you ever code using other programming language, this may seems odd, but this is how Python works, it dynamically "type" the variable.

P.S: So basically it know the data type of a variable when you run the program.

### So, what data type can you store in Python?

I'll list the things down below:

#### **Numerical Types**

- **Integer (int)**
    Integer is a number you usually identified as "that number without any number after comma".

    ```python
    x = 4
    y = 2
    print(type(x))
    # Output: <class 'int'>
    # <- Hash is a comment symbol, so everything after the hash will be ignored by the interpreter
    print(x + y) # -> Addition
    # Output: 6
    print(x - y )# -> Substraction
    # Output: 2
    print(x * y) # -> Multiplication
    # Output: 8
    print(x / y) # -> Division
    # Output: 2
    print(x % y) # -> Modulo Operation
    # Output: 0
    print(x ** 2) # -> Exponential Expression
    # Output: 16
    ```

- **Float (float)**
    Float is a number you usually identified as "that number with number after comma".

    ```python
    x = 1.23456
    print(type(x))
    # Output: <class 'float'>
    y = 1
    print(type(y))
    # Output: <class 'int'>
    print(x-y)
    # Output : 0.23456
    ```

- **Complex (complex)**
    Complex is as you the name stated, complex number. If you haven't learn about it, it's basically a number concept using imaginary number that got $\sqrt{-1}$ on them usually indicated by i or j, where the latter is use for Python.

    ```python
    x = 1234j
    print(type(x))
    # Output: <class 'complex'>
    ```

#### **Sequential Types**

- **List (list)**
    List is a concept of putting a lot of data inside container where you can call them using their indexes.

    ```python
    x = [1,1.23456, 1234j]
    # Notes;
    # You can put any type of data inside a list
    
    print(type(x))
    # Output: <class 'list'>
    print(x[0])
    # Output: 1
    print(x[1])
    # Output: 1.23456
    print(x[3])
    # Output: IndexError: list index out of range
    # If you copy paste the whole thing and run, it will stop until the line above
    print(x[1:])
    # Output: [1.23456,  1234j]
    print(x[:2])
    # Output: [1, 1.23456]
    print(x[-1])
    # Output: 1234j
    print(x[-2])
    # Output: 1.23456
    print(x[-2:])
    # Output: [1.23456,1234j]
    x[0] = "one"
    print(x)
    # Output: ["one",1.23456,1234j]
    ```

- **Tuple (tuple)**
    Tuple can do everything a list can but without the ability to change it's content or in short it is **immutable**.

    ```python
    x = (1,1.23456, 1234j)
    print(type(x))
    # Output: <class 'tuple'>
    x[0] = "one"
    print(x)
    # Output: ["one",1.23456,1234j]
    ```

- **Range (range)**
    Range is a way to make an array of ascending number where you can change where it start, end and the difference between each number.

    ```python
    # range(start,end,step)

    x = range(5)
    print(type(x))
    # Output: <class 'range'>
    print(x)
    # Output: range(0,10)
    # This is equivalent with an array of number starting with 0 up to 4 -> [0,1,2,3,4]
    y = range(1,10,2)
    # This range is equivalent with [1,3,5,7,9]
    ```

#### **Mapping Types**

- **Dictionary (dict)**
    Dictionary (or hash map in computer term) is a data structure based on a key to value mapping.

    ```python
    x = {
    'name': 'John Doe',
    'age': 24,
    'is_worker': True,
    'other_info': {'hobby': ['coding', 'music'], 'love_cat': True},
    }

    print(x["name"])
    # Output: "John Doe"
    print(x["other_info])
    # Output: {'hobby': ['coding', 'music'], 'love_cat': True}
    print(x["other_info"]["hobby"])
    # Output: ['coding', 'music']
    ```

#### **Text Types**

- **String (str)**
    String is an array of bytes that represent character in unicode

    ```python
    x = "abc"
    print(type(x))
    # Output: <class 'str'>
    print(x[0])
    # Output: a
    ```

### That's a lot, whats next?

Actually, we haven't touch all of the types, but this should be sufficient enough for basic understanding with datatype, you can check out this quick summary from W3S [here](https://www.w3schools.com/python/python_datatypes.asp). Now let's go to the next sub-chapter.

## Let's Talk About Condition, Loops and Control Flow

Okay, that's a lot to talk about but let's talk about all of them

### Condition?

We are talking about logical condition that is the backbone of computing. Lets start with the basic of the basic.

- **Basic Logic**

  ```python
  x = 10
  y = 100
  print(x == y) # -> Equal to 
  # Output: False
  print(x != y) # -> Not equal to 
  # Output: True
  print(x > y) # -> Greater than 
  # Output: False
  print(x >= y) # -> Greater than or Equal to 
  # Output: False
  print(x < y) # -> Less than 
  # Output: True
  print(x <= y) # -> Less than or Equal to 
  # Output: True

  z = 50
  print(x > y and x < z) # -> You can use AND logic
  # Output: False
  print(x > y or x < z) # -> You can also use OR logic
  # Output: True
  ```

- **If Block**

  ```python
  #if CONDITION:
  #  PROCESS WHEN CONDITION IS TRUE
  x = 10
  y = 100
  
  if x > y:
    print("x is bigger than y")
  # We use indentation to seperate process inside 
  # the if block (other language usually use "()" or "{}")
  # Output:
  # No output because the condition isn't met, x > y yield False
  if x < y:
    print("x is smaller than y")
  # Output: x is smaller than y
  ```

- **If...Else Block**

  ```python
  #if CONDITION:
  #  PROCESS WHEN CONDITION IS TRUE
  #else:
  #  PROCESS WHEN CONDITION IS FALSE
  x = 10
  y = 100

  if x > y:
    print("x is greater than y")
  else:
    print("x is less than y)
  # Output: x is less than y
  ```

- **If...Elif Block**

  ```python
  #if CONDITION:
  #  PROCESS WHEN CONDITION IS TRUE
  #elif CONDITION2:
  #  PROCESS WHEN CONDITION2 IS TRUE and CONDITION IS FALSE
  #else:
  #  PROCESS WHEN CONDITION and CONDITION2 IS FALSE
  x = 10
  y = 100

  if x > y:
    print("x is greater than y")
  elif x == y:
    print("x is equal to y")
  else:
    print("x is less than y)
  # Output: x is less than y
  ```

That's basically all of the basic backbone of conditional logic you can do in Python, let's move on to the next thing.

### Loop? Loop? Loop?

Loop in essence is repeating a set of action over and over. Writing the same process for 1000 time ain't fun right? Let's see how we can loop things out.

- **While Loop**

  ```python
  # while CONDITION:
  #   PROCESS TO REPEAT WHILE THE CONDITION IS TRUE
  x = 0

  while x < 5:
    print(x)
    x = x + 1
  # Output:
  # 0
  # 1
  # 2
  # 3
  # 4
  ```

- **For Loop**

  ```python
  # for VARIABLE(S) in ARRAY:
  #   PROCESS THINGS IN ARRAY THAT NOW CALLED VARIABLE(s)
  x = ["I", "Love", "Python"]
  
  for i in x:
    print(i)
  # Output:
  # I
  # Love
  # Python
  ```

- **Control Flow**

  ```python
  for i in range(1000):
    if i % 5 != 0:
      continue # -> This skip the cycle and "continue" to a new cycle
    if i > 10:
      break # -> This stop and "break" the loop
    print(i)
  # Output:
  # 0
  # 5
  # 10
  # P.S This is NOT a good way to deal with this case, 
  # this program is made to show how break and continue work
  ```

We've learn a lot for now, but how do we make something useful? We'll answer that on the next Chapter

## TLDR

- Data type of a variable is the type of information that the variable is currently holding.
- There are a lot of datatype ranging from numerical, sequential, mapping and text.
- There are also Condition/Logic and Loops that made things easier for logical process and also repetitive process.
