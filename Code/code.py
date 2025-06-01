import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load data from a CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    return pd.read_csv(file_path)

def showing_data(df):
    data=df.head(10)
    return data

def info_data(df):
    """Display information about the DataFrame."""
    info = df.info()
    return info

def plot_data(df):
    """Plot data from the DataFrame."""
    x = df['total_deaths']
    z = df['new_deaths']
    y = df['total_cases']

    plt.figure(figsize=(10, 6))  # Set figure size first
    plt.plot(x, y, label='Total Deaths vs Total Cases')
    plt.plot(z, y, label='New Deaths vs Total Cases')
    
    plt.title("COVID Cases vs Deaths")
    plt.xlabel("Deaths")
    plt.ylabel("Total Cases")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_histogram(df, column, bins=20, color='skyblue'):
    
    #Checking if the column exists in the DataFrame
    if column not in df.columns:
        print(f"Column '{column}' not found in DataFrame.")
        return
    #The cloumn is present in the DataFrame
    plt.figure(figsize=(10, 6))
    plt.hist(df[column].dropna(), bins=bins, color=color, edgecolor='black')
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    file_path=r"C:\Users\soura\OneDrive\Desktop\Project\Data_set\owid-covid-latest.csv"
    df=load_data(file_path)
    print("Data loaded successfully.")
    print("Showing first 10 rows of the dataset:")
    print(showing_data(df))
    print("\nDataFrame Information:")
    print(info_data(df))
    print("\nPlotting data...")
    plot_data(df)
    print("Data plotted successfully.")
    print("\nPlotting histogram for 'total_cases' column...")
    plot_histogram(df, 'total_cases', bins=30, color='lightgreen')
    print("Histogram plotted successfully.")    
    
    
if __name__ == "__main__":
    main()