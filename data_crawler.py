import yfinance as yf
import pandas as pd
import os


folder_name = "data"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

start_date = '2020-01-01' 
end_date = '2023-12-31'

banking_stocks = ['BBCA.JK', 'BBNI.JK', 'BBRI.JK', 'BMRI.JK']

for stock in banking_stocks:
    data = yf.download(stock, start=start_date, end=end_date)
    
    title = stock.replace('JK', '').replace('.', '')
    df = pd.DataFrame(data)
    df.to_csv(f'{folder_name}/{title}_2023.csv')


