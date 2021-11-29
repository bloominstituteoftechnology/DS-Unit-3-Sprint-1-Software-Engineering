# MODULE 1 Project - Python Modules, Packages, and Environments

Places for your code (and dependencies) to live.

## **Learning Objectives**

* Understand and follow Python namespaces and imports
* Create a Python package and install dependencies in a dedicated environment

## Before Lecture

In order to follow along fully with today’s Guided Project, please use this warmup time and [this document](https://github.com/LambdaSchool/DS-Unit-3-Setup) to install the following tools:

* VS Code
* Git Bash
* Python
* Pipenv

Also ensure you are able to run each of the following commands without error:

* `conda --version`
* `pipenv --version`
* `git --version`
* `code ~/Desktop` (Mac / Windows Git Bash) or `code C:\Users\USERNAME\Desktop` (Windows other)

## Guided Project

During today's Guided project we'll be talking about:

* Writing Python code locally vs in Notebook
* Common command line commands
* Virtual Environments
* Python scripts, modules, packages, and libraries

For more information visit the [Guided Project markdown file](https://github.com/ryanleeallred/DS-Unit-3-Sprint-1-Software-Engineering/blob/main/module1-python-modules-packages-and-environments/guided-project.md)

## Module Project (assignment)

1) Create your own lambdata-yourusername package (structure your package the same way it was done in the lecture)  
2) Implement at least 2 of the following "helper" utility functions in a `helper_functions.py` module.

For more information visit the [Module Project markdown file](https://github.com/ryanleeallred/DS-Unit-3-Sprint-1-Software-Engineering/blob/main/module1-python-modules-packages-and-environments/assignment.md)

## Stretch Goals

1) Complete more than one of the helper functions from part 3 of the assignment.

2) Look for ways to reduce function calls to Pandas and NumPy in your `helper_functions.py` module. Try and implement as much as you can with "vanilla python"

3) Continue to challenge yourself by publishing your package with pyPI.

### Publishing your Package with PyPI

1. Register for a test PyPI account
2. Publish your package as lambdata-yourusername (to avoid conflicts)
3. Start a Python notebook, and install your package with !pip install --index-url [https://test.pypi.org/simple/](https://test.pypi.org/simple/) lambdata-yourusername
4. import lambdata_yourusername as lambdata in your notebook, and try it out!

We suggest using [Twine](https://pypi.org/project/twine/#:~:text=Twine%20is%20a%20utility%20for,and%20links%20to%20additional%20resources.) for uploading your pypi packages. Twine itself can be installed with pipenv install -d twine so it is a development dependency.

You might find the command below important in uploading: twine upload --repository-url [https://test.pypi.org/legacy/](https://test.pypi.org/legacy/) dist/*

## Resources

Many of the utility functions can be implemented with the right clever calls to pandas, numpy, and other libraries - that's fine! Use those as dependencies. There's still value in a package that encapsulates more complicated libraries and exposes streamlined functionality with a simplified API. If you would like to generate some fake data check out the [Faker python package](https://faker.readthedocs.io/en/master/) to craft specific data types.

Also note - there's a lot more than 2 ideas to choose from for your helper functions. Throughout the week, whenever you have finished the daily assignment baseline, you can always come back and add more functionality to your lambdata (including ideas of your own)!

Check out steps 3 to 6 if you would like to attempt a stretch goal. I would recommend trying to figure this out on your own! Remember to check documentation and Google!

The [official Python packaging tutorial](https://packaging.python.org/tutorials/packaging-projects/) can help you if you get stuck with the assignment. Make sure to use Test PyPI! If you get through all the steps, try some of the following stretch goals:

* Check out the source code for [pandas](https://github.com/pandas-dev/pandas), and see if you can make sense of it. Try to find the actual logic behind specific functions you use (e.g. `pd.DataFrame`, `df.replace`, etc.). Reading source code is challenging, especially from large codebases, but it's a skill that will help you debug and fix real issues in professional situations.
* Explore [PyPI](https://pypi.org/), the Python Package Index - this is where `pip` (the official base Python package installer, which both Anaconda and `pipenv` build on) gets things from by default. For now stick with Test PyPI for your own publishing, but you can work to make things "real"!
