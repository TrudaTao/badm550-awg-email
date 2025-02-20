#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:11:57 2025

@author: truda
"""
import pandas as pd


file_path = '/Users/truda/Downloads/2023_merged_without_nodate_files.xlsx' 

df = pd.read_excel(file_path, engine='openpyxl')

print(df.head())


import seaborn as sns
import matplotlib.pyplot as plt

df_selected = df[["% of Sent", "Total Clicks"]]
df_selected = df_selected.apply(pd.to_numeric, errors='coerce')

#
plt.figure(figsize=(5,4))
sns.heatmap(df_selected.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap between % of Sent and Total Click (2023)")

plt.show()


df['Date'] = pd.to_datetime(df['Date'])

# Pearson Correlation Coefficient
overall_correlation = df[['Total Clicks', '% of Sent']].corr().iloc[0, 1]
print(f"Total Clicks 和 % of Sent Pearson Correlation Coefficient: {overall_correlation:.2f}")


df_sorted = df.sort_values('Date')

# time series plot
plt.figure(figsize=(12, 5))
plt.plot(df_sorted['Date'], df_sorted['Total Clicks'], label='Total Clicks', marker='o', linestyle='-')
plt.plot(df_sorted['Date'], df_sorted['% of Sent'] * 1000, label='% of Sent (scaled)', marker='s', linestyle='-')

plt.xlabel('Date')
plt.ylabel('Values (Clicks / Scaled % of Sent)')
plt.title(f'Time Series of Total Clicks and % of Sent (Correlation: {overall_correlation:.2f})')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()

file_path = '/Users/truda/Downloads/2024-Links.xlsx' 
df = pd.read_excel(file_path, engine='openpyxl')

print(df.head())


import seaborn as sns
import matplotlib.pyplot as plt

df_selected = df[["% of Sent", "Total Clicks"]]
df_selected = df_selected.apply(pd.to_numeric, errors='coerce')


plt.figure(figsize=(5,4))
sns.heatmap(df_selected.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap between % of Sent and Total Click (2024)")

plt.show()


df['Date'] = pd.to_datetime(df['Date'])

# Pearson Correlation Coefficient
overall_correlation = df[['Total Clicks', '% of Sent']].corr().iloc[0, 1]
print(f"Total Clicks 和 % of Sent Pearson Correlation Coefficient: {overall_correlation:.2f}")


df_sorted = df.sort_values('Date')

# time series plot
plt.figure(figsize=(12, 5))
plt.plot(df_sorted['Date'], df_sorted['Total Clicks'], label='Total Clicks', marker='o', linestyle='-')
plt.plot(df_sorted['Date'], df_sorted['% of Sent'] * 1000, label='% of Sent (scaled)', marker='s', linestyle='-')

plt.xlabel('Date')
plt.ylabel('Values (Clicks / Scaled % of Sent)')
plt.title(f'Time Series of Total Clicks and % of Sent (Correlation: {overall_correlation:.2f})')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()
