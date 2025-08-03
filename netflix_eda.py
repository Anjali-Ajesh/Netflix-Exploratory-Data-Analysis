# netflix_eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_netflix_eda():
    """
    Loads the Netflix dataset and performs an exploratory data analysis,
    generating several visualizations.
    """
    # --- 1. Load and Inspect the Dataset ---
    try:
        df = pd.read_csv('netflix_titles.csv')
    except FileNotFoundError:
        print("Error: 'netflix_titles.csv' not found.")
        print("Please download the dataset from https://www.kaggle.com/datasets/shivamb/netflix-shows")
        print("And place it in the project directory.")
        return

    print("--- Dataset Head ---")
    print(df.head())
    print("\n--- Dataset Info ---")
    df.info()

    # --- 2. Data Cleaning ---
    # Handle missing values. For this analysis, we'll focus on columns
    # that don't have many missing values. For 'country', we can fill with 'Unknown'.
    df['country'] = df['country'].fillna('Unknown')
    df.dropna(subset=['rating', 'duration'], inplace=True) # Drop rows with missing rating or duration

    # --- 3. Analysis & Visualization ---

    # Plot 1: Distribution of Movies vs. TV Shows
    plt.figure(figsize=(8, 8))
    sns.set_theme(style="whitegrid")
    ax = sns.countplot(x='type', data=df, palette='pastel')
    ax.set_title('Distribution of Content Types on Netflix', fontsize=16)
    ax.set_xlabel('Content Type', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    # Add annotations
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=11, color='gray', xytext=(0, 5),
                    textcoords='offset points')
    plt.savefig('content_type_distribution.png')
    print("\nGenerated 'content_type_distribution.png'")
    plt.close()


    # Plot 2: Top 10 Content Producing Countries
    # We need to handle entries with multiple countries
    country_data = df.assign(country=df['country'].str.split(', ')).explode('country')
    top_10_countries = country_data['country'].value_counts().drop('Unknown').head(10)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_10_countries.values, y=top_10_countries.index, palette='viridis')
    plt.title('Top 10 Content Producing Countries on Netflix', fontsize=16)
    plt.xlabel('Number of Titles', fontsize=12)
    plt.ylabel('Country', fontsize=12)
    plt.tight_layout()
    plt.savefig('top_10_countries.png')
    print("Generated 'top_10_countries.png'")
    plt.close()


    # Plot 3: Distribution of Content Ratings
    plt.figure(figsize=(14, 7))
    rating_order = df['rating'].value_counts().index
    sns.countplot(x='rating', data=df, order=rating_order, palette='coolwarm')
    plt.title('Distribution of Content by Rating', fontsize=16)
    plt.xlabel('Rating', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('content_rating_distribution.png')
    print("Generated 'content_rating_distribution.png'")
    plt.close()

    print("\n--- EDA Complete ---")


if __name__ == '__main__':
    perform_netflix_eda()
