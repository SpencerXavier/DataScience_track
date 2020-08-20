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
