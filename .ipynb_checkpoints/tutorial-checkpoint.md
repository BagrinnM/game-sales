# Tutorial: Data Processing and Visualization Using the `game_sales` Package

## Getting Started

### 1. Import the package:

```python
import game_sales as gs
```

### 2. class `DataPreprocessing`

It contains the following functions:

| Function | Purpose |
| -------- | ------- |
| `__to_lowcase` | Converts column names to lowercase |
| `__data_to_Int64` | Converts year to Int64 format |
| `__esrb_to_user_friendly` | Decodes ESRB Rating |
| `__apply_esrb_conversion` | Applies the ESRB conversion |
| `__add_global_sales` | Adds a column with global sales |
| `isna_view` | Displays missing values as a percentage diagram |
| `get_data` | Returns the dataset |


Creating an object for data preprocessing and loading the dataset:

```python
data = gs.DataPreprocessing('file_path')
```

This object now contains an already processed data set, which can be used for further analysis and plotting.
Additionally, you can use the ***isna_view*** function to visualise the amount of missing data:

```python
data.isna_view()
```
<img src="https://github.com/Bagrinn96/game-sales/blob/main/img/isna_view.png?raw=true">

And also use the resulting dataset at will as a ‘DataFrame’ object:
***But it is important not to do this if you want to work with this package, because it is designed to work with an object of class DataPreprocessing:***


```python
data = data.get_data() # data - 'DataFrame' object
```
***But it is important not to do this if you want to work with this package, because it is designed to work with an object of class DataPreprocessing:***


### 3. class `DataDiscovery`

It contains the following functions:

| Function | Purpose |
| -------- | ------- |
| `release_by_year` | Displays game releases by year |
| `global_sales_by_platform` | Displays global sales by platform |
| `global_sales_by_genre` | Displays global sales by genre |
| `sales_dynamics_by_platform` | Displays sales dynamics by platform |
| `plot_sales_vs_scores` | Plots the correlation between sales and scores |
| `sales_by_esrb` | Displays sales based on ESRB rating |

+ release_by_year

```python
gs.DataDiscovery(data).release_by_year()
```

<img src="https://github.com/Bagrinn96/game-sales/blob/main/img/release_by_year.png?raw=true">

***P.s.*** Data for the years when the current platforms are relevant is important.

+ global_sales_by_platform, global_sales_by_genre

We use a box plot to determine the success of the platform. It's worth comparing the median sales on platforms and analyzing genre profitability on a box plot, comparing the median sales across each genre, and checking which of them is more stable and has a longer line of successfully selling games.

```python
gs.DataDiscovery(data).global_sales_by_genre()
gs.DataDiscovery(data).global_sales_by_platform()
```

<img src="https://github.com/Bagrinn96/game-sales/blob/main/img/global_sales_by_genre.png?raw=true">
<img src="https://github.com/Bagrinn96/game-sales/blob/main/img/global_sales_by_platform.png?raw=true">

***Conclusion:*** The genres with the highest and most stable median sales are Shooter. On the other hand, while the Action genre releases significantly more games than others, its median sales values are low, and in fact, 75% of all games in this genre have not sold more than 250k copies. In contrast, the median sales for Shooters are already at the 500k mark. Sports and Platform genres also show relatively good performance. As for platforms, the most successful and relevant at the moment are PS3, PS4 and XOne.

+ sales_dynamics_by_platform

```python
gs.DataDiscovery(data).sales_dynamics_by_platform()
```

<img src="https://github.com/Bagrinn96/game-sales/blob/main/img/sales_dynamics_by_platform.png?raw=true">

In 2016, 3 platforms lead in sales: PS4, XOne, and 3DS. HOWEVER, the data for 2016 is incomplete, and it is not worth concluding about a drop in sales. You can compare the growth/decline in other periods, such as 2015 vs. 2014.

+ plot_sales_vs_scores

```python
gs.DataDiscovery(data).plot_sales_vs_scores()
```

<img src="https://github.com/Bagrinn96/game-sales/blob/main/img/plot_sales_vs_scores.png?raw=true">
<img src="https://github.com/Bagrinn96/game-sales/blob/main/img/correlation.png?raw=true">

***Conclusion:*** The correlation between game reviews and sales for the PC platform is very weak. For other platforms, the correlation coefficient also does not reach any significant values.

+ sales_by_esrb

```python
gs.DataDiscovery(data).sales_by_esrb()
```

<img src="https://github.com/Bagrinn96/game-sales/blob/main/img/sales_by_esrb.png?raw=true">

***Conclusions:*** While the organization that assigns the age rating is based in America, in Japan most games are not assigned an age rating at all, so it does not affect sales. In Europe and North America, the best-selling games are in the 'For Everyone' category, followed by 'For Teens 13+' and 'For Adults'. 

## 4. class `TopFive`

You should organize the graphs for the TOP-5 section:

+ Choose a relevant period for analysis.
+ For each TOP-5 category, build 3 graphs side by side using subplots. It is optimal to compare three regions for each type of portrait together.
+ Create a "two-level heading" – one for all three graphs together and one for each individual graph.

```python
gs.TopFive(data).plot_top_genres_by_region()
gs.TopFive(data).plot_top_platforms_by_region()
```

<img src="https://github.com/Bagrinn96/game-sales/blob/main/img/plot_top_genres_by_region.png?raw=true">
<img src="https://github.com/Bagrinn96/game-sales/blob/main/img/plot_top_platforms_by_region.png?raw=true">

***Conclusion:*** The most popular platform in Japan was Nintendo DS, but games for it stopped being released as early as 2013. 
In Europe and North America, the most popular genres sind Action, Sports and Shooter. In Japan, the most preferred genre is Role-Playing followed by Action.

## Overall Conclusion

+ Currently, the most promising platforms for new games are XOne and PS4. If you plan to release a product for XOne, it does not make sense to spend money on advertising campaigns in Japan because Xbox consoles are practically not sold and are not popular there. On the contrary, it makes sense to invest more effort in advertising in North America. PS4 is a more cosmopolitan console, so it is also worth advertising your new product in Japan.
+ The most sold games are in the Action, Sports, and Shooter genres. However, based on the median value, the most copies are sold in the Shooter, Platform, and Sports genres. Among these genres, Sports and Shooter are in the top 5 in Europe, North America, and Japan, so these genres can be chosen. Or you could take a risk and make a good platformer, which is also popular in niche circles.
+ As for the age category, it is better to target a broader audience to get more sales. These are the "For Everyone" or "For Adults" categories.
+ There is no significant relationship between game scores and their sales.

***Conclusion:*** A potentially popular product for users in North America and Europe could be a shooter on the PlayStation 4 (or Xbox One).


