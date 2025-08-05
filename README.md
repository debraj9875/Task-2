# Task-2
Understand data using statistics and visualizations
1. Summary Statistics
You can use df.describe() and df.median() to obtain basic statistics:

Mean, median, standard deviation, min, max for all numeric columns (Age, Fare, SibSp, Parch, etc.).

These statistics help you quickly spot ranges, averages, and extreme or unusual values.

Example output for Age and Fare (using sample data):

Feature	Count	Mean	Median	Std	Min	Max
Age	9	28.11	27.00	14.95	2	54
Fare	10	27.02	16.10	23.60	7.25	71.28
Insight: Age and Fare both have wide spreads; Fare is skewed with high outliers.

2. Histograms and Boxplots
Histograms for Age/Fare show the distribution and highlight skew or multiple peaks.

Boxplots (e.g., Age and Fare grouped by Survival) let you compare distributions and spot outliers or group differences.

Example insights:

Age distribution is right-skewed; most passengers are 20–40.

Fare has a long tail—most people paid a modest fare, with a few expensive tickets.

Boxplots highlight that survivors tend to have lower ages (children) and higher fares (wealthier).

3. Pairplot & Correlation Matrix
Correlation matrix shows which features are related. For Titanic:

Survived is moderately negatively correlated with Pclass (higher class = higher survival).

Fare and Pclass are strongly negatively correlated (higher class, higher fare).

SibSp and Parch somewhat correlate (family size factors).

Pairplots visualize all variable relationships, colored by Survived, exposing clusters and relationships (e.g., survivors are clustered among high fares and lower classes).

4. Patterns, Trends, and Anomalies
Class and Fare:

1st class and higher fares have better survival odds.

Family:

Most passengers traveled with no or one family member.

Outliers:

Some extremely high Fares.

Age missing for some, requiring handling.

Skewness:

Both Fare and Age are right-skewed.

5. Inferences from Visuals
Survival bias: Females, higher class, children, and those who paid more had higher survival rates.

Class and fare are strong predictors of survival.

Age and family structure (SibSp, Parch) add nuance, especially for children.

Majority of lower class and male passengers did not survive.
