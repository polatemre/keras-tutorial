# 1-Load Data.

from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load pima indians dataset
# see https://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]
# 2-Define Model.

# create model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

# 3-Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# 4-Fit the model
model.fit(X, Y, nb_epoch=150, batch_size=10)
# 5-Evaluate Model.
scores = model.evaluate(X, Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# calculate predictions
predictions = model.predict(X)
# round predictions
rounded = [round(x) for x in predictions]
print(rounded)
