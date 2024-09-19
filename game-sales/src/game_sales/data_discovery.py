# Libraries importing
import pandas as pd  
import matplotlib.pyplot as plt 

class DataDiscovery:
    """ 
    Class for exploring and visualizing. It provides methods 
    to discover patterns in sales by year, platform, genre, and other factors.
    """

    def __init__(self, preprocessor):
        """
        Initializes the DataDiscovery class with the dataset processed by the preprocessor.
        """             

        # retrieve the processed dataset from the preprocessor
        self.data = preprocessor.get_data()

        # filter data for the relevant period (after 2013)
        self.latest_data = self.data[self.data['year_of_release'] > 2013] 

    def release_by_year(self):
        """
        Plots the number of games released each year.
        """
        
        self.data.pivot_table(index='year_of_release', 
                              values='name', 
                              aggfunc='count') .plot(kind='bar',  #count the number of games ('name') for each eyar and plot a bar chart        
              xlabel='Year', # rename x-axis
              ylabel='Number of games released') # rename y-axis  

    def global_sales_by_platform(self):
        """
        Plots a boxplot of global game sales for each platform (filtered for releases after 2013).
        Displays sales distribution with a y-axis limit of 2 million copies.
        """
        
        self.latest_data.boxplot(column='global_sales', by='platform', figsize=(15, 5))  
        plt.ylim(0, 2)  # limit the y-axis to 2 million copies

    def global_sales_by_genre(self):
        """
        Plots a boxplot of global game sales for each genre (filtered for releases after 2013).
        Displays sales distribution with a y-axis limit of 2 million copies.
        """

        
        self.latest_data.boxplot(column='global_sales', by='genre', figsize=(15, 5))  
        plt.ylim(0, 2)  # limit the y-axis to 2 million copies

    def sales_dynamics_by_platform(self):
        """
        Plots the dynamics of global game sales over time, broken down by platform.
        Displays a line chart with the years on the x-axis and the sum of global sales on the y-axis.
        """

        self.data.pivot_table(index='year_of_release',  # year is on the x-axis
                              columns='platform',  # platforms will be used to break down sales
                              values='global_sales',  
                              aggfunc='sum').plot(figsize=(20,10))  # sum the global sales for each platform by year and Plot the resulting data as a line chart
 
    def plot_sales_vs_scores(self):
        """
        Plots the impact of critic and user scores on game sales for three platforms (Xbox One, PS4, PC).
        Creates scatter plots showing the relationship between sales and scores for each platform.
        Also prints the correlation between scores and sales for each platform.
        """

        platforms = ['XOne', 'PS4', 'PC']  # platforms of interest
        colors = ['red', 'blue', 'green']  # colors for each platform's plot

    
        fig, axes = plt.subplots(3, 2, figsize=(15, 10))  # create a figure with 3x2 subplots

        # loop through each platform and its color
        for i, (platform, color) in enumerate(zip(platforms, colors)):
            # filter the data for the current platform and limit global sales 
            data = self.latest_data[(self.latest_data['platform'] == platform) & (self.latest_data['global_sales'] < 5)]

            # plot the impact of critic scores on global sales
            axes[i, 0].scatter(data['global_sales'], data['critic_score'], c=color, edgecolors='black')  
            axes[i, 0].set_title(f'Impact of critic scores on game sales {platform}') 
            axes[i, 0].set_xlabel('Number of copies sold, millions')  
            axes[i, 0].set_ylabel('Critic scores, 0 to 100') 

            # Plot the impact of user scores on global sales
            axes[i, 1].scatter(data['global_sales'], data['user_score'], c=color, edgecolors='black')  
            axes[i, 1].set_title(f'Impact of user scores on game sales {platform}')  
            axes[i, 1].set_xlabel('Number of copies sold, millions')  
            axes[i, 1].set_ylabel('User scores, 0 to 10') 

        plt.tight_layout()  #adjust layout to prevent overlap between subplots
        plt.show()  # display the figure

        # calculate and print the correlation between scores and sales for each platform
        for platform in platforms: 
            
            data_p = self.latest_data[self.latest_data['platform'] == platform]

            print(f'Platform {platform}')  
            # calculate and print correlation between critic scores and global sales
            print(f"Correlation of critics scores and sales: {data_p['critic_score'].corr(data_p['global_sales'])}")
            # calculate and print correlation between user scores and global sales
            print(f"Correlation of users scores and sales: {data_p['user_score'].corr(data_p['global_sales'])}")
            print() 

    def sales_by_esrb(self):
        """
        Plots sales by ESRB rating for different regions (Japan, Europe, North America).
        Displays a horizontal bar chart showing the sum of sales by rating for each region.
        """
        
        self.latest_data.pivot_table(index='rating_new',  
                                     values=['jp_sales', 'eu_sales', 'na_sales'],  # sum sales for different regions
                                     aggfunc='sum').plot(kind='barh')  # aggregate sales data by summing for each region and plot a horizontal bar chart
          
        plt.legend(['Europe', 'Japan', 'North America'])  
        plt.xlabel('Number of games sold, millions')  
