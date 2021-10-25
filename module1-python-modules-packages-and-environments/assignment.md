# MODULE 1 Project - Python Modules, Packages, and Environments

Places for your code (and dependencies) to live.

## **Learning Objectives**
* Understand and follow Python namespaces and imports
* Create a Python package and install dependencies in a dedicated environment

## **Before Lecture**

Please install the following before our Guided Project. Instructions can be found [here](https://github.com/LambdaSchool/DS-Unit-3-Setup).

- VS Code
- Git Bash
- Python
- Pipenv

In order to pursue today's stretch goal's you'll also want to have installed the following. Instructions can be found towards the bottom of [this document](https://github.com/LambdaSchool/

- git (if on Mac). If you're on Windows git is installed automatically with Git Bash.
- Set up an SSH key on your local machine.
- Add the SSH key to your GitHub account.

## **Assignment**

1) Create your own lambdata-yourusername package (structure your package the same way it was done in the lecture)  
2) Implement at least 2 of the following "helper" utility functions in a `helper_functions.py` module:

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
  
* `def addy_split(addy_series)`: Split addresses into three columns (df['city'], df['state'], and df['zip']) - you can use [regex](https://docs.python.org/3/library/re.html) to detect the format and pull out important pieces.

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

## **Resources and Stretch Goals**

#### Stretch:
1. Register for a test PyPI account
2. Publish your package as lambdata-yourusername (to avoid conflicts)
3. Start a Python notebook, and install your package with !pip install --index-url [https://test.pypi.org/simple/](https://test.pypi.org/simple/) lambdata-yourusername
4. import lambdata_yourusername as lambdata in your notebook, and try it out!

We suggest using [Twine](https://pypi.org/project/twine/#:~:text=Twine%20is%20a%20utility%20for,and%20links%20to%20additional%20resources.) for uploading your pypi packages. Twine itself can be installed with pipenv install -d twine so it is a development dependency.

You might find the command below important in uploading: twine upload --repository-url [https://test.pypi.org/legacy/](https://test.pypi.org/legacy/) dist/*

#### Resources:

Many of the utility functions can be implemented with the right clever calls to pandas, numpy, and other libraries - that's fine! Use those as dependencies. There's still value in a package that encapsulates more complicated libraries and exposes streamlined functionality with a simplified API. If you would like to generate some fake data check out the [Faker python package](https://faker.readthedocs.io/en/master/) to craft specific data types.

Also note - there's a lot more than 2 ideas to choose from for your helper functions. Throughout the week, whenever you have finished the daily assignment baseline, you can always come back and add more functionality to your lambdata (including ideas of your own)!

Check out steps 3 to 6 if you would like to attempt a stretch goal. I would recommend trying to figure this out on your own! Remember to check documentation and Google!

The [official Python packaging tutorial](https://packaging.python.org/tutorials/packaging-projects/) can help you if you get stuck with the assignment. Make sure to use Test PyPI! If you get through all the steps, try some of the following stretch goals:


* Check out the source code for [pandas](https://github.com/pandas-dev/pandas), and see if you can make sense of it. Try to find the actual logic behind specific functions you use (e.g. `pd.DataFrame`, `df.replace`, etc.). Reading source code is challenging, especially from large codebases, but it's a skill that will help you debug and fix real issues in professional situations.
* Explore [PyPI](https://pypi.org/), the Python Package Index - this is where `pip` (the official base Python package installer, which both Anaconda and `pipenv` build on) gets things from by default. For now stick with Test PyPI for your own publishing, but you can work to make things "real"!