#elt_pipeline.py

#1. import the necessary libraries
import pandas as pd
from sqlalchemy import create_engine

#2. Define the file path to the raw CSV
file_path = "C:/Users/kiera/Desktop/Python/Data_engineer_project/train.csv"

#3. Set up the connection to the SQLite database
#This creates a new file 'titanic.db' in the folder. It doesnt exist, to be created.
database_path = "sqlite:///C:/Users/kiera/Desktop/Python/Data_engineer_project/titanic.db"
engine = create_engine(database_path)

#4. EXTRACT: Read CSV file into a pandas dataframe
df = pd.read_csv(file_path)

#5. TRANSFORM: Perform data cleaning on the Dataframe
#Inspect data
print("Data shape before cleaning:", df.shape)
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Handle missing values
# For the 'Age' column, fill missing values with the median age
df['Age'].fillna(df['Age'].median(), inplace=True)

# For the 'Cabin' column, which has many missing values, we might just note its presence.
# A common approach is to create a new column 'Has_Cabin'
df['Has_Cabin'] = df['Cabin'].notnull().astype(int)

# For the 'Embarked' column, which has only 2 missing values, fill with the most common port ('S')
df['Embarked'].fillna('S', inplace=True)

# Drop the original 'Cabin' column as it's mostly missing and we've extracted the info we need
df.drop(columns=['Cabin'], inplace=True)

# Standardize text: Make 'Sex' column lowercase for consistency
df['Sex'] = df['Sex'].str.lower()

# Fix data types: Ensure 'Fare' is a float (it usually is, but it's good practice)
df['Fare'] = df['Fare'].astype(float)

# Check the results of our cleaning
print("\nData shape after cleaning:", df.shape)
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# 6. LOAD: Write the cleaned DataFrame to the SQL database
# 'to_sql' creates a new table called 'titanic_clean'
# `if_exists='replace'` means if the table already exists, overwrite it. Use `'append'` to add data instead.
df.to_sql('titanic_clean', con=engine, index=False, if_exists='replace')
print("\nData successfully loaded to the 'titanic_clean' table in the database.")

# 7. BONUS: Confirm the data was loaded correctly
# Execute a SQL query to read the first 5 rows from the new table
query = "SELECT * FROM titanic_clean LIMIT 5;"
result_df = pd.read_sql(query, con=engine)
print("\nSample data from the database:")
print(result_df)