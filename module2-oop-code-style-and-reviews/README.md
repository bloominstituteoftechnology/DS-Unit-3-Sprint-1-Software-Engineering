# Object-Oriented Programming, Code Style and Reviews

"Code that works" is good - "code that other people can read" is better.

## Learning Objectives

- create a basic Python class, with a constructor, methods, and fields
- write stylistic (PEP 8) Python code, and give and receive a basic code review

## Before Lecture

Read the [official Python Class
tutorial](https://docs.python.org/3/tutorial/classes.html), and try to reproduce
the examples in your own Python environment.

Read the [PEP 8 style guide](https://pep8.org/), and then look back at code
you've written in the past. Identify at least three times you did something the
style guide says you shouldn't, and write the corrected version.

## Live Lecture Task

We will first live code a class based on class request/discussion, brainstorming
what fields and methods make sense. We will then discuss style more broadly.

Style matters - but we're engineers, which means we're a little lazy. Let's set
up tools to check style automatically, so we fix issues before they hit review.

Then we will discuss what a code review actually is, and if folks are brave they
can volunteer to have their code reviewed with the class. It's scary, but this
is a safe time to do it (and good practice for the assignment!).

## Assignment

First, revisit your code from yesterday - was it stylistic? Run a style check 
and correct any issues you see. Also, refactor your code
to use at least 1 class - remember, be DRY (Don't Repeat Yourself), not WET
(Write Every Time)!

Then - code review! Examine the code below and clean it up following the [PEP8 Style Guide](https://pep8.org/) 
and try your best to avoid using your linter! Here is the unreadable code that you should try and 
make PEP8 compliant: 

```python

### IN style_example.py FILE###

#what would you say if you were working with someone and this is the code they gave you?

import math,sys;
def exampl1():
  ### THIS IS A LONG COMMENT AND should be wrapped to fit within a 72 character limit
  some_tuple =( 1,2, 3,'a'  );
  some_variable={"long":'LONG CODE LINES should be wrapped within 79 character to prevent page cutoff stuff',
                 'other':[math.pi, 100,200, 300, 9999292929292, "This IS a long string that looks gross and goes beyond what it should"]
                  ,"more": {"inner": "THIS whole logical line should be wrapped"}, "data": [444,5555,222,3,3,4,4,5,5,5,5,5,5,5]}
  return (some_tuple, some_variable)
def example_2(): return {"has_key() is deprecated": True}
class Example3(   object):
  def __init__   (self, bar):
    if bar: bar+= 1; bar=bar* bar     ; return bar
    else:
                some_string = """
                  INDENTATION IN MULTIPLE STRINGS SHOULD NOT BE TOUCHED only actual code should be reindented,
THIS IS MORE CODE
"""
                return (sys.path, some_string)
```

Here a few considerations to keep in mind while doing a code review:
- Can you follow the code flow/layout?
- Can you understand the logic/reasoning for what it is doing?
- Could you build with (`import` and use) or extend on it (as a developer adding
  more to the codebase)?
  
As an additional exercise, pair up with a fellow student (self organized) and perform a code review on their
newly written OOP converted helper functions! Remember to think about the previous considerations in your code review
and walk them through areas you think could use some improvement. 

Please submit your new `helper_functions.py` that's been transformed into classes and 
the edited code review as a file named `code_review.py`.

## Resources and Stretch Goals

If you have trouble getting a PEP8 tool working in your local environment, you
can use [PEP8 online](http://pep8online.com/) to check code.

Also, many organizations create their own "flavor" of style guides - for an example,
read the
[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

***Stretch***: And if you get through all the above - make `lambdata` better! Implement 2 more
helper functions, and/or refactor your code to be more object-oriented.
