import pandas as pd  
import matplotlib.pyplot as plt  

class TopFive:
    """ 
    Class for generating visualizations of the top 5 genres and platforms.
    """

    def __init__(self, preprocessor):
        """ 
        Initializes the TopFive class with the dataset processed by the preprocessor. 
        """
        # retrieve the processed dataset from the preprocessor
        self.data = preprocessor.get_data()

        # filter data for the relevant period (after 2013)
        self.latest_data = self.data[self.data['year_of_release'] > 2013] 


    def plot_top_genres_by_region(self):
        """
        Plots the top 5 game genres by sales in different regions (Japan, North America, Europe).
        Creates three bar charts showing the top genres in each region.
        """

        # list of regions to analyze sales 
        regions = ['jp', 'na', 'eu']  
        region_titles = ['Japan', 'North America', 'Europe']

        # create a figure with 3 subplots 
        fig, axes = plt.subplots(1, 3, figsize=(18, 5)) 
        fig.suptitle('Top 5 Game Genres by Region') 
        
        # loop through each region 
        for i, region in enumerate(regions):  
            # create a pivot table to aggregate sales by genre for the current region
            top_genres = self.latest_data.pivot_table(index='genre',  # group by genre
                                               values=f'{region}_sales',  # sum sales for the given region
                                               aggfunc='sum')  # aggregate sales by summing them up
            
            top_genres = top_genres.sort_values(f'{region}_sales', ascending=False)[:5]  # sort and get top 5 genres
            
            # plot a bar chart for the top genres in the current region
            axes[i].bar(top_genres.index, top_genres[f'{region}_sales'])  
            axes[i].set_title(region_titles[i])  

        
        plt.tight_layout()  
        plt.show()  

    def plot_top_platforms_by_region(self):
        """
        Plots the top 5 gaming platforms by sales in different regions (Japan, North America, Europe).
        Creates three side-by-side bar charts showing the top platforms in each region.
        """

        # list of regions to analyze sales for
        regions = ['jp', 'na', 'eu']  
        
        region_titles = ['Japan', 'North America', 'Europe']

        # create a figure with 3 subplots
        fig, axes = plt.subplots(1, 3, figsize=(18, 5))  
        fig.suptitle('Top 5 Game Platforms by Region')  

        # coop through each region to plot the top 5 platforms by sales
        for i, region in enumerate(regions):  
            # create a pivot table to aggregate sales by platform for the current region
            top_platforms = self.latest_data.pivot_table(index='platform',  # group by platform
                                                  values=f'{region}_sales',  # sum sales for the given region
                                                  aggfunc='sum')  # aggregate sales by summing them up
            
            top_platforms = top_platforms.sort_values(f'{region}_sales', ascending=False)[:5]  # Sort and get top 5 platforms
            
            # plot a bar chart for the top platforms in the current region
            axes[i].bar(top_platforms.index, top_platforms[f'{region}_sales'])  # plot platform names on x-axis and sales on y-axis
            axes[i].set_title(region_titles[i])  

       
        plt.tight_layout()  
        plt.show()  
