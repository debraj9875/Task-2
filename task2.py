import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")

# 1. Summary statistics
print(df.describe())
print(df.median(numeric_only=True))

# 2. Histograms
df.hist(column=["Age", "Fare", "SibSp", "Parch"], bins=20, figsize=(12,8))
plt.tight_layout()
plt.show()

# Boxplots grouped by Survived
plt.figure(figsize=(12,6))
sns.boxplot(x='Survived', y='Age', data=df)
plt.show()
sns.boxplot(x='Survived', y='Fare', data=df)
plt.show()

# 3. Correlation matrix
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

# 3. Pairplot (for key numerical columns)
sns.pairplot(df, vars=["Age", "Fare", "SibSp", "Parch"], hue="Survived")
plt.show()
