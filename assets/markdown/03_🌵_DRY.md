<details>
<summary>Table of Content</summary>

# Table of Content

- [Table of Content](#table-of-content)
  - [What is DRY?](#what-is-dry)
  - [What's a function?](#whats-a-function)
  - [What's a Class?](#whats-a-class)
  - [TlDR](#tldr)

</details>

## What is DRY?

DRY is an abbreviation for Don't Repeat Yourself, a small but powerful reminder for programmer to have as little of repetition in their code. But how? Well there is something tha can help us with that called **Function** and **Class**, both in respect of each other is used for **Functional Programming** and **Object Oriented Programming**. We'll learn more about function than class because it's easier to understand for beginners.

## What's a function?

Function is a way in programming where we can bundle up some process making it easier to use anywhere and easier to change. Let's see the example problem below.

*Without function*
*Get the sum of each pair*

```python
x = (1, 2)
y = (3, 4)
z = (5, 6)

print(x[0][0] + x[0][1])
print(y[0][0] + y[0][1])
print(z[0][0] + z[0][1])
```

*Now make the first variable squared*

```python
x = (1, 2)
y = (3, 4)
z = (5, 6)

print(x[0] ** 2 + x[1])
print(y[0] ** 2 + y[1])
print(z[0] ** 2 + z[1])
```

*And Now make the second variable squared root*

```python
x = (1, 2)
y = (3, 4)
z = (5, 6)

print(x[0] ** 2 + x[1] ** (1 / 2))
print(y[0] ** 2 + y[1] ** (1 / 2))
print(z[0] ** 2 + z[1] ** (1 / 2))
```

By seeing this example, you can imagine, doing this but with hundreds of line and interconnected process, it's going to be a **NIGHTMARE**, so let's do this the non nightmarish way

*With function*
*Get the sum of each pair*

```python
# Anatomy of a function
# def FUNCTION_NAME(VARIABLE(S)):
#     PROCESS
#     return OUTPUT
# For both VARIABLE and OUTPUT, you can use as many as you want, 
# and also not use them at all, you call that 
def process_pair(pair):
    return pair[0] + pair[1]


x = (1, 2)
y = (3, 4)
z = (5, 6)


print(process_pair(x))
print(process_pair(y))
print(process_pair(z))
```

*Now make the first variable squared*

```python
def process_pair(pair):
    return pair[0] ** 2 + pair[1]


x = (1, 2)
y = (3, 4)
z = (5, 6)


print(process_pair(x))
print(process_pair(y))
print(process_pair(z))

```

*And Now make the second variable squared root*

```python
def process_pair(pair):
    return pair[0] ** 2 + pair[1] ** (1/2)


x = (1, 2)
y = (3, 4)
z = (5, 6)


print(process_pair(x))
print(process_pair(y))
print(process_pair(z))

```

See? it's easier to do thing with function, it compact things up and changes can be made easily without a lot of things to change with.

## What's a Class?

Class is a way in Python to do some Object Oriented Programming, in short we use Class and treat them in our program as an Object.

*This is how class looks like*

```python
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi my name is {self.name}, and I'm {self.age} years old")


person_1 = Human("Bob", "18")
person_2 = Human("Susie", "18")

person_1.greet()
person_2.greet()
# Output: 
# Hi my name is Bob, and I'm 18 years old
# Hi my name is Susie, and I'm 18 years old
```

We can see that each "Object" has it own function and also variable that we can use. There a lot of implementation of OOP but to cut thing short I'll just show you what it look like, feel free to Google it out.

Let's go to the next chapter!

## TlDR

- We can make some repetitive lengthy process into a function that can be reuse to process things.
- Function help reduce the amount of edit when you need to edit the process.
- Class is a way in python to make an object to do OOP.
- Object in a way, got it own variable and also function inside of it
