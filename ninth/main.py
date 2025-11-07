import numpy as np
from scipy.stats import norm
from sklearn import datasets
from random import shuffle

iris = datasets.load_iris()
X, y = iris.data, iris.target

lst = list(range(150))
shuffle(lst)
X_train = X[lst[:120]]
y_train = y[lst[:120]]
X_test = X[lst[120:]]
y_test = y[lst[120:]]


flower_class = 0
feature_idx = 0

def find_pdf(X, y):
    # data for 1 type of flower and 1 feature
    mask = (y == flower_class)
    feature_data = X[mask, feature_idx]

    mean = np.mean(feature_data)
    std = np.std(feature_data)

    print(f"class: {flower_class} ({iris.target_names[flower_class]})")
    print(f"feature: {feature_idx} ({iris.feature_names[feature_idx]})")
    print(f"mean: {mean:.4f}")
    print(f"std: {std:.4f}")
    print(f"num: {len(feature_data)}")

    # calculate pdf
    print("\npdf:")
    # creating 10 point between min and max and norm pdf for each point
    test_values = np.linspace(feature_data.min(), feature_data.max(), 10)
    pdf_values = []
    for val in test_values:
        pdf_value = norm.pdf(val, loc=mean, scale=std)
        print(f"  X = {val:.2f}, PDF = {pdf_value:.4f}")
        pdf_values.append(pdf_value)
    print(sum(pdf_values)/len(pdf_values))

find_pdf(X_train, y_train)
find_pdf(X_test, y_test)