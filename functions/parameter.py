import pandas as pd

def addCautiousIndex():
    print("ADD CAUTIOUS")
    

def varianceGdp(df = pd.DataFrame):
    alpha = 0.5  # weight for deaths
    beta = 0.2   # weight for cases
    
    # Avoid division by zero or missing population values
    df['population'] = df['population'].replace(0, 1).fillna(1)
    df['total_cases'] = df['total_cases'].replace(0, 1).fillna(0)
    df['total_deaths'] = df['total_deaths'].replace(0, 1).fillna(0)
    df['stringency_index'] = df['stringency_index'].replace(0, 1).fillna(0)
    

    # Calculate adjusted GDP
    df['gdp_adjusted'] = df['gdp_per_capita'] * (
        1 - alpha * (df['total_deaths'] / df['population']) 
        - beta * (df['total_cases'] / df['population'])
    )

    # Calculate GDP variance
    df['gdp_variance'] = df['gdp_per_capita'] - df['gdp_adjusted']
    
    return df

def findHighestStringencyIndex(df = pd.DataFrame):
    baseData = df.groupby('iso_code')
    stringency_index = baseData['stringency_index'].max()    
    result = stringency_index.sort_values(ascending=False)
    return result

import pandas as pd

def findHighestStringencyIndexIdx(df: pd.DataFrame):
    # Step 1: Group by 'iso_code' and get the index of the row with the maximum 'stringency_index' for each group
    baseData = df.groupby('iso_code')['stringency_index'].idxmax()
    
    # Step 2: Use .loc to get the entire rows corresponding to the maximum 'stringency_index' for each group
    result = df.loc[baseData]
    
    # Step 3: Sort the result by 'stringency_index' in descending order
    result = result.sort_values('stringency_index', ascending=False)
    
    return result

def findHighestAvgStringencyIndex(df: pd.DataFrame):
    baseData = df.groupby(['iso_code', 'location'])['stringency_index'].mean()
    return baseData.sort_values(ascending=False)

def mostAffectedCountry(df = pd.DataFrame):
    baseData = df.groupby('iso_code')
    mostGdp = baseData['gdp_adjusted'].max()
    leastGdp = baseData['gdp_adjusted'].min()
    
    # result =  baseData.agg(
    #     selisihGdp= mostGdp - leastGdp,
    #     leastGdp=leastGdp,
    #     mostGdp=mostGdp,
    #     totalCase=('total_cases', 'max')
    # ).reset_index()
    
    return mostGdp - leastGdp


def mostAffectedCountryByGDPPercentage(df: pd.DataFrame):
    # Group by 'iso_code' (representing countries)
    grouped = df.groupby(['iso_code', 'location'])
    
    # Calculate COVID-19 impact per capita for each group (as percentage)
    df['case_per_capita_percentage'] = (df['total_cases'] / df['population']) * 100
    df['death_per_capita_percentage'] = (df['total_deaths'] / df['population']) * 100
    
    # Calculate the overall "COVID impact percentage" for each country
    df['covid_impact_percentage'] = df['case_per_capita_percentage'] + df['death_per_capita_percentage']
    
    # Calculate GDP per capita percentage (relative to the total GDP in the dataset)
    total_gdp = df['gdp_per_capita'].sum()  # Sum of all GDP values in the dataset
    df['gdp_per_capita_percentage'] = (df['gdp_adjusted'] / total_gdp) * 100
    
    # Aggregate the data for each country
    result = grouped.agg(
        total_cases_percentage=('case_per_capita_percentage', 'sum'),
        total_deaths_percentage=('death_per_capita_percentage', 'sum'),
        covid_impact_percentage=('covid_impact_percentage', 'sum'),
        gdp_per_capita_percentage=('gdp_per_capita_percentage', 'mean'),
        gdp_adjusted_diff=('gdp_adjusted', lambda x: x.max() - x.min()),  # Calculate max - min,
        total_cases=('total_cases', 'max'),
        mostGdp=('gdp_adjusted', 'max'),
        leastGdp=('gdp_adjusted', 'min')
    ).reset_index()
    
    # Sort by the 'covid_impact_percentage' in descending order to find the most affected countries
    result_sorted = result.sort_values(by='gdp_adjusted_diff', ascending=False)
    
    # Return the relevant columns including the gdp_adjusted difference
    return result_sorted[['iso_code', 'location', 'gdp_per_capita_percentage', 'covid_impact_percentage', 'gdp_adjusted_diff', 'total_cases', 'mostGdp', 'leastGdp']]


def mostCasesByCountry(df: pd.DataFrame):
    baseData = df.groupby('iso_code')
    total_cases = baseData['total_cases'].max()
    result = total_cases.sort_values(ascending=False)
    return result

def caseByMonth(df = pd.DataFrame):
    
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    grouped = df.groupby(['year', 'month'])['value'].sum().reset_index()
    
    return grouped

def caseByCountry(df):
    if df.empty:
        raise ValueError("The DataFrame is empty. Please provide a valid DataFrame.")
    
    if 'iso_code' not in df.columns or 'total_cases' not in df.columns:
        raise ValueError("The DataFrame must contain 'iso_code' and 'total_cases' columns.")
    
    # Group data by 'iso_code'
    baseData = df.groupby('iso_code')
    
    # Sum total cases per country
    total_cases = baseData['total_cases'].sum()
    
    # Sort values in descending order
    result = total_cases.sort_values(ascending=False)
    
    return result

def totalCountry(df: pd.DataFrame):
    totalCountry = df.groupby('iso_code')
    return len(totalCountry)