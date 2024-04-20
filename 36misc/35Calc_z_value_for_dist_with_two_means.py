from math import sqrt

meanA = 80
deviationA = 5
nA = 5

meanB = 83
deviationB = 4
nB = 6

z = (meanA - meanB) / (sqrt((deviationA**2 / nA) + (deviationB**2 / nB)))
print(z)