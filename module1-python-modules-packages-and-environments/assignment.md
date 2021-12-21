# MODULE 1 Project - Python Modules, Packages, and Environments

## Setup

You will need the following tools before you are able to complete the assignment. Instructions can be found [here](https://github.com/LambdaSchool/DS-Unit-3-Setup).

* VS Code
* Git Bash
* Python
* Pipenv

In order to pursue today's stretch goal's you'll also want to have installed the following. Instructions can be found towards the bottom of the [Unit 3 Setup document](https://github.com/bloominstituteoftechnology/DS-Unit-3-Setup/blob/main/README.md)

* git (if on Mac). If you're on Windows git is installed automatically with Git Bash.
* Set up an SSH key on your local machine.
* Add the SSH key to your GitHub account.

## Assignment

### Part 1

Create your own `bloomdata-yourusername` package (structure your package the same way it was done in the lecture). Make sure that you're working from a virtual environment and that you have an outer project-level folder and an inner project sub-folder.

### Part 2

Implement the following "helper" utility functions in a `helper__functions.py` module. These code tasks will give you familiarity with some techniques that will be helpful for the sprint challenge! NumPy will be a useful dependency for generating certain kinds of random numbers.

1) `def random_phrase():` Write a function that can create a random combination of adjectives and nouns. When called the function should return a single string containing a **randomly selected** adjective and noun pair:

**Adjectives**

`['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']`

**Nouns**

`['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']`

For example:

`>>> random_phrase()`

> 'large tree'

`>>> random_phrase()`

> 'blue bicycle'

---

2) `def random_float(min_val, max_val):`

Write a function that returns a random **float** sampled from a uniform distribution with a minimum value of `min_val` and a maximum value of `max_val`.

---

3) `def random_bowling_score():`

Write a function that when called returns a random **integer** between 0 and 300.

---

4) `def silly_tuple():`

Write a function that when called returns a tuple that contains three items. the first should be a random adjective-noun string, the second should be a float representing a star-rating between 1 and 5 - rounded to one decimal place. And the third item should be a random bowling score between 0 and 300.

Examples:

`>>> silly_tuple()`

> ('blue house', 4.2, 187)

`>>> silly_tuple()`

> ('potent phone', 0.7, 83)

5) `def silly_tuple_list(num_tuples):`

Write a function that returns a list filled with a designated number of silly tuples.

`>>> silly_tuple_list(2)`

> [('blue house', 4.2, 187), ('potent phone', 0.7, 83)]

Please note how all of the above functions build on each other and use previous functions that have been written to complete their work. These are examples of "helper functions." Helper functions are functions that don't necessarily exist to be called directly, but exist to be used by other functions to complete their work.

### Part 3 

Implement at least 1 of the following "helper" utility functions in a `helper_functions.py` module. These code tasks are more advanced and are more robust to what you would find inside of a package that you  import and use as a tool during another project. You can use Pandas and/or NumPy functions to help you 

* `def null_count(df)`: Check a dataframe for nulls and return the number of missing values.

Example Input (df = pd.DataFrame):
> | column 0    | column 1    | column 2    |
> | ----------- | ----------- | ----------- |
> | NaN         | 9           | 10          |
> | 4           | NaN         | 2           |
> | 3           | NaN         | 2           |

Function:
> `null_count(df)`

Expected Output (int):
> `3`

* `def train_test_split(df, frac)`: Create a Train/Test split function for a dataframe and returns both the Training and Testing sets. `Frac` referes to the precent of data you would like to set aside for training.

Example Input (df = pd.DataFrame):
> | column 0    | column 1    | column 2    |
> | ----------- | ----------- | ----------- |
> | 0           | 1           | 2           |
> | 3           | 4           | 5           |
> | 6           | 7           | 8           |

Function:
> `train_test_split(df, frac=0.2)`

Expected Output (tuple of two dataframes):
  (
> | column 0    | column 1    | column 2    | 
> | ----------- | ----------- | ----------- |
> | 3           | 4           | 5           |
  ,
> | column 0    | column 1    | column 2    | 
> | ----------- | ----------- | ----------- | 
> | 0           | 1           | 2           |
> | 6           | 7           | 8           |
  )
    
