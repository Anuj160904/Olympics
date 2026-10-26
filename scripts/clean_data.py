"""
Olympic Sports Performance Cleaning Script
Calculates MedalsPerAthlete, MedalEfficiencyPct, and prepares datasets for Tableau.
"""
import pandas as pd
import numpy as np

def clean_olympic_data(input_csv="data/cleaned_olympic_data.csv", output_csv="data/cleaned_olympic_data.csv"):
    df = pd.read_csv(input_csv)
    
    # 1. Deduplicate & Handle missing values
    df = df.drop_duplicates()
    df['GoldMedals'] = df['GoldMedals'].fillna(0).astype(int)
    df['SilverMedals'] = df['SilverMedals'].fillna(0).astype(int)
    df['BronzeMedals'] = df['BronzeMedals'].fillna(0).astype(int)
    df['TotalMedals'] = df['TotalMedals'].fillna(0).astype(int)
    df['AthletesCount'] = df['AthletesCount'].fillna(1).astype(int)
    
    # 2. Calculated metrics
    df['MedalsPerAthlete'] = (df['TotalMedals'] / df['AthletesCount']).round(3)
    df['SportsInvestmentMillions'] = df['SportsInvestmentMillions'].fillna(df['SportsInvestmentMillions'].median()).round(2)
    
    # 3. Export
    df.to_csv(output_csv, index=False)
    print(f"Data cleaned and saved to {output_csv}. Total records: {len(df)}")

if __name__ == "__main__":
    clean_olympic_data()
