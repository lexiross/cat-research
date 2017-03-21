from sklearn.metrics import mean_squared_error, r2_score
import numpy
from sklearn import linear_model

columns = [
    "size",
    "sex",
    "age",
    "outdoorness",
    "fur length",
    "pawing at the door",
    "making muffins",
    "setting belly trap",
    "rubbing self on corners",
    "loving boxes",
    "contortionism",
    "drooling",
    "random sprinting",
    "loving oddly specific vegetarian foods",
    "hiding under the sheets",
    "preferring men",
    "attacking toes",
    "knocking things over",
    "loving keyboards",
    "staring intensely at the wall",
    "blep",
    "drinking from the faucet",
    "freaking out about half-empty food bowl",
    "standing on hind legs",
]

data = numpy.genfromtxt('data-clean.csv', delimiter=',', skip_header=1)

results = []
for i in range(5, 24):
    for j in range(0, 5):
        model = linear_model.LinearRegression(fit_intercept=True, n_jobs=1, normalize=True)
        data = [row for row in data if not numpy.isnan([row[i], row[j]]).any()]
        xs = [[row[j]] for row in data]
        ys = [row[i] for row in data]
        model.fit(xs, ys)
        prediction = model.predict(xs)
        results.append([columns[i], columns[j], model.coef_[0], r2_score(ys, prediction)])

best = sorted(results, key=lambda item: item[3], reverse=True)
for row in best[0:10]:
    print(row[1], "is", "positively" if row[2] > 0 else "negatively", "correlated (", row[2], ") with", row[0])

# print(best[0:10])
#
# # Make predictions using the testing set
# diabetes_y_pred = regr.predict(diabetes_X_test)
#
# # The coefficients
# print('Coefficients: \n', regr.coef_)
# # The mean squared error
# print("Mean squared error: %.2f"
#       % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# # Explained variance score: 1 is perfect prediction
# print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))
