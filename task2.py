import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Titanic-Dataset.csv")

# 1. Summary statistics
print(df.describe())                      # Numeric columns: mean, std, min, 25%, 50%, 75%, max
print(df.median(numeric_only=True))       # Medians

# 2. Histograms for numeric columns
numeric_columns = ['Age', 'Fare', 'SibSp', 'Parch']
df[numeric_columns].hist(bins=20, figsize=(12, 8))
plt.tight_layout()
plt.show()

# 2. Boxplots of Age and Fare grouped by Survival
plt.figure(figsize=(12, 6))
sns.boxplot(x='Survived', y='Age', data=df)
plt.title('Age by Survival')
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='Survived', y='Fare', data=df)
plt.title('Fare by Survival')
plt.show()

# 3. Correlation Matrix
corr = df.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title('Correlation Matrix')
plt.show()

# 4. Pairplot for feature relationships
sns.pairplot(df, vars=numeric_columns, hue="Survived")
plt.show()
