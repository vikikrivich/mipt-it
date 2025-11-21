# 1
import numpy as np
s = lambda x: 1/(1+np.power(np.e, -x)) # sigmoid
x1 = 1.0
x2 = 0.5
w11 = 0.9
w12 = 0.2
w21 = 0.3
w22 = 0.8

# 1
x = np.array([x1, x2])
w = np.array([[w11, w12],
              [w21, w22]])  

res1 = s(w.T @ x)
print(res1)
print("\n")

# 2
w = np.array([[w11, w21],[w12, w22]])
i = np.array([x1, x2])
res2 = s(w @ i)
print(res2)
print("\n")

# 3
w1 = np.array([[0.9, 0.3, 0.4],
               [0.2, 0.8, 0.2],
               [0.1, 0.5, 0.6]])
w2 = np.array([[0.3, 0.7, 0.5],
               [0.6, 0.5, 0.2],
               [0.8, 0.1, 0.9]])
i = np.array([0.9, 0.1, 0.8])

hidden = s(w1 @ i)
res3 = s(w2 @ hidden)
print(res3)
print("\n")

# 4
w11 = 2.0
w12 = 1.0
w21 = 3.0
w22 = 4.0
e1 = 0.8
e2 = 0.5

w = np.array([[w11, w21],
              [w12, w22]])
e = np.array([e1, e2])

res4_1 = e1 * w11 / (w11 + w21) + e2 * w12 / (w12 + w22)
res4_2 = e1 * w21 / (w11 + w21) + e2 * w22 / (w12 + w22)

hidden_errors = np.array([res4_1, res4_2])
print(hidden_errors)
print("\n")

# 5
w11 = 3.0
w12 = 1.0
w21 = 2.0
w22 = 7.0
e1 = 0.42
e2 = 0.88

rows = np.array([[w11, w21],
                 [w12, w22]])

res5_1 = e1 * w11 / (w11 + w21) + e2 * w12 / (w12 + w22)
res5_2 = e1 * w21 / (w11 + w21) + e2 * w22 / (w12 + w22)

print(res5_1, res5_2)
print("\n")

# 6
w = np.array([[w11, w21],[w12, w22]])
e = np.array([e1, e2])

res6 = w.T @ e
print(res6)
print("\n")


# 7
o1 = 0.4
o2 = 0.5
w11 = 2.0
w12 = 1.0
w21 = 3.0
w22 = 4.0
e1 = 0.8
e2 = 0.5
a = 0.1

np.array([[w11, w21],[w12, w22]])
e = np.array([e1, e2])
o = np.array([o1, o2])

net1 = w11 * o1 + w21 * o2
y1 = s(net1)
derivative1 = y1 * (1 - y1)
delta_w11 = a * e1 * derivative1 * o1
w11_new = w11 + delta_w11

print(y1)
print(derivative1)
print(delta_w11)
print(w11_new)

w = np.array([[w11, w21],[w12, w22]])
e = np.array([e1, e2])
o = np.array([o1, o2])
a = 0.1
res7 = w @ o
print(res7)
print("\n")


# 8
w = np.array([[w11, w21],[w12, w22]])
o = np.array([o1, o2])
e = np.array([e1, e2])
a = 0.1

net = w @ o
y = s(net)
delta = (y - e) * y * (1 - y)
term_e = delta * e
term_eo = term_e * o
delta_w = term_eo * a
w_new = w + np.tile(delta_w, (2, 1))

print(net)
print(y)
print(delta)
print(term_e)
print(term_eo)
print(delta_w)
print(w_new)
print("\n")

# 9
import numpy as np
s = lambda x: 1/(1+np.power(np.e, -x)) # sigmoid
w = np.array([[2.0, 3.0],[1.0, 4.0]])  # weights
a = 0.1                                # learning rate

X = np.array([[0.9, 0.1], [0.2, 0.8]]) # input  data
Y = np.array([[1.0, 0.0], [0.0, 1.0]]) # output data

#   X      y
#[.9 .1] [1 0]
#[.2 .8] [0 1]

epochs = 500
for epoch in range(epochs):
  for i in range(len(Y)):
    x, y = X[i], Y[i]
    o = s(x @ w)    # outputs
    e = y - o       # output errors
    d = e * o * (1 - o) # delta
    g = np.outer(x, d) # gradient - исправленная строка
    w += a * g      # updating weights
    
print(w)
print("\n")

# 10
w = np.array([[2.0, 3.0],[1.0, 4.0]])  # initial weights
a = 0.1                                # learning rate

X = np.array([[0.9, 0.1], [0.2, 0.8]]) # input data
Y = np.array([[1.0, 0.0], [0.0, 1.0]]) # output data

# Training
epochs = 5
for epoch in range(epochs):
    for i in range(len(Y)):
        x, y = X[i], Y[i]
        o = s(x @ w)    # outputs
        e = y - o       # output errors
        d = e * o * (1 - o) # delta
        g = X.T @ d # gradient
        w += a * g      # updating weights

def query(x):
    return s(x @ w)  # forward pass through the network

def predict(x):
    return np.argmax(query(x))  # return class with highest probability

def score(X, y):
    correct = 0
    for i in range(len(y)):
        if predict(X[i]) == y[i]:
            correct += 1
    return correct / len(y)  # return accuracy

X_test = np.array([[1.0, 0.0], [0.7, 0.2], [0.5, 0.5], [0.2, 0.7], [0.0, 1.0]])
y_test = np.array([0, 0, 1, 1, 1])

print(w)
print("Accuracy:", score(X_test, y_test))
print("\n")