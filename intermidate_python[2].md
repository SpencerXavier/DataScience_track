# Basic Plots with Matplotlib

##  goal: data visualiztion
* Basic Plots with Matplotlib : remember to plt.show()
1. line plot
```
plt.plot(x,y)
plt.show()
```
2. scatter plot
```
plt.scatter(x,y,s = size, c = color)
plt.show()
```
3. histogram plot
```
plt.hist(values, bins = 10, ...)
bins = how many columns
```
4. change axis scale,name,title,ticks,text
```
plt.xscale('log')
plt.xlabel('name')
plt.ylabel('name')
plt.title('Title Name')
plt.yticks([0,2,4,6,8,10], display names)
plt.text(xloc,ylocation,'text')

```
5. ps
```
help(plt.hist) to explore attributes
plt.clf() = clean up
list.index(2030)可以得到該值的index
```

# Dictionary
ps. list review
```
list.index("keyword") will return the index number
list[index] will return value

```

1. part1
```
key-value pair
dict["key"] will return the value
del(dict["key"] will remove key and values
'keyword' in dict will return boolean

dict.keys() will return all keys
dict.values() will return all key
```
2. part2
```
ps. difference between lists and dictionary
List: Index by range of number
Dict: Index by unique keys
```

3. part3
```
Add new key and value : dict[new_key] = 'new_value'
Adding two same keys will display last one(meaning update), but contain both in dict.
List can contain list, dict can contain dict
to access dict in dict, use multiple [ ][ ] ,also for adding
```

# pandas

1. part 1
```
row = observations
column = variable
(column - row)

numpy array : only one data type
Pandas : high level data manipulation tool, built on Numpy

```
2. part2
```
import pandas as pd
dict = pd.DataFrame(dict)
will create automatic label

dataframe 的index :dataframe.index = [list or ndarray]
data['column name'] = column access
data['slicing number'] = row access

dataframe 的coloumn : dataframe['column_name'] will return value with Pandas Series
dataframe 的coloumn : dataframe[['column_name']] will return value with  Pandas DataFrame
multiple dataframe 的coloumn(row,index) : use loc or iloc
row access : data.loc[[rows name or index]]
column access : data.loc[:,'[column names]]
row and column : data.loc[[index], [column names]]


```

3. part3 - CSV
```
file = pd.read_csv('file path', index_col = 0)
will create automatic index column
use index_col = 0 means first column contain row indexes
```

# Logic, Control Flow and Filtering 
1. comparison operators
```
array > conditions = return boolean
array[array > conditions] = return result

string comparison : according to the alphabet

```
2. boolean opeartor
```
AND, OR, NOT
to compare array, use np.logical
np.logical_and/or(array1, array2)
np.logical_not(array1)

To return True values :
array[np.logical_and(condition)]
```
3. if, elif, else
```
if condition :
    expression
elif condition :
    expression
else :
    expression
No indentation to exit statement
```


















