# Assignment

## Part 1 - PEP8 Styles

Revisit your code from yesterday - was it stylistic? Look over your code and compare it to the PEP8 guide (maybe even use your linter)
and correct any issues you see.

## Part 2 - Add Some Classes

Create a new file in your bloomdata folder called `student.py`

- Create a parent class called `Student` that has at least two attributes and two methods associated with it.

- Create a child class called `BloomTechStudent` that adds at least one attribute and one method that are specific to BloomTech students.

- Then write a function called `student_generator` that will generate randomly generate values for your Bloomtech student's attributes. Create 30 different randomly generated Bloomtech students and add them to a list.

## Part 3 - Code Review

Copy the code below into a new `code_review.py` file and then work on cleaning it up following the [PEP8 Style Guide](https://pep8.org/). Try it without your linter first and see how far you can get and then turn your linter on to see what you missed.

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
  
## What should I submit to Canvas?

Please submit your `student.py` file and your `code_review.py` files to Canvas.

## Resources and Stretch Goals

### Stretch Goals

If you get through all of the above - make `bloomdata` better! Implement 2 more helper functions, and/or refactor your code to be more object-oriented.

### Resources

If you have trouble getting a PEP8 tool working in your local environment, you can use [PEP8 online](http://pep8online.com/) to check code.

Also, many organizations create their own "flavor" of style guides - for an example, read the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
