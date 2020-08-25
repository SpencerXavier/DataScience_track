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
4. Flitering Pandas DataFrame
```
3 Steps
1.Select the corresponding column
2.Set conditions on column
3.Use result(To return True values :) to select rows

data[ data [ column ] > x ]

```
# Loops
1. While Loop
```
print default new line
print(x, end = ' ') will be space sepearate

while condition :
     expression
```

2. For Loop
```
for var in seq:
    expression
ps. string can also be iterated.
```

3. For loop
```
for index, x in enumerate(list)
    print(index,x)

enumerate(list,start=0) default start=0

```
4. data structure: foor loop with Looping Data Structures, Part 1 (DICT & Array)
```
1.Dictionary

method

To loop a dictionary,
use dict.items()
for key, value in dict.items():
    print(key,value)
Otherwise will causing errors

2.NumPy Arrays

function

To loop an array
1D is ok
2D will need nditer
for vlaue in np.nditer(array):
    print(value)
Otherwise will causing two outputs

```
5. Looping Data Structures, Part 2 (DataFrame)
```
DataFrame.iterrows():

for x in DataFrame:
    print(x)
this will print column

for x, y in DataFrame.iterrows():
    print(x)
    print(y)

x will be label
y will be row and data for each column
(index, Series) 

ps. specificy on row you want to print which column 
print(label+ row['column'])
ps.add  column
a.Use Apply()

DataFrame['new column'] = DataFrame['old column'].apply(function)

b.use for loop

for label, row in DataFrame.iterrows():
     DataFrame.loc[label, 'new column'] = function(row['old column'])

```
# Random Numbers
1. Random Numbers
```
np.random.seed(number)
np.random.rand()
will generate a random number from 0 ~ 1



can also manually set the seed
np.random.seed(number)
same seed = same random number (to ensure Reproducibility)

np.random.rand(x,y) will create an array with x rows, y column
np.random.randint(x,y) will create a random number between x and y

```
2. Random walk
```
create an empty list to append list = [     ]
a.coin toss
step 1: Print out Process (Random Steps)

for x in range(times):
conin = np.random.randint(0,2)
    if condition1:
        list.append('expression1')
    if condition2:
        list.append('expression2)
        
ps.max(0,step-1) : step never goes below 0

```






