import pandas as pd
import matplotlib.pyplot as plt

import functions as func

portfolio_size = 100000

#generate raw data frame and post to csv
bond_df = pd.DataFrame(func.random_bond_tenors(portfolio_size), columns = ['bond_tenor'])
bond_df['bond_yield'] = bond_df['bond_tenor'].apply(func.random_yield)
bond_df['par_value'] = 100
bond_df['bond_price'] = bond_df.apply(lambda x: func.bond_price(x['par_value'], x['bond_yield'], x['bond_tenor']), axis=1)
bond_df['bond_modified_duration'] = bond_df.apply(lambda x: func.bond_modified_duration(x['bond_tenor'], x['bond_yield']), axis=1)
bond_df['bond_convexity'] = bond_df.apply(lambda x: func.bond_convexity(x['bond_tenor'], x['bond_yield']), axis=1)
bond_df.to_csv('outputs/raw_bond_data.csv')

#generate portfolio aggregation by bond tenor
tenor_df = bond_df.groupby('bond_tenor').apply(func.tenor_aggregations)
tenor_df['tenor_weight'] = tenor_df['tenor_count'] / len(bond_df)
tenor_df = tenor_df[['tenor_weight', 'market_value', 'average_yield', 'tenor_duration', 'tenor_convexity']].reset_index()
tenor_df.to_csv('outputs/portfolio_by_tenor.csv')

#generate average yield curve graph for bond portfolio
plt.plot(tenor_df['bond_tenor'], tenor_df['average_yield'])
plt.title('Average Yield Curve of Bond Portfolio')
plt.xlabel('Bond Tenor (Years)')
plt.ylabel('Average Yield (%)')
plt.savefig('outputs/portfolio_yield_curve.png')
plt.close()

#generate portfolio value scenario analysis
plt.figure(figsize=(10, 6))
for index, row in tenor_df.iterrows():
    yield_changes = [i/10 for i in range(0, 31, 10)]
    price_changes = [func.portfolio_value_change(row['tenor_duration'], row['tenor_convexity'], i) for i in yield_changes]
    plt.plot(yield_changes, price_changes, label = f"Bond Tenor {int(row['bond_tenor'])} years")

plt.title('Portfolio Value Change Across Different Yield Changes')
plt.xlabel('Yield Change (%)')
plt.ylabel('Change in Average Portfolio Value (%)')
plt.legend()
plt.savefig('outputs/portfolio_value_change.png')
plt.close()