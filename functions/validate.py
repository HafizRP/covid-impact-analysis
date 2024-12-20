import pandas as pd

def validate(data = pd.DataFrame):
    
    # REMOVE DATA STRINGENCY IS NULL WHEN CASES AND DEATHS WAS EXIST
    hasCases = data['total_cases'].notnull() & data['total_deaths'].notnull() # APAKAH SUDAH ADA KASUS
    isSecure = data['stringency_index'].isnull()
    noCaseWithStringency = (data['stringency_index'] > 0) & (data['stringency_index'] < 20)
    data = data[~isSecure & hasCases | noCaseWithStringency]
    
    # HAPUS DATA YANG TIDAK MEMILIKI GDP
    emptyGdp = data['gdp_per_capita'].isnull()
    data = data[~emptyGdp]
    
    # Drop all unnamed columns if they are irrelevant
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
    return data