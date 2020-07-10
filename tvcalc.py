import math
from matplotlib import pyplot as plt
import pandas as pd

def time_value_calculator(country, start_year, end_year):

    # Loading and cleaning dfframe
    df = pd.read_csv('inflation.csv')
    df = df[df['Country Name'].values == country]
    df = df.drop(['Indicator Name', 'Indicator Code', 'Unnamed: 64', 'Country Name', 'Country Code'], axis=1)
    df = df.truncate(before=str(start_year), after=str(end_year), axis="columns")

    # Creating an array for present values every year (inlcuding NaN)
    pv = []
    pv.append(1)

    for i in range(1, len(df.columns) + 1):
        if df.isnull().iloc[0, i - 1]:
            pv.append(pv[i - 1] * 1.01)
        else:
            pv.append((1 + 0.01 * df.iloc[0, i - 1]) * pv[i - 1])

    # Extracting Answer
    diff = end_year - start_year
    if diff >= 0:
        return "1U in {start} is worth {value}U in {year}, where U represents {country}'s currency".format(country=country, year=end_year, value=round(pv[diff], 2), start=start_year)
    else:
        return "Not Enough Data"

# User input
country = input("Enter Region: ")
start_year = int(input("Enter Start Year: "))
end_year = int(input("Enter Current or End Year: "))

# Calling Function
print(time_value_calculator(country, start_year, end_year))
