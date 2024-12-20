import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualizeCases(df):
    # Group by country and calculate total cases
    caseByCountry = df.groupby(['iso_code'])
    totalCaseByCountry = caseByCountry['total_cases'].max()

    # Sort by total cases in descending order and take the top 10 countries
    sortedCaseByCountry = totalCaseByCountry.sort_values(ascending=False)
    top_10_country = sortedCaseByCountry.head(10)

    # Print top 10 countries for debugging
    print(top_10_country)

    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(top_10_country.index, top_10_country.values, marker='o', color='blue')

    # Adding labels and grid
    plt.title("Kasus COVID-19 Top 10 Negara", fontsize=16)
    plt.xlabel("Negara", fontsize=12)
    plt.ylabel("Total Kasus Terinfeksi (Dalam Juta)", fontsize=12)
    plt.grid()
    plt.xticks(rotation=45, fontsize=10)  # Rotate labels for better visibility

    # Tight layout for better spacing
    plt.tight_layout()

    # Show the plot
    plt.show()
    
def visualizeDeaths(df):
    # Group by country and calculate total cases
    caseByCountry = df.groupby(['iso_code'])
    totalCaseByCountry = caseByCountry['total_deaths'].max()

    # Sort by total cases in descending order and take the top 10 countries
    sortedCaseByCountry = totalCaseByCountry.sort_values(ascending=False)
    top_10_country = sortedCaseByCountry.head(10)

    # Print top 10 countries for debugging
    print(top_10_country)

    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(top_10_country.index, top_10_country.values, marker='o', color='blue')

    # Adding labels and grid
    plt.title("Kasus COVID-19 Top 10 Negara", fontsize=16)
    plt.xlabel("Negara", fontsize=12)
    plt.ylabel("Total Kasus Meninggal", fontsize=12)
    plt.grid()
    plt.xticks(rotation=45, fontsize=10)  # Rotate labels for better visibility

    # Tight layout for better spacing
    plt.tight_layout()

    # Show the plot
    plt.show()
    
def visualizeGdp():
    return True;

def visualizePercentageCase(df: pd.DataFrame):
    groupedByCountry =  df.groupby(['iso_code', 'location'])
    
    groupedAgg = groupedByCountry.agg(
        total_cases=('total_cases', 'max'),
        total_deaths=('total_deaths', 'max'),
        avg_stringency=('stringency_index', 'mean'),
        # country_name=('location', 'first')
    )
    
    groupedAgg['deaths_percentage'] = (groupedAgg['total_deaths'] / groupedAgg['total_cases']) * 100
    
    top_10 = groupedAgg.sort_values(by=['total_cases'], ascending=[False]).head(20)
    
    # print(top_10)
    
    # Create a heatmap
    plt.figure(figsize=(8, 5))
    sns.heatmap(top_10[['total_cases', 'total_deaths', 'deaths_percentage', 'avg_stringency']], 
            annot=True, fmt=".1f", cmap="coolwarm", linewidths=0.5)

    # Add title
    plt.title('Heatmap of Cases, Deaths, and Death Percentage')

    # Show the plot
    plt.tight_layout()
    plt.show()

def visualizeEconomy(df: pd.DataFrame):
    groupedByCountry = df.groupby(['iso_code', 'location'])
    groupedAgg = groupedByCountry.agg(
        min=('gdp_adjusted', 'min'),
        max=('gdp_adjusted', 'max'),
        total_cases=('total_cases', 'max'),
        total_deaths=('total_deaths', 'max'),
        base=('gdp_per_capita', 'min')
    )
    
    groupedAgg['gdp_difference'] = (groupedAgg['max'] - groupedAgg['min'])
    
    top_20 = groupedAgg.sort_values(by=['gdp_difference'], ascending=False).head(20)
    
    plt.figure(figsize=(8,5))
    sns.heatmap(top_20[['base', 'min', 'max', 'gdp_difference', 'total_cases', 'total_deaths']], annot=True, fmt=".1f", cmap='coolwarm', linewidths=0.5)
    plt.title("Heatmap GDP Difference")
    plt.tight_layout()
    plt.show()
    
    
