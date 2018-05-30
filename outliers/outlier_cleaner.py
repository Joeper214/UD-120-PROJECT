#!/usr/bin/python
from operator import itemgetter

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    errors = map(calculate_error, predictions, net_worths)
    cleaned_data = zip(ages, net_worths, errors)
    cleaned_data.sort(key=itemgetter(2), reverse=True)
    to_remove = int(round(len(predictions)*0.1))
    del cleaned_data[0:to_remove+1]

    return cleaned_data

def calculate_error(x, y):
    z = x-y
    return z**2

