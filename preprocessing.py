# preprocessing.py
from __future__ import print_function  # For Python 2/3 compatibility
import pandas as pd

# Define column names for the Adult dataset
COLUMNS = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income'
]

def preprocess_adult_data(input_file, output_file, sample_size=1500):
    # Step 1: Load data and replace '?' with NaN
    print("[1/4] Loading dataset...")
    df = pd.read_csv(
        input_file,
        header=None,
        names=COLUMNS,
        na_values='?',
        skipinitialspace=True
    )
    print("Original dataset: {} rows".format(len(df)))

    # Step 2: Remove rows with missing values ('?' entries)
    print("\n[2/4] Removing rows with missing values...")
    df_clean = df.dropna()
    print("Cleaned dataset: {} rows remaining".format(len(df_clean)))

    # Step 3: Sample rows from cleaned data
    print("\n[3/4] Sampling {} rows.".format(sample_size))
    sample_size = min(sample_size, len(df_clean))
    df_sampled = df_clean.sample(n=sample_size, random_state=42)

    # Step 4: Save processed data
    print("\n[4/4] Saving to {}...".format(output_file))
    df_sampled.to_csv(output_file, header=False, index=False)
    print("Done! Saved {} rows to {}".format(len(df_sampled), output_file))

if __name__ == "__main__":
    preprocess_adult_data(
        input_file='datasets/adult.data',
        output_file='datasets/processed_adult.data',
        sample_size=1500
    )
