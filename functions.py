import random as rnd
import numpy as np
import pandas as pd

#this function generates a random distribution of zero coupon bonds by bond tenor, tenor weight and portfolio size
def random_bond_tenors(bond_number: int):
    bond_tenors = [3,5,10,30]
    sample_probabilities = [0.20, 0.30, 0.30, 0.20]
    return np.random.choice(bond_tenors, size = bond_number, p = sample_probabilities)

#this function maps each bond tenor to a stochastic, normal yield curve. the yield curve steps up with tenor
def random_yield(tenor: int) -> float:
    match tenor:
        case 3:
            return rnd.uniform(2.0, 3.0)
        case 5:
            return rnd.uniform(4.0, 5.5)
        case 10:
            return rnd.uniform(6.0, 8.00)
        case 30:
            return rnd.uniform(10.00, 11.00)
        
#this function calculates the current bond price using yield, tenor and an assumed par value of 100
def bond_price(par_value, bond_yield, bond_tenor):
    discount_rate = bond_yield / 100
    discount_factor = (1 + discount_rate) ** bond_tenor
    return par_value / discount_factor

#this function calculated the modified duration for each zero coupon bond using tenor and yield
def bond_modified_duration(bond_tenor, bond_yield):
    discount_rate = bond_yield / 100
    return bond_tenor / (1 + discount_rate)

#this function calculated the convexity for each zero coupon bond using tenor and yield
def bond_convexity(bond_tenor, bond_yield):
    discount_rate = bond_yield / 100
    discount_factor = (1 + discount_rate) ** 2
    numerator = (bond_tenor ** 2) + bond_tenor
    return numerator / discount_factor

"""
This function is applied to the raw bond list to aggregate it by tenor. 
It's a piece wise function that creates multiple columns in the new dataframe.
It counts the total bonds by tenor, sums the market value, and averages yield.
It also sums duration and convexity. 
Since this is aggregating raw bonds at equal weight, these columns are directly summed.
"""
def tenor_aggregations(x):
    d = {}
    d['tenor_count'] = x['bond_tenor'].count()
    d['market_value'] = round(x['bond_price'].sum(),2)
    d['average_yield'] = round(x['bond_yield'].mean(),2)
    d['tenor_duration'] = round(x['bond_modified_duration'].sum(), 2)
    d['tenor_convexity'] = round(x['bond_convexity'].sum(), 2)
    return pd.Series(d, index=['tenor_count', 'market_value', 'average_yield', 'tenor_duration', 'tenor_convexity'])

#this function is applied when plotting the portfolio value change of each bond tenor against yield change
def portfolio_value_change(tenor_duration, tenor_convexity, yield_change):
    return (-1 * tenor_duration * yield_change) + (0.5 * tenor_convexity * (yield_change ** 2)) * 100
        