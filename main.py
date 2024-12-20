from functions import parameter, validate, visualisation
import pandas as pd

data = pd.read_csv('raw_data.csv')

# VALIDATE DATE
data = validate.validate(data)

# Variance Data
parameter.varianceGdp(data)

stats = data.describe()

print(stats)


# info = data.info()

# print(info)


# top5Covid = parameter.mostAffectedCountryByGDPPercentage(data)
# top5Covid = parameter.mostAffectedCountry(data)
# covidByCountry = data[data['iso_code'] == 'SMR']
# caseByMonth = parameter.caseByMonth(data)

# stats = parameter.mostCasesByCountry(data)

# visualisation.visualizeCases(data)
# visualisation.visualizeDeaths(data)
# visualisation.visualizePercentageCase(data)
# visualisation.visualizeEconomy(data)

# Set the display options to show all rows and columns
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Prevent line wrapping
pd.set_option('display.max_colwidth', None)  # Prevent truncating column content

# print(stats)
# print(caseByMonth)
# print(covidByCountry)
# print(covidByCountry)