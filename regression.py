from numpy import genfromtxt
from sklearn import linear_model

columns = ["size","sex","age","outdoorness","fur","paws_door","muffins","belly_trap","corners","boxes","contort","drools","sprints","veggie","sheets","men","toes","knocks","keyboard","stares","blep","faucet","food_freak","hind_legs"]

data = genfromtxt('data-clean.csv', delimiter=',', skip_header=1)

for i in range(6, 24):
    model = linear_model.LinearRegression()
    xs = [row[0:5] for row in data if None not in row[0:5]]
    ys = [row[i] for row in data if row[i] != None]
    model.fit(xs, ys)
    print("The coefficients for " + columns[i])
    print(model.coef_)
