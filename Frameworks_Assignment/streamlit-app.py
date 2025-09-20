import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# -----------------------------
# Part 1: Data Loading and Basic Exploration
# -----------------------------
try:
    df = pd.read_csv("metadata.csv")
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: metadata.csv not found. Please check the file path.")

print("Shape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())
print("\nSample rows:")
print(df.head())

# -----------------------------
# Part 2: Data Cleaning and Preparation
# -----------------------------
df = df.dropna(subset=['publish_time', 'title'])
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))
print("\nCleaned dataset shape:", df.shape)

# -----------------------------
# Part 3: Data Analysis and Visualization
# -----------------------------
# 1. Publications by year
year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
plt.bar(year_counts.index, year_counts.values)
plt.title("Number of Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()

# 2. Top journals
top_journals = df['journal'].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_journals.values, y=top_journals.index)
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.show()

# 3. Word cloud of titles
titles_text = " ".join(df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Frequent Words in Paper Titles")
plt.show()

# 4. Source distribution
plt.figure(figsize=(8, 5))
df['source_x'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Sources of Papers")
plt.xlabel("Source")
plt.ylabel("Count")
plt.show()

# -----------------------------
# Part 4: Streamlit App (basic structure)
# -----------------------------
# Save this section in a separate file named streamlit_app.py to run with Streamlit
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers from the metadata.csv file")

df = pd.read_csv("metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

year_range = st.slider("Select Year Range", 2019, 2023, (2020, 2021))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.subheader("Sample Data")
st.dataframe(filtered_df[['title', 'authors', 'journal', 'year']].head())

year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title("Publications by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)
"""