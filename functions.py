
# functions.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from scipy.stats.contingency import association

# --- Data Loading and Merging ---
def load_and_merge_data(demo_file, experiment_file, web_data_pt1, web_data_pt2):
    df_final_demo = pd.read_csv(demo_file)
    df_final_experiment_clients = pd.read_csv(experiment_file)
    df_final_web_data_pt_1 = pd.read_csv(web_data_pt1)
    df_final_web_data_pt_2 = pd.read_csv(web_data_pt2)

    df_concat_web_data = pd.concat([df_final_web_data_pt_1, df_final_web_data_pt_2], ignore_index=True)
    df_concat_web_data.sort_values(by='client_id', inplace=True)

    df_merged = pd.merge(df_final_demo, df_final_experiment_clients, on='client_id', how='inner')
    df_final = pd.merge(df_merged, df_concat_web_data, on='client_id', how='inner')

    return df_final

# --- Data Cleaning ---
def clean_data(df):
    df_filtered = df[df['Variation'].notna()].dropna()
    df_filtered['logons_6_mnth'] = df_filtered['logons_6_mnth'].astype(int)
    df_filtered['gendr'] = df_filtered['gendr'].replace({'X': 'U'})
    df_filtered = df[df['Variation'].notna()]
    df_filtered['date_time'] = pd.to_datetime(df_filtered['date_time'])
    return df_filtered

# --- Statistical Analysis (mean, variance, etc.) ---
def calculate_stat_metrics(df, column):
    mean_val = df[column].mean()
    median_val = df[column].median()
    mode_val = df[column].mode()[0]
    variance_val = df[column].var()
    std_dev_val = df[column].std()
    min_val = df[column].min()
    max_val = df[column].max()
    range_val = max_val - min_val
    quartiles_val = df[column].quantile([0.25, 0.5, 0.75])
    skewness_val = df[column].skew()
    kurtosis_val = df[column].kurtosis()

    return {
        "mean": mean_val,
        "median": median_val,
        "mode": mode_val,
        "variance": variance_val,
        "std_dev": std_dev_val,
        "min": min_val,
        "max": max_val,
        "range": range_val,
        "quartiles": quartiles_val,
        "skewness": skewness_val,
        "kurtosis": kurtosis_val
    }

# --- Completion Rate Calculation ---
def calculate_completion_rate(df, step_name):
    completion_count = df.groupby('Variation')['process_step'].apply(lambda x: (x == step_name).sum())
    total_count = df['Variation'].value_counts()
    completion_rate = completion_count / total_count
    return completion_rate

# --- Crosstab and Chi-square Test ---
def perform_chi2_test(df, col1, col2):
    crosstab_result = pd.crosstab(df[col1], df[col2])
    chi2, p, dof, expected = chi2_contingency(crosstab_result)
    cramer_v = association(crosstab_result, method='cramer')
    return chi2, p, dof, cramer_v

    # --- Time Spent Analysis ---

def calculate_time_spent(df):
 
    df['date_time'] = pd.to_datetime(df['date_time'])

    df = df.sort_values(by=['visitor_id', 'date_time'])

    df['time_spent'] = df.groupby('visitor_id')['date_time'].diff().dt.total_seconds().fillna(0)
    
    return df

def age_category(df):
    # Define bins and labels for 4 categories
    bins = [0, 30, 40, 50, df['clnt_age'].max()]  # Add another bin for 30-40 age group
    labels = ['Young (0-30)', 'Young Adults (31-40)', 'Middle-aged (41-50)', 'Senior (51+)']

    # Discretize 'clnt_age' into 4 categories
    df['clnt_age_category'] = pd.cut(df['clnt_age'], bins=bins, labels=labels, include_lowest=True)

    # Display value counts to check the distribution of clients across age categories
    df['clnt_age_category'].value_counts()
    return df

def bal_category(df):
 
    bins = [0, 100000, 200000, 300000, df['bal'].max()]     
    labels = ['Low', 'Medium', 'High', 'Strong']

    df['balance'] = pd.cut(df['bal'], bins=bins, labels=labels, include_lowest=True)

    df['balance'].value_counts()
   
    return df

def tenure_category(df):
    bins = [0, 48, 96, 200, df['clnt_tenure_mnth'].max()]     
    labels = ['New', 'Medium Time', 'Long Time', 'Very Long Time']

    df['tenure'] = pd.cut(df['clnt_tenure_mnth'], bins=bins, labels=labels, include_lowest=True)

    df['tenure'].value_counts()
   
    return df

def average_time_spent_by_step(df):
    avg_time_spent = df.groupby(['Variation', 'process_step'])['time_spent'].mean().unstack()
    return avg_time_spent

# --- Correlation Analysis ---
def time_correlation(df, group_by_column):
    df['previous_time_spent'] = df.groupby('visitor_id')['time_spent'].shift(1)
    correlation_df = df.groupby(group_by_column)[['time_spent', 'previous_time_spent']].corr().iloc[0::2, -1]
    correlation_df = correlation_df.reset_index().rename(columns={'level_1': 'Variable', 0: 'Correlation'})
    return correlation_df


    
    

