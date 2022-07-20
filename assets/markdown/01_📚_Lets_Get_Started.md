
<details>
<summary>Table of Content</summary>
  
# Table of Content

- [Table of Content](#table-of-content)
  - [What is Python?](#what-is-python)
    - [Things to know](#things-to-know)
  - [How to install it?](#how-to-install-it)
    - [Cleaner?](#cleaner)
    - [What can it do?](#what-can-it-do)
    - [Why do I need different version of python?](#why-do-i-need-different-version-of-python)
    - [So how to install this "environment manager thingy"?](#so-how-to-install-this-environment-manager-thingy)
    - [And, how do we install conda?](#and-how-do-we-install-conda)
    - [Are we done yet?](#are-we-done-yet)
  - [Lets Talk About Dependencies](#lets-talk-about-dependencies)
    - [What now? A dependencies manager?](#what-now-a-dependencies-manager)
    - [So no need to install another dependency manager?](#so-no-need-to-install-another-dependency-manager)
    - [This is the last thing right?](#this-is-the-last-thing-right)
  - [Here We Go Again With IDE](#here-we-go-again-with-ide)
    - [Should we use python notebook? or should we use regular python?](#should-we-use-python-notebook-or-should-we-use-regular-python)
    - [Umm, so now what?](#umm-so-now-what)
    - [When are we talking about IDE?](#when-are-we-talking-about-ide)
    - [What IDE Should I Choose?](#what-ide-should-i-choose)
  - [TLDR](#tldr)

</details>

## What is Python?

![image](https://openclipart.org/download/248484/387.svg)
source: openclipart.org

Made by [Guido Van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) in the late 80s and first released in 1991.

Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation [(Kuhlman, Dave)](https://web.archive.org/web/20120623165941/http://cutter.rexx.com/~dkuhlman/python_book_01.html).

### Things to know

- Indentation rather than `;` or `{}` or `begin end`
- Support structuring with function, class, module and package
- Support flow control such as `if if-else while for`
- Support OOP (Object Oriented Programming)

## How to install it?

You can download it straight from [python official website](https://www.python.org/downloads/) and install it like you do with a program. **BUT**, it's better to do things a little bit cleaner with the help of something.

### Cleaner?

Yes! You can make the process of installation cleaner using something called an environment manager.

### What can it do?

- Install different version of python for each project you have.
- Make it easier to change python version for each project
- Preventing conflict between projects.

### Why do I need different version of python?

Because of something called **dependencies**, we will talk more about it later, to make it simple, you can use a package made by someone else and sometimes it can only run in specific python version. In real production environment, they don't usually use the latest python version but they use an older version to make sure things work accordingly.

### So how to install this "environment manager thingy"?

There are a lot of environment manager out there ranging from the old built-in one such as virtualenv to the latest manager made by the community and/or organization such as Conda. With a wide range of manager to choose from, it's going to be a bit hard to choose what to use. For this workshop we are going to focus solely on conda made by Anaconda organization.

### And, how do we install conda?

![image](https://assets.anaconda.com/production/anaconda-meta.jpg?w=1200&h=630&q=82&auto=format&fit=clip&dm=1632326952&s=2b336a00fa13405f84ce2f5b74e21fee)
source: anaconda.com

There are two main distribution that the Anaconda organization provide, the first one is Anaconda and the other one is Miniconda. The difference between these two distribution is solely based on the things that is preinstalled when you install the distribution. Anaconda provided a lot of preinstalled library for science such as Numpy, Scipy, Pandas and so on with built-in GUI and conda env manager, while Miniconda only install the conda env manager and usually aimed for more advanced user. You can access both installation in the list below:

- [Anaconda](https://www.anaconda.com/products/distribution)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

### Are we done yet?

Nope, I put a lot of information upfront so that you get prior knowledge with how to set things up and how things is going on under the hood. This is going to help with your journey learning Python.

## Lets Talk About Dependencies

In the previous subchapter, we talk about dependencies, so now lets talk about what it is actually and how is it going to affect your workflow.

### What now? A dependencies manager?

You are 100% correct if you guess this out, but first a bit more about dependencies.

The meaning of dependencies can be simplified into **a graph of interconnection between libraries/package versions that rule how a library can be installed**.

Let say library A use library B, we can say that library A depends on library B and library B is the dependencies for library A. This set of rules is usually set in a library requirements, but how if you use a lot of library with each of their own requirements? How do you sorted things out?

This is where dependencies manager came to the rescue, there are **a lot** I repeat **a lot** of dependencies manager out there, such as pip, pipenv, poetry and conda. pip is a builtin dependency manager that usually came with python and conda the environment manager we talk about before is also a dependency manager. So lets use conda as your dependency manager

### So no need to install another dependency manager?

Yes, long ago I use conda but now I personally use poetry for my project, but you can stick with conda for now.

### This is the last thing right?

Nope, we need one more thing, we need a place to code right?

## Here We Go Again With IDE

We already finish installing things and know about some of this stuff, but where do we code? Okay, but before that lets talk about something more important, honestly the internet is actually divided in this.

### Should we use python notebook? or should we use regular python?

To get the record straight:

- Coding with python notebook (.ipynb) is a way of coding python where we can split things up to chunks and can run each chunks independently while still keeping variable between chunks
  ![image](https://upload.wikimedia.org/wikipedia/commons/d/d0/Jupyter_Notebook.png)
source: wikimedia.org

- Coding in regular python (.py) is coding everything and running things at once
  ![image](https://live.staticflickr.com/65535/50755664453_892327b031_b.jpg)
source: flickr.com - kirbyurner

This is the main pros and cons from both of this approach

|                                          | .ipynb             | .py                |
| ---------------------------------------- | ------------------ | ------------------ |
| Easy to use (Beginner Friendly)          | :white_check_mark: |                    |
| Easy to modularize (Production Friendly) |                    | :white_check_mark: |

### Umm, so now what?

Personally I use both in my development flow, I experiment things out with notebook and finish it off with a script. I strongly recommend that you start it out to experiment using notebook and slowly start to code in raw regular python script.

What I've seen on the internet and a few forums, notebook is really popular in data analytics while the python script is popular in  things that need script to run such as server backend and also website frontend.

### When are we talking about IDE?

Okay, we'll talk about IDE now, IDE is the acronym of Integrated Development Environment. This is basically an app that can do everything for you, ranging from running, writing, to seeing the inside of the actual python code, editing and also debugging. There are a lot of IDE to choose from if you search but the powerhouse in Python programming is Jupyter Lab, VSCode and PyCharm.

- Jupyter Lab
  ![image](https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Sample-jupyterlab-2021-06.png/1200px-Sample-jupyterlab-2021-06.png?20210607155631)
  source: wikimedia.org
  
  A web browser based IDE that was developed as the successor of the regular Jupyter Notebook, with the added function such as extension and also file explorer similiar with what modern python IDE usually looks like. This IDE is popular in data analytics community.

- VSCode
  ![image](https://live.staticflickr.com/841/43359779851_2b149c66d6_b.jpg)
  source: flickr.com

  Maybe one of of the most popular IDE, this IDE isn't bounded to program in Python but a lot of other programming language can be written, run and test here.

- PyCharm
  ![image](https://upload.wikimedia.org/wikipedia/commons/0/05/PyCharm_4.5.1.png)
  source: wikimedia.org

  An IDE made by JetBrains solely for the purpose of programming in Python, it got built-in support for env manager and dependencies manager, making it easiser to set up project and installing dependencies.

### What IDE Should I Choose?

From my personal experience with these IDE, they got their things of their own, some pros and cons that I won't talk about because choosing an IDE is based on your own preference. I started Python from raw Jupyter Notebook then I join the Jupyter Lab 3.0 train, but with more project that needed GUI and also non Python project, I start switching my workflow to VS Code. I've just started to use PyCharm, the set up and dependencies installation is a breeze, but I was used to set things up in VS Code, I just stick with it.

For this workshop however, I'll recommend you use VS Code, because now it support both .py and .ipynb so you can easily switch between notebook and python script while also give a lot of room to develop things other than Python.

## TLDR

- Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation [(Kuhlman, Dave)](https://web.archive.org/web/20120623165941/http://cutter.rexx.com/~dkuhlman/python_book_01.html).

- You can install python from the official website but it's better to install an environment manager that can handle installing different version of python to make it easier to switch versio9n between project.

- Environment manager help prevent conflict between project by creating a virtual environment

- I recommend conda as the environment manager with [Anaconda](https://www.anaconda.com/products/distribution) for beginner and [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

- Dependencies is a graph of interconnection between libraries/package versions that rule how a library can be installed.

- You need dependencies manager to resolve the dependencies in a project, conda can be used to solve dependencies and pip - the builtin dependencies manager - can be use to

- You can code python using python notebook (.ipynb) or python script (.py), if you are going to do a lot of data analytics, python notebook can be your choice while python script is used for a more mature implementation of python such as GUI, webserver, and frontend development.

- Its better to start by learning in notebook and start to transition to python scripting. A balance between these two can help leverage your development process.

- The 3 powerhouse for Python coding is Jupyter Lab, VS Code, and PyCharm.

- If you are purely doing data analytics, Jupyter Lab is your choice. If you are purely using python script and want easy set up use PyCharm. Lastly, if you want more flexibility in using other programming language, VS Code is your choice.
