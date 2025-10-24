from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris(as_frame=True)
X, y = iris['data'], iris['target']
print(X.head())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.8, random_state=42)


neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)

print(neigh.score(X_test, y_test))

for n in range(1, 10):
    neigh = KNeighborsClassifier(n_neighbors=n)
    neigh.fit(X_train, y_train)
    print(f"n_neighbors: {n}, score: {neigh.score(X_test, y_test)}")

metric_list = ['euclidean', 'manhattan', 'chebyshev', 'minkowski']
for metric in metric_list:
    neigh = KNeighborsClassifier(n_neighbors=3, metric=metric)
    neigh.fit(X_train, y_train)
    print(f"metric: {metric}, score: {neigh.score(X_test, y_test)}")