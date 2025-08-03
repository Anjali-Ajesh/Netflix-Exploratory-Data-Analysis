# Netflix-Exploratory-Data-Analysis
An Exploratory Data Analysis (EDA) project that dives into the Netflix Movies and TV Shows dataset. This script uses Python, Pandas, Matplotlib, and Seaborn to uncover trends and patterns within the Netflix content library.
## Features

-   **Data Cleaning:** Handles missing values in the dataset to prepare it for analysis.
-   **Content Distribution Analysis:** Visualizes the distribution of movies vs. TV shows available on Netflix.
-   **Geographical Analysis:** Identifies and plots the top 10 countries that produce the most content for Netflix.
-   **Rating Analysis:** Analyzes the distribution of content across different maturity ratings (e.g., TV-MA, PG-13).
-   **Insightful Visualizations:** Creates clear and informative bar charts and pie charts to present the findings.

## Technology Stack

-   **Python**
-   **Pandas:** For data loading, cleaning, and manipulation.
-   **Matplotlib & Seaborn:** For creating static data visualizations.
-   **Jupyter Notebook (Recommended):** Ideal for running this type of step-by-step analysis.

## Setup and Usage

A virtual environment is recommended for this project.

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Anjali-Ajesh/netflix-eda.git](https://github.com/Anjali-Ajesh/netflix-eda.git)
    cd netflix-eda
    ```

2.  **Install Dependencies:**
    ```bash
    # Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    # Install the required libraries
    pip install pandas matplotlib seaborn
    ```

3.  **Download the Dataset:**
    * This project uses the "Netflix Movies and TV Shows" dataset from Kaggle.
    * [Download Link](https://www.kaggle.com/datasets/shivamb/netflix-shows)
    * Download the `netflix_titles.csv` file and place it in the root directory of your project.

4.  **Run the Analysis:**
    Execute the Python script from your terminal. The script will print some basic info and then generate and save the visualization plots as image files (`.png`) in your project directory.
    ```bash
    python netflix_eda.py
    ```
    For a more interactive experience, it's recommended to run the code cells in a Jupyter Notebook.
