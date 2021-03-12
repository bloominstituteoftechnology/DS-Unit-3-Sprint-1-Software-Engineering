from mymodule.helper_functions import Data
import pandas as pd

import seaborn as sns

iris = sns.load_dataset("iris")
iris.head()

print(Data.null_count(iris))
print(Data.list_2_series(iris, pd.DataFrame(iris["sepal_length"])))

pass
