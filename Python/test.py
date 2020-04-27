#imports
import numpy as np
import pandas as pd


#using Numpy
a = np.array([1,2,3,4,5,6,7,8])
#this will print out elements of a that are > 4
print(a[a>4])
#print(a)
#should print out the array.
print(a.dtype)

items = [1,2,3,4,5]
def inc(x): return x+1
list(map(inc,items))

#print(items)

#using Pandas
#here, I will create a series
#You can define a new series starting with NumPy arrays or with an existing series .
series = pd.Series([12,-4,7,9,9,9,7], index=['a','b','c','d','e','f','g'])
#print(series.index)
#print(series.values)
series['b'] = -456
#print(series)

pdsimple=pd.Series(series)
#print(pdsimple)

series[series > 0]

#print(np.log(series))
#print(series.unique())
#print("-----")
#print(series.value_counts())

serd = pd.Series([1,0,2,1,2,3], index=['white','white','blue','green','green','yellow'])

testisin = serd.isin([0,3])
print(testisin)
print("---------------")
snull = pd.Series([6,5,4,np.NaN,14])
print(snull.isnull())
print("-------------")
print(snull.notnull())

# define a dataframe.
dfdata = {'color' : ['blue', 'green', 'yellow', 'red', 'white'],\
'object' : ['ball','pen','pencil','paper','mug'],\
'price' : [1.2,1.0,2.2,0.9,1.7]}

mydf = pd.DataFrame(dfdata)
print (mydf)