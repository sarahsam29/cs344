import numpy as np
import pandas as pd
from keras.datasets import boston_housing


(training_x, training_y), (testing_x, testing_y) = boston_housing.load_data()

print('training_x shape:', training_x.shape)
print('training_y shape:', training_y.shape)
print('testing_x shape:', testing_x.shape)
print('testing_y shape:', testing_y.shape)

#I am diving the training set into a new training set and a validation set.
#The validation set recieves the first half of the training set and the new training set receives the other half.

validation_x = training_x[0:202]
training_x = training_x[203:]

validation_y = training_y[0:202]
training_y= training_y[203:]
print("\n")

print('validation_x shape:', validation_x.shape)
print('validation_y shape:', validation_y.shape)
#print('training_x shape:', training_x.shape)
#print('training_y shape:', training_y.shape)


boston_df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv")
boston_df['tax_percent'] = (boston_df['tax']/ 100)
boston_df['affordability'] = (boston_df['tax_percent'] * boston_df['lstat'])

print(boston_df.head())

# I want to describe how affordabile a city is based on the full value property tax and the percent of low income people living in a town.
# The idea is that if the full value property tax is fairly low, and there is a greater percent of low income people living in the town then
# the town is fairly affordable. Affordability is a percentage, where lower percents indicate a more expesive area and higher percents indicate
# cheaper areas. That being said, I wanted to convert 'tax' to a percent so that I can multiply it with 'lstat' and I am not sure if that is correct.