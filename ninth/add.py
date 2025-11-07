from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


iris = datasets.load_iris(as_frame=True)
X, y = iris['data'], iris['target']

# key - n_neighbors, val - list scores
results = {}


for n_neighbors in range(1, 11):
    scores = []

    for random_state in range(100):
        X_train, X_test, y_train, y_test = train_test_split( 
            X, y, train_size=0.2, random_state=random_state
        )

        neigh = KNeighborsClassifier(n_neighbors=n_neighbors)
        neigh.fit(X_train, y_train)

        score = neigh.score(X_test, y_test)
        scores.append(score)
    
    results[n_neighbors] = scores


df_results = pd.DataFrame(results)


plt.figure(figsize=(10, 6))
sns.boxplot(data=df_results)
plt.xlabel('n_neighbors')
plt.ylabel('score')
plt.title('Distribution (100 splits for each)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


print("\nstatistics by n_neighbors:")
print(df_results.describe())

