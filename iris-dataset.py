import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Task 1: Load and Explore Dataset
# -----------------------------
try:
    # Load Iris dataset from seaborn
    df = sns.load_dataset('iris')
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: Dataset not found. Please check the file path.")

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check structure and missing values
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Clean dataset (drop rows with missing values if any)
df = df.dropna()
print("\nShape after dropping missing values:", df.shape)

# -----------------------------
# Task 2: Basic Data Analysis
# -----------------------------
print("\nBasic Statistics:")
print(df.describe())

# Group by species and compute mean
species_group = df.groupby('species').mean(numeric_only=True)
print("\nMean values per species:")
print(species_group)

# Observations
print("\nObservations:")
print("- Setosa generally has the smallest petal and sepal sizes.")
print("- Virginica tends to have the largest measurements among all species.")

# -----------------------------
# Task 3: Data Visualization
# -----------------------------
plt.figure(figsize=(12, 8))

# 1. Line Chart - Trend of sepal_length (Just for visualization purposes, sorted by index)
df_sorted = df.sort_index()
plt.subplot(2, 2, 1)
plt.plot(df_sorted.index, df_sorted['sepal_length'], label='Sepal Length', color='blue')
plt.title('Line Chart of Sepal Length')
plt.xlabel('Index')
plt.ylabel('Sepal Length')
plt.legend()

# 2. Bar Chart - Average petal length per species
plt.subplot(2, 2, 2)
species_group['petal_length'].plot(kind='bar', color='green')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length')

# 3. Histogram - Distribution of Sepal Length
plt.subplot(2, 2, 3)
plt.hist(df['sepal_length'], bins=15, color='purple', edgecolor='black')
plt.title('Sepal Length Distribution')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')

# 4. Scatter Plot - Sepal Length vs Petal Length
plt.subplot(2, 2, 4)
plt.scatter(df['sepal_length'], df['petal_length'], c='red', alpha=0.7)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')

plt.tight_layout()
plt.show()
