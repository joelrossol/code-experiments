# Helpful Python Notes.

> by Joel Rossol



#### Iterating through lists

```python
items = [1,3,5,7,9]
def inc(x): return x+1
list(map(inc,items))
[2, 3, 4, 5, 6]
```

You can do the same thing by creating a lambda function directly inside...

```python
items = [1,3,5,7,9]
list(map((lambda x: x+1),items))
```

Open question: what is the deal with lambda functions?  What makes them different than normal functions?

#### Helpful Functions 

reduce()

filter()

map(function, list) - basically just a function to iterate over a list using a function that will run whatever processes you want on the list.



#### Basic Functions

```python
def inc(x): return x+1
```

would be the same as (in JS)

```javascript
function(x){
	return x + 1;
}
```





#### Python Dictionaries

in Pandas, a series and a dictionary are similar.  A dictionary would include indexes for you as so:

```python
>>>mydict = {'red':2000, 'blue':1000, 'yellow': 500}
```

Dictionaries use the {} instead of ().

Dictionaries are good for key/value pairs.

you can say myseries = pd.Series(mydict) to create series out of dicts.

```python
import pandas as pd

countries = ['United States', 'Germany', 'Japan', 'India', 'Russia', 'Canada', 'Egypt']
needslicense =  [True, True, True, False, True, True, True]
carsperthousand = [809, 731, 588, 18, 200, 70, 45]
my_cars_dict = {'country': countries,
           'needs_license': needslicense,
           'cars_per_thou': carsperthousand }
 
# Build a DataFrame cars from my_cars_dict
carinfo = pd.DataFrame(my_cars_dict)
print(cars)
```

