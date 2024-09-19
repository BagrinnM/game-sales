# game_sales: General Info

This package allows the analysis of video game sales data. Below is an example of the dataset structure:

|         Name         | Platform | Year of Release |  Genre   | Publisher | NA Sales | EU Sales | JP Sales | Critic Score | User Score | Rating |
|----------------------|----------|-----------------|----------|-----------|----------|----------|----------|--------------|------------|--------|
| New Super Mario Bros |   Wii    |      2009       | Platform | Nintendo  |   12.3   |   11.4   |   14.5   |     87.0     |    9.0     |   E    |

The dataset includes game sales data up to 2016, and the goal is to analyze the sales and suggest the best options for creating and releasing a new game in 2017.

## What This Package Can Do

### Data Preprocessing (***class `DataPreprocessing`***)
- Standardizes the dataset for analysis
- Adds a column with global sales
- Identifies missing data
- Decodes ESRB ratings

### Data Discovery (***class `DataDiscovery`***)
- Analyzes game releases by year
- Tracks sales by platform
- Visualizes sales trends over time
- Shows global game sales distribution
- Assesses the impact of critics' and users' scores

### User Portrait in Different Regions (***class `TopFive`***)
- Displays top 5 genres by region
- Displays top 5 platforms by region

## Installation

To install the package, run the following command:

```console
pip install game-sales
```

## Get started using game_sales

In order to start working with a dataset, it must be brought into a standard working form (rename columns, add data columns necessary for analysis, etc.). For this purpose there is DataPreprocessing class, which gives an output dataset ready for further analysis and processing:

```python
import game_sales as gs

data = gs.DataPreprocessing('file_path')

```

For example, we want to see the top 5 game genres in the regions:


```python

gs.TopFive(data).plot_top_genres_by_region()

```

<img src="https://github.com/Bagrinn96/game-sales/blob/main/img/plot_top_genres_by_region.png?raw=true">

Or for example, we need to analyze sales by ESRB rating and draw a conclusion:

```python

gs.DataDiscovery(data).sales_by_esrb()

```

<img src="https://github.com/Bagrinn96/game-sales/blob/main/img/sales_by_esrb.png?raw=true">

***Conclusions***
While the organisation that assigns the age rating is based in America, in Japan most games are not assigned an age rating at all, so it does not affect sales. In Europe and North America, the best-selling games are in the ‘mature 17+’ category, followed by ‘everyone’ and ‘teen 13+’. 

## License

`game-sales` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
