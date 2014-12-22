import numpy as np

x = [1,2,3,4,5,6]
y = [10,11,12,13,14,16]

print np.square(np.array(x) - np.array(y))
print ""

print x
print y
print ""

print np.array(x)
print  np.array(y)

    # sum_of_data_minus_predictions = (np.square(data - predictions)).sum()
    # sum_of_predictions_minus_mean = (np.square(predictions - np.mean(data))).sum()
    # r_squared = 1 - sum_of_data_minus_predictions / sum_of_predictions_minus_mean
print ""

print np.square(np.array(x) - np.array(y)).sum()
print 81*5 + 100
print ""

print np.square(np.array(x) - np.mean(np.array(y))).sum()

print '###'

xa = np.array(x)
ya = np.array(y)

top = np.square(xa - ya).sum()
bottom = np.square(xa - np.mean(ya)).sum()
print top
print bottom
print 'r2=', (1-top/bottom)
print ""

print (9-7)**2, (7-9)**2, (18-36)**2, (36-18)**2





