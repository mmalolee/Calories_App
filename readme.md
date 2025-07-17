# Application for Predicting Calories Burned During Running

## Problem Description

The goal of this project is to create and train a machine learning model to estimate the number of calories burned during running based on a user's physiological data. The final model is implemented in a web application built using **Streamlit**, allowing users to estimate burned calories based on:

- predicted running duration (in minutes),
- heart rate (beats per minute),
- body temperature (°C),
- and gender.

## Technologies Used

- `pathlib`, `joblib` – file path operations, model saving,
- `pandas`, `numpy` – data analysis and manipulation,
- `matplotlib`, `seaborn` – visualizations,
- `scikit-learn` – linear regression model, data splitting, metrics,
- `streamlit` – web application.

## Dataset

The data comes from the [Kaggle](https://www.kaggle.com/datasets/fmendes/fmendesdat263xdemos/data?select=exercise.csv) platform and includes the following:

- participant data (gender, age, height, weight, training duration, heart rate, body temperature),
- number of calories burned.

## Project Structure

- calories_app_project
    - models
        - lm_females.pkl
        - lm_males.pkl
    - processed
        - females.csv
        - males.csv
    - raw
        - calories.csv
        - exercises.csv
    - app.py
    - cals.ipynb
    - readme.md
    - requirements.txt

## Running the Application (local environment)

- Open `app.py` and project's folder in VSCode.
- Open the terminal with *CTRL + Shift + `*
- Create a Conda environment using Python version 3.11.11.
- Activate the Conda environment: `conda activate env_name`.
- Install required packages from the requirements.txt file:
    - `cd path_to_project_folder`
    - `pip install -r requirements.txt`
- In the terminal, run the command: `streamlit run app.py`.
- Save code using *Ctrl + S*

## Running the Application (Streamlit Community Cloud)

- The app has been deployed using Streamlit Community Cloud: [Streamlit Calories App](https://caloriesapp.streamlit.app/)

## Analysis Steps

### 1. Loading and Merging Data

- Loaded data from two files: `exercise.csv` and `calories.csv`.
- Merged them using the `User_ID` column.
- Removed unnecessary columns and checked data types and missing values.

### 2. Data Preparation

- Converted `Duration` and `Heart_Rate` columns to integer type.
- Reviewed unique values in the `Gender` column.
- A heatmap identified the most important features
  - workout duration (`Duration`),
  - heart rate (`Heart_Rate`),
  - body temperature (`Body_Temp`).
- Scatter plots showed differences between genders.

### 3. Removing outliers and splitting data by Gender

- Box plots revealed outliers in the body temperature column.
- IQR was calculated and used to filter out records with outliers.
- Selected features and target (predicted) variable.
- Split data into two tables by gender and saved them as separate `.csv` files.

### 4. Model Building and Training

- Data was split into independent variables (`Duration`, `Heart_Rate`, `Body_Temp`) and the dependent variable (`Calories`) for each gender.
- Data was split into training and test sets (70/30 split).
- Trained two linear regression models (one for females, one for males).

### 5. Models Evaluation

- Analyzed regression coefficients.

| Feature     | Females Linear Coefficient | Males Linear Coefficient |
|-------------|----------------------------|---------------------------|
| Duration    | 6.446386                   | 6.948862                  |
| Heart_Rate  | 1.679007                   | 2.333261                  |
| Body_Temp   | -14.995103                 | -20.087459                |

- Analyzed MAE and R².

| Metric     | Females   | Males     |
|------------|-----------|-----------|
| MAE        | 6.702942  | 14.464262 |
| R²         | 0.977285  | 0.917716  |

- Reviewed residual scatter plots and histograms.

### 6. Model Saving and Deployment

- Models were saved in `.pkl` format using `joblib`.
- Loaded into a Streamlit app allowing the user to predict calorie burn from input values.
- A simple user interface was created to enter data.
- Input validation was added to prevent errors or negative predictions.

### For more details click [here](cals.ipynb).

## Conclusions

- Workout duration had the greatest impact on calories burned.
- The female model achieved better accuracy (lower MAE and higher R²) due to less data variance (based on the dataset used).
- Results may be different from real life due to the nature of the phenomenon (e.g., lack of information about participants fitness level or muscle mass).
- The residuals form a U-shape, indicating non-linearity in the data. The model underestimates results at low and high input values.
- The residual histogram deviates from normality, suggesting greater error variance.
- The negative coefficient for `Body_Temp` is due to multicollinearity—this variable is highly correlated with other independent features. Since they carry similar information, the regression model assigns an illogical negative influence to one of them (calories burned decreasing as body temperature rises).

## Possible Improvements

- Use a more advanced regression model that handles non-linear relationships better.
- Apply cross-validation.
- Use more precise and comprehensive data.