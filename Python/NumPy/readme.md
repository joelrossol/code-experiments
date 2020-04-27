# Helpful NumPy Notes.

> by Joel Rossol



## Importing Numpy

The basic import for Numpy.  You first need to install it via PIP, and then import it into your python project.

First, install NumPy on your system using PIP.

```bash
Pip install numpy
```

Then, use an import in your project to use the library.  Any usage will be np.{function_name()}

```python
import numpy as np
```



### Basic NumPy Functions 

There are a few generic NumPy functions that are helpful when working with {something}.

```python
np.array([1,2,3], dtype={})
np.ndim
np.size 
np.shape
np.zeros
np.ones((3,3)) #this will create an array 1, 1.5, 2, 2.5, etc...
np.arrange(0,10,.5)
np.linspace(1,10,.5) #almost the same, but the last argument is the number of values inbetween.
np.random.random() #here, you need to go into the '.random' module before you can call the random function
np.dtype.name
```

An Example of these functions in Real Life:

```python
npex = np.arange(0,20).reshape((3,3)) 
# creates a 3x3 table of nmbers
# gives you an array of...
# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14],
#        [15, 16, 17, 18, 19]])
```



#### Iterating through NumPy data sets

Here is a basic example, but not best practice:

```python
for row in var:
  print(row)
```

A better way to handle iterating through NumPy data would be:

```python
Np.apply_along_axis(function, axis=x, arr=arrayVar)
#this lets you use a custom function in the first argument that can do whatever processing you want.
```



#### Combining Arrays with NumPy

np.vstack((A,B)) -- adds on rows

np.hstack((A,B)) -- adds on columns

Np.column_stack((a,b,c)) //this creates a two-dimensional array

np.row_stack((a,b,c)) //this creates a two-dimensional array



#### Copy Data in NumPy

New = var.copy()



#### Giving Names to Columns

Np.dtype.names = ('id', 'title', 'quantity') //etc.



Saving & Loading

np.save('file name', data)

loadvar = np.load('saved_data.npy')



#### Loading external data sources

Here is an example of how you would load a CSV file, for example

```python
externaldata = np.genfromtxt('file.csv',delimiter=',',names=True)
#3 arguments.  File name, delimiter, and column headers.
```



## Pandas

Installation

pip install pandas

\>>> s = pd.Series([12,-4,7,9], index=['a','b','c','d'])

\>>> s
a  12
b  -4
c   7
d   9
dtype: int64

s.values()

s.index()



arr = np.array([1,2,3,4])

S3 = pd.Series(arr)

You can define a series with an undefined value...

S2 = pd.Series([5,3,np.NaN,14])

And then use the series.isnull() and series.notnull()  functions.

------------

in Pandas, a series and a dictionary are siilar.

so a dictionary would include indexes for you as so:

mydict = {'red':2000, 'blue':1000, 'yellow': 500}

series use the {} instead of ().

you can say myseries = pd.Series(mydict) to create series out of dicts.

frame = pd.DataFrame(data, columns=['widget','price'])

frame3 = pd.DataFrame(np.arange(16).reshape((4,4)), index=['red','blue','yellow','white'], columns=['ball','pen','pencil','paper'])

\>>> frame3

​    ball pen pencil paper

red    0  1    2   3

blue    4  5    6   7

yellow   8  9   10   11

white   12  13   14   15



frame.columns

frame.values

frame.index

frame['column-name'] //gets you the values in a column



use LOC to get a specific location within a dataframe (a row)

frame.loc[2, 4]

Select a range of data from a df 

```python
// frame[1:4] or... frame['object'][4]

>>> frame.index.name = 'id'
>>> frame.columns.name = 'item'
>>> frame
item   color  object  price
id
0       blue    ball    1.2
1      green     pen    1.0
2     yellow  pencil    0.6
3        red   paper    0.9
4      white     mug    1.7
```



#### Adding / deleting columns and populating data.

you can do

frame['newcolname'] = 123. //this will make every rwo in that column = 123

to pass in specific values for each row, use an array liike so:

frame['newcolname'] = [1,2,3,4,5]

del frame['columnname']



#### filtering

frame[frame < 1.2]

//gets all rows with any value less than 1.2

```python
>>> nestdict = {'red':{2012: 22, 2013: 33},
...             'white':{2011: 13, 2012: 22, 2013: 16},
...             'blue': {2011: 17, 2012: 27, 2013: 18}}
>>> frame2 = pd.DataFrame(nestdict)
>>> frame2
      blue    red  white
2011    17    NaN     13
2012    27   22.0     22
2013    18   33.0     16
```

#### methods on Pandas Indexes

series.idxmin()

series.idxmax()



#### Arithmetic methods

df.add(frame2)

df.sub()

df.div()

df.mul()

Df.sum()

Df.mean()

df.describe() //this one give you all the calculations at once.



frame.sort_index()

frame.sort_index(axis=1)

frame.sort_values(by='colname')

frame.sort_values(by=['col1','col2'])

series.rank()

//what is the difference between ranking and soting?





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



