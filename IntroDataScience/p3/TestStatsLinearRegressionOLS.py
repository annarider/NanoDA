import numpy as np

import statsmodels.api as sm

y = [1,3,4,5,2,3,4]
x = range(1,8)
print x
x = sm.add_constant(x)

print x

model = sm.OLS(y,x)
print model

results = model.fit()
print results

results.params
print results.params

results.tvalues
print results.tvalues


print results.t_test([1,0])

print results.f_test(np.identity(2))

half = len(x)/2
model2 = sm.OLS(y[:half], x[:half])
results2 = model2.fit()
predictions2 = results2.predict(x[half:])

print 'predict'
print results.predict()