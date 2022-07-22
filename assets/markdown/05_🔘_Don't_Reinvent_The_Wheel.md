<details>
<summary>Table of Content</summary>

# Table of Content

- [Table of Content](#table-of-content)
  - [Time Is Money](#time-is-money)
  - [Leveraging Public Library](#leveraging-public-library)
    - [Numpy - Low Level Computation](#numpy---low-level-computation)
    - [Scipy - High Level Computation](#scipy---high-level-computation)
    - [Pandas - Tabular Data Processing](#pandas---tabular-data-processing)
    - [Plotly - Graphing Tool](#plotly---graphing-tool)
    - [Streamlit - Pure Python Web App Builder](#streamlit---pure-python-web-app-builder)
  - [Stranger Danger](#stranger-danger)
  - [With great power comes great responsibility](#with-great-power-comes-great-responsibility)
  - [TLDR](#tldr)

</details>

## Time Is Money

You don't want to waste your time making things from ground up when there are already a lot of library out there that will help you do your exact stuff.

## Leveraging Public Library

There are a lot of professional out there, and they make a lot of library that can help either themselves, the community or for their own business. You can easily install this library through the command prompt using pip and/or conda. This leads us to some of the most useful library that us ***Engineers*** really need.

### Numpy - Low Level Computation

![image](data:image/png;base64,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)
source: wikimedia-commons

Numpy is a library that help with the fundamental of  scientific computing. Python is known to be slow due to some design choice it was made with ([click here if you want to know more](https://www.quora.com/Will-Python-become-faster-if-GIL-is-removed)). This isn't feasible if you want to crunch a lot of data such as mathematical computation, signal processing and even image processing.

Numpy leverage CPython, where essentialy the function in Numpy is pre-compiled in C and ready to use in Python. The speed also came from the "vectorization" of an array where you can do a lot of calculation that is similar with your traditional math calculation i.e. matrix calculation and else.

Personally this library is really handy when we are using a lot of matrix/array based calculation because it remove the needs of loops to do the calculation

*Example Code*

```python
import numpy as np

# Traditional multiplication to an array
x = [1]*500000

for i, value in enumerate(x):
    x[i] = value * 2
# Time: 0.09341669799994179 s

# Numpy Method
x = np.ones(500000)
mult_array = x*2
# Time: 0.009684274999926856 s

# ~ 10x faster

```

Check this [quickstart](https://numpy.org/doc/stable/user/quickstart.html) or this [absolute beginner tutorial](https://numpy.org/doc/stable/user/absolute_beginners.html) made by Numpy themselves to learn more

### Scipy - High Level Computation

![image](https://editor.analyticsvidhya.com/uploads/37666Scipy.PNG)
source: analyticsvidhya.com

Scipy is a higher level of Numpy where you can do more scientific stuff without the need of coding things out. We can do integration, optimization, signal processing, image processing and much more.

I usually use Scipy to do signal and image processing. Sometimes I use it to do some sanity check when I'm making my own scientific calculation.

### Pandas - Tabular Data Processing

![image](data:image/png;base64,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)
source: wikimedia-common
Pandas is a library that help you work with tabular data i.e. xlsx, csv, txt, parquet etc. This library help you getting tabular data from a file and can easily do some operation to the data.

I personally use this when I need to either do some analysis with data or extract an array of data to then be processed with Numpy.

You can check out this [10 minutes tutorial](https://pandas.pydata.org/docs/user_guide/10min.html) or [a longer essential tutorial](https://pandas.pydata.org/docs/user_guide/basics.html) provided by Pandas.

### Plotly - Graphing Tool

![image](data:image/png;base64,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)
source: wikimedia-common

There are a lot of plotting to choose from, the most mainstream plotting library is matplotlib, but it limits only for static plot without interactivity.

I personally use plotly due to the interactivity it gave and also a high level library it provided called Plotly Express that made it easier to plot things out.

You can check out plotly documentation [here](https://plotly.com/python/)

### Streamlit - Pure Python Web App Builder

![image](https://miro.medium.com/max/1200/1*srQdUu5yPUu6msmYr_-eQw.jpeg)
source: blog.devgenius.io

This is the library that made all of this module available. When working with program, you are bound to present things out, but maybe you don't have the time or knowledge to make things quickly.

Base on the first thing you see on their website, *"Streamlit turns data scripts into shareable web apps in minutes. All in pure Python. No front‑end experience required."*

I highly recommend this library if you need to make a GUI for your program. They also provide free cloud hosting of your web app, the sole reason you can access this web through the internet.

You can check Streamlit Get Started page [here](https://docs.streamlit.io/library/get-started)

## Stranger Danger

Even though there are a lot of library out there, you need to be careful with what library you are installing, and always make sure that you are installing the exact library you want to install.

There are a lot of case where some threat actor start making fake library that can either steal files from your computer and/or wreck havoc to your computer. This don't only apply for python library, all public library for any programming language is vulnerable with this kind of attack.

So alwasy double-check the library you want to install before hitting enter.

You can check one of the news about this attack [here](https://thehackernews.com/2022/06/multiple-backdoored-python-libraries.html)

## With great power comes great responsibility

With the abundance of public library making it easier to do things, it doesn't mean that you are going to do your homework with a pre-made function from some library.

There are some beauty and also knowledge that you can learn from impelementing low code stuff. From my personal experience, I've implemented both Discrete Fourier Transform and Fast Fourier Transform using pure Numpy. I still use Scipy and Numpy own function for the purpose of testing only.

So use the power of these library wisely.

## TLDR

- You can use and install public library from pip and/or conda to make your work easier.
- Numpy is a library that help you do array/matrix based computation easier and way faster than traditional Python.
- Scipy is a higher level library than Numpy that can do much more scientific stuff.
- Pandas is a library that help you work with tabular data such as the one you find in an excel or google sheets.
- Plotly is a library that help you make beautiful interactive plot easily.
- Streamlit is a library for building quick web apps and provided their own cloud to deploy your web app to the internet.
- Double-check the library that you want to install to make sure you are installing the library you intended to install
- Don't use these library to cheat your way through university, learn from low level coding and finally impelement it the easy way if there are no restriction against that
