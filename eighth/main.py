import pandas as pd 
import numpy as np
from sklearn import datasets

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df.head()

print(f"Исходные данные: \n{df.head()}")
print(f"Размер датасета: {df.shape}")

# 1
df = df.sample(frac=1).reset_index(drop=True)
print(f"\nПосле перемешивания: \n{df.head()}")

# 2 
train_size = int(0.8 * len(df))
train_df = df.iloc[:train_size]
test_df = df.iloc[train_size:]

print(f"train_df: \n{train_df.head()}")
print(f"test_df: \n{test_df.head()}")

# 3 поиск по признаку
X_train = train_df.drop(columns=['target'])
y_train = train_df['target']
X_test = test_df.drop(columns=['target'])
y_test = test_df['target']

# 4 вектор разности
distances = []
for _, test_row in X_test.iterrows():
    row_distances = []
    for _, train_row in X_train.iterrows():
        diff = test_row - train_row
        row_distances.append(diff)
    distances.append(row_distances)

# 5 квадрат разности (длина расстояния)
squared_distances = []
for row_distances in distances:
    squared_row = []
    for diff in row_distances:
        squared = diff.pow(2).sum()
        squared_row.append(squared)
    squared_distances.append(squared_row)

# 6 ближайшие соседи (5 штук)
nearest_neighbors = []
for i, row_distances in enumerate(squared_distances):
    distances_series = pd.Series(row_distances)
    sorted_distances = distances_series.sort_values()
    nearest_5 = sorted_distances.head(5)
    nearest_neighbors.append(nearest_5)

print(f"nearest_neighbors: \n{nearest_neighbors}")

# 7 значения этих точек в y_train
nearest_values = []
for i, nearest_neighbor in enumerate(nearest_neighbors):
    neighbor_values = []
    for neighbor_idx in nearest_neighbor.index:
        neighbor_values.append(y_train.iloc[neighbor_idx])
    nearest_values.append(neighbor_values)

print(f"nearest_values: \n{nearest_values}")

# 8 мода
modes = []
for neighbor_values in nearest_values:
    mode = pd.Series(neighbor_values).mode()[0]
    modes.append(mode)
print(f"modes: \n{modes}")

# 9 скопировать y_test в y_pred
y_pred = y_test.copy()

# 10 мода сохранить в y_pred
y_pred = pd.Series(modes)
print(f"y_pred: \n{y_pred}")

# 11 сравнить y_pred == y_test и посчитать среднее
middle = (y_pred.reset_index(drop=True) == y_test.reset_index(drop=True)).mean()
print(f"middle: {middle}")

# 12 класс 
class KNeighborsClassifier:
    def __init__(self, n_neighbors=5):
        self.n_neighbors = n_neighbors

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = []
        for _, test_row in X.iterrows():
            # расстояния до всех точек
            distances = []
            for _, train_row in self.X_train.iterrows():
                diff = test_row - train_row
                distance = diff.pow(2).sum()
                distances.append(distance)
            
            # соседи
            distances_series = pd.Series(distances)
            sorted_distances = distances_series.sort_values()
            nearest_k = sorted_distances.head(self.n_neighbors)
            
            neighbor_values = []
            for neighbor_idx in nearest_k.index:
                neighbor_values.append(self.y_train.iloc[neighbor_idx])
            
            # мода
            mode = pd.Series(neighbor_values).mode()[0]
            predictions.append(mode)
        
        return pd.Series(predictions)

# тест
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_class = knn.predict(X_test)

print(f"предсказания: \n{y_pred_class}")
print(f"реальное: \n{y_test.reset_index(drop=True)}")

# мода
pred_mode = y_pred_class.mode()[0]
real_mode = y_test.mode()[0]
print(f"мода предсказаний: {pred_mode}")
print(f"мода реальных: {real_mode}")
print(f"моды совпадают: {pred_mode == real_mode}")

