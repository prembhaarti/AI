#http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
#url have all terminologies

from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

# training data set (height as feature), (weight as label)
year_ftr = [[2005], [2006], [2007], [2008], [2009]]
# year_ftr = [[2005,4],[2006,6],[2007,8],[2008,10],[2009,12]]

revenue_target= [12, 18, 29, 37, 45]		#

regression = linear_model.LinearRegression()
regression = regression.fit(year_ftr, revenue_target)

# The coefficients
print('Coefficients:', regression.coef_)
print('Residues:', regression.residues_)
print('Intercept:', regression.intercept_)


# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regression.predict(year_ftr) - revenue_target) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regression.score(year_ftr, revenue_target))

# Plot outputs
plt.scatter(year_ftr, revenue_target,  color='black')
plt.plot(year_ftr, regression.predict(year_ftr), color='blue',
         linewidth=3)

# hide x and y axis
# plt.xticks(())   
# plt.yticks(())

# result_input=
plt.show()

predicted_result=regression.predict([2012])
print(predicted_result)

print(regression.score(year_ftr,revenue_target))