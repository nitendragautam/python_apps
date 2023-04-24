import pandas as pd 

print(pd.__version__)

"""
pandas is a column-oriented data analysis API. It's a great tool for handling and analyzing input data,
 and many ML frameworks support pandas data structures as inputs. 

The primary data structures in pandas are implemented as two classes:
DataFrame, which you can imagine as a relational data table, with rows and named columns.

Series, which is a single column. A DataFrame contains one or more Series and a name for each Series.
The data frame is a commonly used abstraction for data manipulation. Similar implementations exist in Spark and R.

"""

#Construct a series
city_names = pd.Series(['San Fransisco', 'San Jose','Sacremento'])

"""
DataFrame objects can be created by passing a dict mapping string column names
 to their respective Series. If the Series don't match in length,
 missing values are filled with special NA/NaN values
"""

city_population = pd.Series([852469, 1015785, 485199])

#Create a data fram from dictionary
city_df=pd.DataFrame({'city_name': city_names, 'Population':city_population})

print(city_df)


# We can load an entire file into an dataframe

cal_housing_df = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")

#Describe an dataframe
# DataFrame.describe to show interesting statistics about a DataFrame.
print(cal_housing_df.describe())

# DataFrame.head, which displays the first few records of a DataFrame:
print(cal_housing_df.head())


"""
Another powerful feature of pandas is graphing. 
For example, DataFrame.hist lets you quickly study the distribution of values in a column:
"""
