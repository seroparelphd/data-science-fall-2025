import numpy as np
import pandas as pd

class NaiveBaseline:
    def __init__(self):
        self.last_value = float('nan')

    def fit(self, ts):
        """Fit the model by storing the last value of the time series.
        Args:
            ts (numpy array or pandas Series): The time series data.
        """
        # Convert pandas Series to numpy array if input is a pandas Series
        if isinstance(ts, pd.Series):
            ts =   # Convert to numpy array

        self.last_value = 
        
    def forecast(self, h):
        """Forecast for the next h time periods using the last observed value.
        Args:
            h (int): Number of periods to forecast.
        Returns:
            numpy array: Forecasted values.
        """ 

class RandomWalkWithDrift:
    '''
    Remember that the Random Walk With Drift Model leads to a forecast which 
    simply extends the secant line connecting the first and last point of the time series.
    '''
    def __init__(self):
        self.initial_value = float('nan')
        self.last_value = float('nan')
        self.slope = float('nan')

    def fit(self, ts):
        

    def forecast(self, h):


class NaiveSeasonalWithDrift:
    """
    Forecasts future values by repeating the most recent seasonal
    pattern of differences (deltas).

    For example, if season_length = 4 and the last 5 values were:
    [3,4,5,6,5], then deltas would be [1,1,1,-1] and the last_value would be 5.

    The forecast into the future would be [6,7,8,7, 8, 9, 10, 9,...].
    """
    def __init__(self, season_length):
        self.season_length = season_length
        self.deltas = None
        self.anchor = None

    def fit(self, ts):

    def forecast(self, h):
        