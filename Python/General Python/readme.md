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
