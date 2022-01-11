# Object Oriented Programming in Python

**Object Oriented Programming** is a programming approach (sometimes called a "paradigm") that seeks to organize our code into bundles of variables and functions that are related to each other. These bundles of related variables and functions are called "objects." Objects can represent anything at all: people, students, animals, cars,` dataframes, machine learning algorithms, etc. 

Any code that we write about these entities we will bundle together in a data structure called a "class." A class organizes the variables and functions that are associated with an object all in one place for improved organization and also so that those variables and functions can interact to do something uesful. Lets look at a more concrete example.

You've already worked with lots of different objects so far, DataFrames for example. 

### Attributes

When we refer to the variables that are associated a certain object we call them "attributes".

Dataframes have attributes like: `.shape`, `.index`, `.dtypes`, etc. 

### Methods

When we refer to the functions that are associated a certain object we call them "methods".

Dataframes have methods like: `.describe()`, `.drop()`, `.head()`, `.isnull()`, `.to_csv()`, etc.

You can view a complete list of the attributes and methods associated with the DataFrame class in the [Pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html).

Notice that the attributes (variables) stored on the dataframe class don't require parentheses, whereas the methods (functions) do.

## Defining a class

### The class Keyword and UpperCamelCase

Let's create a class that can represents any vehicle. We will begin our class definition using the `class` keyword, just like how we use the `def` keyword when we're creating a function.

```
class Vehicle:
```

Whenever we write the name of the class (in this case `Vehicle`) the convention is that we should write it using "UpperCamelCase" this means that we will capitalize each word and put no spaces or underscores in its name. For example, if we were creating a class about BloomTech students we would write: `class BloomTechStudent:`

### Adding Class Attributes

What are some **attributes** that all vehicles have? Doors, wheels, seats, top speed, make, model, mileage, etc. If you had to list a vehicle that you wanted to sell on Craigslist what kind of information would you include in the listing? Those are its attributes.

We can associate **attributes** with a class by including them in something called the `__init__():` method "constructor". Inside of the parentheses of the init method (constructor) we will first pass a variable called `self` and then after that any other parameters that will be required when each new object is created. 

Any attributes that we know will be the same for all objects we create we can declare loosely above the `__init__()` method.

```
class Vehicle:
    # attributes that will initially be the same for all objects
    wheels = 4

    # constructor
    def __init__(self, make, model, year, mileage, color):
        # initial values of the attributes
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.color = color
```

### Adding Class Methods

Now, what are some **functions** or behaviors that vehicles have? They drive, go forwards, reverse, turn, park, honk the horn, etc. We could include some methods that do these as well. 

We associate **methods** with a class by declaring those methods within the class definition but below the constructor (indented just like the body of a function). 

```
class Vehicle:
    # attributes that will initially be the same for all objects
    wheels = 4

    # constructor
    def __init__(self, make, model, year, mileage, color):
        # initial values of the attributes
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.color = color

    # instance method
    def honk(self):
        print("HOOONK!!!")
```
 
### The `self` Keyword

We attach any attributes that we want to exist on our class to the `self` keyword. Each different object that we create with our class will be its own entity and therefore will be able to have unique attributes associated with it.

Likewise, when we add a class method, the first parameter that we include is always `self` this will give the function access to any of the attributes of the class, should it need to use them or modify them in any way. Self refers to the specific instance of the class, not the class definition.

## Instantiating a class

A class definition is like a blueprint for an object, it isn't the object itself. Whenever we create an object from a class we call that "instantiation" or we say that we have "instantiated an object." We can instantiate (or create) a unique Vehicle object by calling the class and passing in initial the initial attributes that are required by the `__init__()` constructor.

```
my_car = Vehicle('Toyota', 'Camry', 2007, 248000, 'gray')
```

Instantiating a class will return to us an object which we can then save to a variable. Once saved to a variable we can access the attributes and methods. 

Think of a class like a mold for casting objects, and the object itself as the objects that get created from the mold. The raw materials that we pour into the mold are like the variables that we provide when we initialize the object. 

![molds can create many objects](/images/mold-casting.jpeg)

## `if __name__ == "__main__":`

It can be a pain to write the same commands over and over in a REPL to test things out. Sometimes we might want to run the file that holds our class as a script and simply include lines at the bottom of the file to test our code. If we put code at the bottom of the file under this if statement above, then it will only be run when the file is read as a script and not when it is imported. 

## Inheriting from another class

We can have many type of objects, but specifically objects that **inherit** from other objects. Let's make a child class that inherits from `Vehicle`. This class will be a more specific kind of Vehicle. Let's make a Car. We would create a child class when we need to define an object that is more specific than the parent class.

```
class Car(Vehicle):
    pass
