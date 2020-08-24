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
1. part1
```
key-value pair
dict["key"] will return the value
list.index("keyword") will return the index number
dict.keys() will return all keys
dict.values() will return all key
```
2. part2
```
'keyword' in dict will return boolean
del(dict["key"] will remove key and values
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







