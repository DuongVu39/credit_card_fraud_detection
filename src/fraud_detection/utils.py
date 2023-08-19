import pandas as pd


def print_shape_dataset(df: pd.DataFrame):
    print(
        f"Number of non frauds transaction is {df['Class'].value_counts()[0]},"
        f" {round(df['Class'].value_counts()[0] / len(df) * 100, 2)} % of the dataset")
    print(
        f"Number of frauds transaction is {df['Class'].value_counts()[1]},"
        f" {round(df['Class'].value_counts()[0] / len(df) * 100, 2)} % of the dataset")