```

Notice that we pass in the name of the parent class inside of parentheses after the new class name. If we "stub out" our child class by just putting the `pass` keyword inside of it, then our Car class will be identical to the Vehicle class but will have a different name, the object will be the same but have the datatype of "Car." At this point the Car class is inheriting all of the attriubutes and methods from the Vehicle class. It is not modifying them or overriding them in any way. 

### Extending the attributes of the parent class

When we want to add an additional attribute to the child class that the parent class doesn't have we can use the `super().init__()` statement to quickly add all of the attributes of the parent class to self. Then we only have to explicitly add the new attribute to the child class. All of the other attributes are **inherited** from the parent. 

```
class Convertible(Car):

    def __init__(self, make, model, year, mileage):
        # give the Car all of the Vehicle properties
        super().__init__(title, ismajor)
        # plus a new attribute that only applies to cars
        self.ismajor= False
```



### Adding new methods of to the child class

When we want to add new methods to the child class we can simply include them below the attribute section just like we would normally. The child will inherit all of the methods from the parent class and will also have its own methods that are defined here.

```
class Car(Vehicle):
    def __init__(self, make, model, year, mileage, color, style):
        # give the Car all of the Vehicle properties
        super().__init__(make, model, year, mileage, color)
        # pluse a new attribute that only applies to cars
        self.style = style

    # We can also give our class new methods that don't exist on the vehicle class
    def description(self):
        print("I am a", self.make, self.model, "with", self.mileage, "miles. I am a", self.color, self.style + '.')
```

Inside my REPL I can test out my new Car class to see that it has both the methods from the parent class as well as the new `description()` method that we have added here. In this example, my python file is called `Vehicle.py`

```
>>> import Vehicle
>>> my_car = Vehicle.Car('Toyota', 'Camry', 2007, 248000, 'gray', 'sedan')
>>> my_car.honk()
HOOONK!!!
>>> my_car.description()
I am a Toyota Camry with 248000 miles. I am a gray sedan.
>>> 
```

One of the primary advantages of classes is minimizing code reuse through inheritance. 

# PEP8 Style Guidelines for Python code. 

PEP8 is a whole bunch of strong suggestions (called conventions) for how you should format your Python code to make it more readable and consistent with the Python code that others write. The more we as pythonistas adhere to similar conventions the easier it will be for us to read each others code and collaborate on our work.

[Click here for the full PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/)

The big idea with PEP8 is that "readability matters" and will make your code better. However, it's a lot of rules and suggestions to keep in mind and apply to your code at all times. Is there an easier way?

## PEP8 Code Linters

A linter is an application that scans your python code as you write it and pops up helpful warnings and error messages telling how you can improve. Linters generally help you catch syntax errors before you run your code, but can also be helpful at suggesting revisions to your code that will put it more in line with PEP8. 

You can turn on automatic code linting in VSCode by:

1) Open the command pane with `[Ctrl]+[Shift]+[p]`
2) Search for "Python Enable/Disable Linting"
3) Make sure linting is enabled
4) Open the command pane again `[Ctrl]+[Shift]+[p]`
5) Search for "Python: Select Linter" I recommend flake8 or pylint. You can try out different ones to see what you like. The linting will happen whenever you save a file.

You can set your code to autoformat to PEP8 style guidelines as automatically every time you save a file by:

1) Open the command pane with `[Ctrl]+[Shift]+[p]`
2) Search for "Preferences"
3) Select "Preferences: Open User Settings"
4) The settings page is pretty long so you're going to want to do `[Ctrl] + f` to search for "settings page look for Search for "Format on Save". 
5) Make sure to check the box and then go back to your file, make some style mistakes and then save the file, they should correct automatically (for the most part - The linter can't add in doc strings to your functions for you).

