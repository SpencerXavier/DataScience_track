# project pipeline
1. read csv
```
super_bowls = pd.read_csv('datasets/super_bowls.csv')
display(super_bowls.head())
```

2. taking note of dataset issues
```
tv.info()
```

3-4. Combined points and  Point difference  distribution and data visulization
```
from matplotlib import pyplot as plt
%matplotlib inline
plt.style.use('seaborn')

combined_pts = super_bowls['combined_pts']
plt.hist(combined_pts)
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()
```

5. Do blowouts translate to lost viewers? [speculation with sns and  linear regression model]
```
# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')
import seaborn as sns
# Create a scatter plot with a linear regression model fit
sns.regplot(x= 'difference_pts', y= 'share_household', data=games_tv)
ps.使用方法：subplot（m,n,p）或者subplot（m n p）。
subplot是将多个图画到一个平面上的工具。 其中，m表示是图排成m行，n表示图排成n列，也就是整个figure中有n个图是排成一行的，一共m行，如果m=2就是表示2行图。 p表示图所在的位置，p=1表示从左到右从上到下的第一个位置。

```
6. Viewership and the ad industry over time [ check your speculation]
```

# Create a figure with 3x1 subplot and activate the top subplot
plt.subplot(3, 1, 1) 
plt.plot(tv.super_bowl, tv.avg_us_viewers, color='#648FFF')
plt.title('Average Number of US Viewers')

# Activate the middle subplot
plt.subplot(3, 1, 2)
plt.plot(tv.super_bowl, tv.rating_household, color='#DC267F')
plt.title('Household Rating')

# Activate the bottom subplot
plt.subplot(3, 1, 3)
plt.plot(tv.super_bowl, tv.ad_cost, color='#FFB000')
plt.title('Ad Cost')
plt.xlabel('SUPER BOWL')

# Improve the spacing between subplots
plt.tight_layout()

```
7.
```

halftime_musicians[0:27]
```










