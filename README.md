# Introduction to Python, Variables and Data Types

## What is Programming?

The process of preparing an instructional program for a device (such as a computer).

## What are Programming Languages?

It acts as a middle-man or translator for translating a program into machine code.

## How do computers perform tasks?

- To perform any task, we need 2 things
  - **The language that computers understand**
  - **Programming Environment**

## Programming Environment➖

- A programming environment combines hardware and software and allows a developer to build applications.
- Developers typically work in **integrated development environments or IDEs**.
- These connect users with all the features necessary to write and test their code correctly.
- Different IDEs will offer other capabilities and advantages.
- Examples of IDEs ➖ **Visual Studio, NetBeans, Eclipse, IntelliJ**, etc.

## What is Python?

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.

| Term              | Meaning                                                       |
| ----------------- | ------------------------------------------------------------- |
| Interpreted       | Executes code line-by-line, no need to compile                |
| Object-Oriented   | Supports class and object-based program structure             |
| High-Level        | Easy to read/write, abstracted from hardware                  |
| Dynamic Semantics | Variables don’t need types declared, type checking at runtime |

Created by Guido van Rossum in 1991 at CWI (Centrum Wiskunde & Informatica), Netherlands.

## General-Purpose Language

Python can be used for:

AI & Machine Learning

Data Science (Most popular choice!)

Web Development (Django/Flask frameworks)

Automation and Scripting

Famous Companies Using Python + Django:
YouTube, Spotify, Pinterest, Instagram, Dropbox

## Why the name “Python”?

Inspired by the BBC comedy “Monty Python’s Flying Circus”.
Guido wanted a name that was short, unique, and mysterious.

## Why Learn Python?

- Simple & Easy to Learn
- Dynamic and Powerful
- Huge Library Ecosystem (130,000+ packages)
- Free and Open Source
- Platform Independent
- Interpreted (no need to compile)
- Robust Exception Handling

## Indentation in Python

Python uses indentation to define blocks of code instead of curly braces {}.

```
    if True:
    print("This is indented correctly")
    ❌ Indentation error if not properly aligned.

```

---

## Note => The extension used for Python files is .py.

## Printing Output in Python

Use the built-in print() function:

```
    print("Hello, world!")
```

You can print strings, numbers, and variables.

---

## Python Comments

Used to explain code and prevent execution.

### Single-line comment:

```
# This is a comment
```

### Multi-line comment:

```
'''
This is
a multi-line comment
'''

```

## What is a Variable?

A named container to store data.

```
name = "Alice"
age = 25
```

Think of variables as boxes with labels.
(CASE SENSITIVE)

## Check Variable Type

```
print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>
```

Python is a fantastic language that automatically identifies the type of data for us.

## Rules for Declaring Variables

### Valid Names:

1. Must start with a letter or \_ (underscore)
2. Can contain letters, numbers, and underscores
3. Case-sensitive (age, Age, and AGE are different)
4. Don't Use Keywords

---
