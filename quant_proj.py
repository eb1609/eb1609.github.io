import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore
fx = pd.read_csv('Exchange_EURALL_CSV.csv', parse_dates=['Date'])
fx.rename(columns={'Price':'Close'}, inplace=True)
fx['Close'] = fx['Close'].astype(str).str.replace(',', '')
fx['Close'] = fx['Close'].str.extract(r'(\d+\.?\d*)')[0].astype(float)
fx['Date'] = pd.to_datetime(fx['Date'], format='%b %d, %Y')
fx = fx.sort_values('Date').reset_index(drop=True)
fx['Return'] = fx['Close'].pct_change(fill_method=None)
fx['Volatility'] = fx['Return'].rolling(window=3).std()
fx['FX_Risk_Factor'] = zscore(fx['Volatility'], nan_policy='omit')
tourism2 = pd.DataFrame({'Date': pd.to_datetime([2021, 2022, 2023], format='%Y'),
    'Close': [5688649, 7543817, 10155640]})
oil = pd.read_csv('Oil_price.csv', header=None, skiprows=4)  
oil.columns = ['Date', 'Close']
oil['Date'] = pd.to_datetime(oil['Date'])
oil = oil.sort_values('Date').reset_index(drop=True)
oil['Return'] = oil['Close'].pct_change()
oil['Volatility'] = oil['Return'].rolling(window=6).std()
oil['Energy_Risk_Factor'] = zscore(oil['Volatility'], nan_policy='omit')
inflation = pd.read_csv('EURO CPI.csv')
inflation.rename(columns={'observation_date':'Date', 'CPHPTT01EZM659N':'Close'}, inplace=True)
inflation['Date'] = pd.to_datetime(inflation['Date'])
inflation = inflation.sort_values('Date').reset_index(drop=True)
inflation['Return'] = inflation['Close'].pct_change(fill_method=None)
inflation['Volatility'] = inflation['Return'].rolling(window=6).std()
inflation['Inflation_Risk_Factor'] = zscore(inflation['Volatility'], nan_policy='omit')
tourism = pd.read_csv('2010-2020 Tourism.csv', skiprows=4)
tourism = tourism[tourism['Country Name'] == 'Albania']
tourism = tourism.loc[:, ~tourism.columns.str.contains('^Unnamed')]
tourism = tourism.drop(columns=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], errors='ignore')
tourism = tourism.T.reset_index()
tourism.columns = ['Date', 'Close']
tourism['Date'] = pd.to_datetime(tourism['Date'], format='%Y', errors='coerce')
tourism = tourism.dropna(subset=['Date'])
tourism = tourism[(tourism['Date'].dt.year >= 2010) & (tourism['Date'].dt.year <= 2020)]
tourism = tourism.sort_values('Date').reset_index(drop=True)
tourism_all = pd.concat([tourism, tourism2], ignore_index=True)
tourism_all = tourism_all.drop_duplicates(subset='Date')
tourism_all = tourism_all.sort_values('Date').reset_index(drop=True)
tourism_all['Return'] = tourism_all['Close'].pct_change(fill_method=None)
tourism_all['Volatility'] = tourism_all['Return'].rolling(window=3).std()
tourism_all['Tourism_Risk_Factor'] = zscore(tourism_all['Volatility'], nan_policy='omit')

fx_annual = (fx.set_index('Date').resample('Y')['Return'].std().reset_index())
fx_annual['FX_Risk_Factor'] = zscore(fx_annual['Return'], nan_policy='omit')
oil_annual = (oil.set_index('Date').resample('Y')['Return'].std().reset_index())
oil_annual['Energy_Risk_Factor'] = zscore(oil_annual['Return'], nan_policy='omit')
inflation_annual = (inflation.set_index('Date').resample('Y')['Return'].std().reset_index())
inflation_annual['Inflation_Risk_Factor'] = zscore(inflation_annual['Return'], nan_policy='omit')
tourism_annual = tourism_all.copy()
fx_annual['Year'] = fx_annual['Date'].dt.year
inflation_annual['Year'] = inflation_annual['Date'].dt.year
oil_annual['Year'] = oil_annual['Date'].dt.year
tourism_annual['Year'] = tourism_annual['Date'].dt.year
risk_index = (
    fx_annual[['Year', 'FX_Risk_Factor']]
    .merge(inflation_annual[['Year', 'Inflation_Risk_Factor']], on='Year', how='inner')
    .merge(oil_annual[['Year', 'Energy_Risk_Factor']], on='Year', how='inner')
    .merge(tourism_annual[['Year', 'Tourism_Risk_Factor']], on='Year', how='inner')
)
risk_index['Date'] = pd.to_datetime(risk_index['Year'], format='%Y')
risk_index['Risk_Index'] = risk_index[['FX_Risk_Factor', 'Inflation_Risk_Factor',
            'Energy_Risk_Factor', 'Tourism_Risk_Factor']].mean(axis=1)
plt.figure(figsize=(12,6))
plt.plot(risk_index['Date'], risk_index['Risk_Index'], marker='o')
plt.axvline(pd.Timestamp('2020-01-01'), linestyle='--', alpha=0.6, label='COVID')
plt.title('Albania Economic Shock & Risk Index (2010–2023)')
plt.xlabel('Year')
plt.ylabel('Risk Index')
plt.legend()
plt.grid(True)
plt.yticks(np.arange(-1, 2, 0.1))
plt.show()