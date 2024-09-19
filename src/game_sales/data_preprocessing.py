# libraries importing
import pandas as pd  
import math 

class DataPreprocessing:
    """ 
    DataPreprocessing class is responsible for loading and preprocessing the game sales dataset. 
    It includes functions to clean, transform, and augment the dataset.
    """
    
    def __init__(self, file_path):
        """
        Initializes the DataPreprocessing class by loading the dataset and applying preprocessing functions.

        """
        # loading the dataset 
        self.data = pd.read_csv(file_path)

        # apply all data preprocessing functions to clean and prepare the data
        self.__to_lowcase()  
        self.__data_to_Int64() 
        self.__apply_esrb_conversion() 
        self.__add_global_sales()  

    def __to_lowcase(self):
        """
        Converts all column names in the dataset to lowercase.
        This ensures consistency in column naming conventions.
        """
        self.data.columns = self.data.columns.str.lower()

    def __data_to_Int64(self):
        """
        Converts the 'year_of_release' column to integer type (Int64) to handle missing values and 
        ensure compatibility with Pandas operations.
        """
        self.data['year_of_release'] = pd.array(self.data['year_of_release'], dtype=pd.Int64Dtype())

    def __esrb_to_user_friendly(self, rating):
        """
        Converts ESRB rating codes to more user-friendly text descriptions.
        """
        if rating == 'E':
            return 'everyone'
        if rating == 'M':
            return 'mature 17+'
        if rating == 'T':
            return 'teen 13+'
        if rating == 'E10+':
            return 'everyone 10+'
        if rating == 'K-A':
            return 'everyone'
        if rating == 'AO':
            return 'adults only 18+'
        if rating == 'EC':
            return 'everyone'
        if rating == 'RP':
            return 'rating pending'
        # handle missing or NaN ratings by assigning 'rating pending'
        if isinstance(rating, float) and math.isnan(rating):
            return 'rating pending'
        # return the original rating if none of the conditions are met
        return rating

    def __apply_esrb_conversion(self):
        """
        Applies the ESRB rating conversion to the 'rating' column and adds a new column 'rating_new' 
        to the dataset.
        """
        self.data['rating_new'] = self.data['rating'].apply(self.__esrb_to_user_friendly)

    def __add_global_sales(self):
        """
        Adds a new column 'global_sales' by summing up the sales from various regions.
        """
        self.data['global_sales'] = self.data[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)

    def isna_view(self):
        """
        Returns a styled Pandas DataFrame showing the percentage of missing values (NaN) in each column.
        """
        
        return (
            (self.data.isna().mean() * 100)  # calculate percentage of NaNs for each column
            .sort_values(ascending=False)  # sort columns by the percentage 
            .to_frame()  # convert the result to a DataFrame
            .rename(columns={0: 'percent_space'})  # rename the column 
            .style.background_gradient('coolwarm')  # apply gradient background coloring
            .format("{:.2f}")  # format percentages to two decimal places
        )

    def get_data(self):
        """
        Returns the processed dataset as a DataFrame
        """
        return self.data
