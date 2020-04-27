# Helpful Pandas Notes.

> by Joel Rossol

## Installation

As usual, it is easy to install pandas via PIP

```bash
pip install pandas
```

And then include it in your project using the following syntax

```python
import pandas as pd
```



## Creating Data Types in Pandas

### Creating a Series in Pandas

One of the basic data types in Pandas is a 'series'.  Think of it as an array with an index.

```python
myseries = pd.Series([12,-4,7,9], index=['a','b','c','d'])
```

You can see output of that series by using the following functions:

```python
>>>myseries.values
array([12, -4,  7,  9])
>>>myseries.index()
Index(['a', 'b', 'c', 'd'], dtype='object')
```

You can also use a NumPy array as the source for a series:

```python
myarray = np.array([1,2,3,4])
pandasseries = pd.Series(myarray)
```

Series have some interesting methods that do not apply to data frames.

myseries.value_counts() and...

myseries.unique()

```python
>>> myseries.value_counts()
 7     1
 12    1
-4     1
 9     1
 
 >>> myseries.unique()
array([12, -4,  7,  9])
```

value_counts() returns a more structured table... while .unique() just spits out an array of unique values. (in no particular order.)



#### Pandas Dictionary Examples

in Pandas, a series and a dictionary are similar.  

so a dictionary would include indexes for you as so:

mydict = {'red':2000, 'blue':1000, 'yellow': 500}

series use the {} instead of ().

you can say myseries = pd.Series(mydict) to create series out of dicts.



### All the DataFrame stuff!

Pandas DataFrames are like giant excel tables.  You have rows, columns, column headers and indices.  

The format for creating a dataframe is as follows:

frame = pd.DataFrame( {data}, \
											index=[{indices}], \
											columns=[{column names}])

You have a **data object**, an **index**, and **columns**. Here is a code example:

```python
>>>mydataframe = pd.DataFrame(np.arange(16).reshape((4,4)), index=['Player 1','Player 2','Player 3','Player 4'], columns=['course 1','course 2','sawgrass','PGA tour course'])

>>> mydataframe
          course 1  course 2  sawgrass  PGA tour course
Player 1         0         1         2                3
Player 2         4         5         6                7
Player 3         8         9        10               11
Player 4        12        13        14               15
```

You can get specific values out of your dataframe by using the following methods:

```python
>>>mydataframe.columns
Index(['course 1', 'course 2', 'sawgrass', 'PGA tour course'], dtype='object')

>>>mydataframe.values
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])

>>>mydataframe.index
Index(['Player 1', 'Player 2', 'Player 3', 'Player 4'], dtype='object')

>>>mydataframe.loc['Player 1'] #this is like grabbing a ROW.
course 1           0
course 2           1
sawgrass           2
PGA tour course    3
Name: Player 1, dtype: int64

>>>mydataframe['sawgrass'] # gets you the values in a *column*
Player 1     2
Player 2     6
Player 3    10
Player 4    14
Name: sawgrass, dtype: int64
```

You can also give your indexes and columns descriptive names.

```python
>>> mydataframe.index.name = 'players'
>>> mydataframe.columns.name = 'courses'
>>> mydataframe
courses   course 1  course 2  sawgrass  PGA tour course
players
Player 1         0         1         2                3
Player 2         4         5         6                7
Player 3         8         9        10               11
Player 4        12        13        14               15

```



#### Adding / deleting columns and populating data.

To add, just append a free-hand column to the frame.

```python
frame['newcolname'] = 123. ##this will make every rwo in that column = 123
#<or>
frame['newcolname'] = [1,2,3,4,5]

```

to delete a column, use the '**del**' keyword.

```python
del mydataframe['columnname']
```



#### Filtering data in a dataframe

In order to filter, you call your frame; pass the same frame into a logical box and get a frame back that has all values that meet the given criteria.  Any values that do not meet the criteria come back as NaN.

```python
>>> mydataframe[mydataframe < 4]
courses   course 1  course 2  sawgrass  PGA tour course
players
Player 1       0.0       1.0       2.0              3.0
Player 2       NaN       NaN       NaN              NaN
Player 3       NaN       NaN       NaN              NaN
Player 4       NaN       NaN       NaN              NaN
#isn't that a bit odd behavior? How else would you do it?
```

.isin() also works on dataframes.



#### methods on Pandas Indexes

series.idxmin()

series.idxmax()

-- need to flush these out more. 

#### Arithmetic methods (add/subtract/multiply/divide)

You can apply the following arithmatic to Pandas data frames using the following functions:

```python
#add 2 data frames together.
df.add(frame2 {or number})
df.sub()
#it is a bit odd that 
>>>mydataframe + 2  #this also works.

#subtract, divide, and multiply frames.
df.sub()/.div().mul()

#running sum() sums the value of each column as a total.  If you want to add up by row, that requires a different approach (below).
>>>mdf.sum()
courses
course 1           24
course 2           28
sawgrass           32
PGA tour course    36
dtype: int64

>>>Df.mean()/.median()/.mode()

>>>df.describe() //this one give you all the calculations at once.
```



#### Sorting Data in a frame

You can sort data in a dataframe in a number of ways using the following functions:

```python
frame.sort_index()
frame.sort_index(axis=1)
frame.sort_values(by='colname')
frame.sort_values(by=['col1','col2'])
series.rank()
//what is the difference between ranking and soting?
```



#### Running calculations on a dataframe by row or by column

functions by row or column

Def range(x):

​	return x.max() - x.min()

frame.apply(range, axis=1/0)

//use .apply() to apply custom logic to a data frame.



#### Correlation & Covariance

Var.corr(sequence)

Var.cov(sequence)

frame.corr() or frame.cov()

frame.corrwith(). //what does this do?





NAN

#### Handling Null values

You can explicitly add null values by using "np.NAN" in any array/series.

You can essentially query for And then use the series.isnull() and series.notnull()  functions.