* `def randomize(df, seed)`: Develop a randomization function that randomizes all of a dataframes cells then returns that randomized dataframe. This function should also take a random seed for reproducible randomization.

Example Input (df = pd.DataFrame):
> | column 0    | column 1    | column 2    |
> | ----------- | ----------- | ----------- |
> | 0           | 1           | 2           |
> | 3           | 4           | 5           |
> | 6           | 7           | 8           |

Function:
> `randomize(df, seed=101)`

Expected Output (pd.Dataframe): 
> | column 0    | column 1    | column 2    |
> | ----------- | ----------- | ----------- |
> | 2           | 5           | 8           |
> | 0           | 3           | 6           |
> | 1           | 4           | 7           |
  
* `def addy_split(addy_series):` Split addresses into three columns (df['city'], df['state'], and df['zip']) - you can use [regex](https://docs.python.org/3/library/re.html) to detect the format and pull out important pieces.

Example Input (addy_series = pd.Series):
> | address                                    |
> | ------------------------------------------ |
> | 890 Jennifer Brooks\nNorth Janet, WY 24785 |
> | 8394 Kim Meadow\nDarrenville, AK 27389     |
> | 379 Cain Plaza\nJosephburgh, WY 06332      |
> | 5303 Tina Hill\nAudreychester, VA 97036    |

Function:
> `addy_split(addy_series)`

Expected Output (pd.Dataframe): 
> | city          | state       | zip         |
> | ------------- | ----------- | ----------- |
> | North Janet   | WY          | 24785       |
> | Darrenville   | AK          | 27389       |
> | Josephburgh   | WY          | 06332       |
> | Audreychester | VA          | 97036       |
  
* `def abbr_2_st(state_series, abbr_2_st=True)`: Return a new column with the full name from a State abbreviation column. An input of FL would return Florida. This function should also take a boolean (`abbr_2_state`) and when `False` takes full state names and return state abbreviations. An input of Florida would return Fl.

Example Input (state_series = pd.Series):
> | states     |
> | ---------- |
> | Alabama    |
> | Arizona    |
> | California |
> | Delaware   |
> | Ohio       |

Function:
> `abbr_2_st(state_series, abbr_2_st=True)`

Expected Output (pd.Series): 
> | st_2_abbr     |
> | ------------- |
> | AL            |
> | AZ            |
> | CA            |
> | DE            |
> | OH            |
  
* `def list_2_series(list_2_series, df)`: Single function to take a list and dataframe then turn the list into a series and add it to the inputted dataframe as a new column.

Example Input (list):
> `[0, 1, 2]`

Function:
> `list_2_series(list, pd.DataFrame())`

Expected Output (pd.Dataframe):  
> | list          |
> | ------------- |
> | 0             |
> | 1             |
> | 2             |

* `def rm_outlier(df)`: A 1.5*Interquartile range outlier detection/removal function that gets rid of outlying rows and returns that outlier cleaned dataframe.

Example Input (df = pd.DataFrame):
> | column 0    | column 1    | column 2    |
> | ----------- | ----------- | ----------- |
> | 0           | 1           | 2           |
> | 3           | 850         | 5           |
> | 6           | 7           | 8           |

Function:
> `rm_outlier(df)`

Example Output (df = pd.DataFrame):
> | column 0    | column 1    | column 2    |
> | ----------- | ----------- | ----------- |
> | 0           | 1           | 2           |
> | 6           | 7           | 8           |

* `def split_dates(date_series)`: Function to split dates of format "MM/DD/YYYY" into multiple columns (df['month'], df['day'], df['year']) and then return the same dataframe with those additional columns.
 
Example Input (date_series = pd.Series):
  > | column 0    |
  > | ----------- |
  > | 02/28/2006  |
  > | 03/09/2010  |
  > | 06/12/1850  |

  Function:
  > `split_dates(date_series)`

  Example Output (df = pd.DataFrame):
  > | month       | day         | year        |
  > | ----------- | ----------- | ----------- |
  > | 02          | 28          | 2006        |
  > | 03          | 09          | 2010        |
  > | 06          | 12          | 1850        |
