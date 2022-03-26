import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as pl
import ipywidgets as widgets

def h(theta, x):
    return theta[0] + theta[1] * x

def cost_fun(h, theta, x, y):
    m = len(y)
    return 1.0 / (2 * m) * sum((h(theta, x[1]) - y[i])**2 for i in range(m)) 

def gradient_descent(h, cost_fun, theta, x, y, alpha, eps):
    current_cost = cost_fun(h, theta, x, y)
    m = len(y)
    while True:
        new_theta = [
            theta[0] - alpha/float(m) * sum(h(theta, x[i]) - y[i] 
                for i in range(m)),
            theta[1] - alpha/float(m) * sum((h(theta, x[i]) - y[i]) * x[i] 
                for i in range(m))
        ]
        theta = new_theta
        try:
            prev_cost = current_cost
            current_cost = cost_fun(h, theta, x, y)
        except OverflowError:
            break
        if abs(prev_cost - current_cost) <= eps:
            break
    return theta

def load_data():
    reader = csv.reader(open('fires_thefts.csv'), delimiter=',')
    x = list()
    y = list()

    for xi, yi in reader:
        x.append(float(xi))
        y.append(float(yi))

    return x, y

x, y = load_data()

best_theta = gradient_descent(h, cost_fun, [0.0, 0.0], x, y, alpha=0.0001, eps=0.00001)

results = [h(best_theta, 50), h(best_theta, 100), h(best_theta, 200)]

print(
    '\nWłamania na tys. mieszkańców dla dzielnicy, w której występuje \nśrednio 50 pożarów na tys. gospodarstw: '
    + str(results[0])
)

print(
    '\nWłamania na tys. mieszkańców dla dzielnicy, w której występuje \nśrednio 100 pożarów na tys. gospodarstw: '
    + str(results[1])
)

print(
    '\nWłamania na tys. mieszkańców dla dzielnicy, w której występuje \nśrednio 200 pożarów na tys. gospodarstw: '
    + str(results[2]) + '\n'
)
