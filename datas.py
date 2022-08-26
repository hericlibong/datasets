

import pandas as pd


url = 'https://raw.githubusercontent.com/CodeForAfrica/covid19-in-africa/master/datasets/africa_historic_data.csv'
covid = pd.read_csv(url)

covid.to_csv('covid_africa.csv')