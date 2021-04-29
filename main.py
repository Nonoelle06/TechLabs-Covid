import numpy as np
import pandas as pd


df_vaccination = pd.read_csv("vaccination/vaccination in the EU.csv")
df_cases = pd.read_csv("cases_deaths/daily number of new reported.csv")

vac_count = len(df_vaccination["Region"].unique())
cases_count = len(df_cases["countriesAndTerritories"].unique())

print(vac_count)
print(cases_count)