from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

# training data set (height as feature), (weight as label)
ht_ftr = [[6],[5],[4],[3],[2],[1]]              
wt_target= [[90],[70],[50],[30],[10],[5]]		# 

regression=linear_model.LinearRegression()
regression=regression.fit(ht_ftr,wt_target)

# The coefficients
print('Coefficients:', regression.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regression.predict(ht_ftr) - wt_target) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regression.score(ht_ftr, wt_target))

# Plot outputs
plt.scatter(ht_ftr, wt_target,  color='black')
plt.plot(ht_ftr, regression.predict(ht_ftr), color='blue',
         linewidth=3)

# hide x and y axis
# plt.xticks(())   
# plt.yticks(())

plt.show()

print(regression.predict(5.5))