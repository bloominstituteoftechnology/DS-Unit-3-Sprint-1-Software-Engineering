# Testing

First we'll write some basic unit tests to demonstrate their functionality. We'll apply these concepts to `lambdata`, but will also discuss them more generally. Come to class with questions and be prepared to discuss documentation and licensing as well!

## Setup and Installation

As per the [pytest docs](https://docs.pytest.org/en/stable/) We can install pytest globally.

`pip install -U pytest`

Then we'll also install it to our virtual environment specifically, but we'll install it as a development package.

`pipenv install pytest --dev`

By using `--dev` and putting our test file outside of our package we're indicating to users of our package that the test suite and testing files that we're including are not something that they should need to use as part of the package itself, but that those parts of the project are for us the "developers" who are creating the package, not necessarily meant for users of the package --unless they want to make an open source contribution.

Create a file in your main project folder, but not inside of the lambdata folder call it `test_lambdata.py` it is a convention to put the word "test" at the beginning of any files that are for testing our code.

Import pytest and our lambdata package at the top of our new test file

```python
import pytest
import lambdata
```

inside of your `lambdata.py` add the following function

```python
def increment(num):
    return num + 1
```

Then, inside of your `test_lambdata.py` file import lambdata and create a function specifically to test the implementation of imcrement int. We'll put `assert` statements inside of our testing function. We can add as many assert statements as we like. If any of these assert statements fail an error will be thrown by pytest when the testing file is executed.

```python

import lambdata as ld

def test_increment_int():
    assert ld.increment_num(3) == 4
    assert ld.increment_num(100) == 101
```

Now go to your ternimal and run the test file.

`pytest test_lambdata.py`

You should see output similar to the following if all of the assert statements in your test function have evaluated to `True`

![terminal example pytest output](/images/test-example.png)

We can add more functions to test other scenarios or datatypes as inputs.

```python
def test_increment_float():
    assert ld.increment_num(5.5) == 6.5 

def test_increment_neg_int():
    assert ld.increment_num(-5) == -4

def test_increment_neg_float():
    assert ld.increment_num(-5.2) == -4.2
```

This time try running your test file with pytest using verbose output

`pytest test_lambdata.py --verbose`

The verbose output can be extra helpful for not only getting insight into which tests failed by why they failed as well. It does a good job of showing ups what was expected when we ran the test versus what values we actually got when we ran the test.

We can test more than functions. We can also test variables, lists, dataframes, classes, etc. But the process is very similar where we write a function inside of our test file and use assert statements that *should* be true if our code is correct and written properly.

Another helpful function when testing is to use the `isinstance()` function to test the datatype of certain variables and objects.

```python
def test_dtypes():
    '''test that the attribute is a string'''
    assert isinstance(my_object.attribute, str)
```

In this way we can compare datatypes of variables, objects, attributes, and values returned from functions to make sure tha their datatype is correct.

Let's practice testing a class by making a new `wallet.py` file and building a simple class inside of it. Something like:

```python
class Wallet():
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            print("insufficient funds")
        else:
            self.balance -= amount
    
    def add_cash(self, amount):
        self.balance += amount

    def __repr__(self):
        return f'<Wallet, Balance: ${self.balance}>'
```

Create a new file called `test_wallet.py` to test the class, import the class into the file and then let's write some functions to test the class functionality.

## Decorators

Decorators wrap a function to modify its behavior. They always start with the `@` symbol and are used right before a function. They will modify the behavior of the function that comes directly after the `@decorator` statement

### Functions as first class objects in Python

When we say that a function is a first-class object in python, what we mean is that the function definition (the function body) can be saved to a variable and passed around as a variable just like anything else.

```python
def say_hello(name):
  return f"Hello {name}!"

def be_awesome(name):
  return f"{name} is awesome."

def greet_bob(greeting_func):
  return greeting_func('Bob')
```

What a function does basically gets stored to a variable under the function name. The function is invoked when we put the invoking parentheses after the function's name.

```python
# the say_hello variable holds the function definition inside of it.
print(say_hello)

Output: <function say_hello at 0x7f954830e0>
```

Because of this, we can pass functions into other functions as parameters. Notice how when we pass them into a function we don't put the invoking parentheses on the end. If we did that then the function would immediately be invoked and we don't want that to happen yet.

```python
greet_bob(be_awesome)

Output: 'Bob is awesome.'
```

```python
greet_bob(say_hello)

Output: 'Hello bob!'
```

### Building a decorator from scratch

A decorator adds functionality to an already existing function by adding lines of code before and after the function. This extension of functionality takes the original function and "decorates" it with some additional functionality.  

We will us a wrapper function: `wrapper` to add lines of code before and after we invoke the main function of interest: `my_func`.

```python
def my_decorator(my_func):
  def wrapper():
    print("This happens before the function")
    my_func()
    print("This happens after the function")
  return wrapper

def my_func():
  print("Stuff my function does")

extended_func = my_decorator(my_func)

extended_func()

Output:
"This stuff happens before the function"
"Stuff my function does"
"This happens after the function"
```

This behavior is so useful that python has special built-in syntax to "decorate" functions (add functionality before and after) without having to wrap our function manually every time.

```python
@my_decorator
def my_func():
  print("Stuff my function does")

my_func()

Output:
"This stuff happens before the function"
"Stuff my function does"
"This happens after the function"
```

What the `@my_decorator` line does, is takes the function declared directly below it and passes it into the function called `my_decorator()` to add functionality before and after the main function is called.

## Pytest Fixtures

[From the Docs](https://docs.pytest.org/en/6.2.x/fixture.html)

Pytest fixtures are decorators that help us set up scenarios that can be repeated throughout our test cases so that we our testing code isn't as repetitive.

```python
@pytest.fixture()
def empty_wallet():
    '''returns a wallet instance with a zero balance'''
    wallet = Wallet()
    return wallet

@pytest.fixture
def wallet_20():
    '''returns a wallet of balance: 20'''
    return Wallet(20)
```

Now we can pass the variables `empty_wallet` and `wallet` into any of our test case functions and we'll automatically have wallet objects with specific attributes without having to recreate them inside of each testing function that we want to use them in.

```python
def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test setting_initial_amount(wallet):
    assert wallet.balance == 20
```

Running `pytest --fixtures` from the command line will give us a summary of all of the fixtures defined in that directory. The output of this command also shows us the docstrings of our fixtures. Yet another way that docstrings can provide value.

## Docstring Best Practices

There are a few popular ways of organizing docstrings. Some of the most important information to include is:

* The parameters and datatypes of the parameters that the function accepts as input.
* Definitions of what each parameter does.
* What is returned from the function and its accompanying data type(s).

Really your docstring can be however you want it to be as long as you think it's informative. Two popular docstring formats are the "Numpy" and "Google" formats, but there are ho hard and fast rules here.

For more info on python documentation best practices:

[Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/#docstring-formats)

## `README.md` file best practices

[Markdown Cheat Sheet](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf)

## Choosing a License

* [choosealicense.com](https://choosealicense.com/)

* [Mike Rossetti all about Software Licensing](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/software/licensing.md)
