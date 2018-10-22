from tqdm import tqdm 
from matplotlib import pyplot as plot
from matplotlib import patches as patch
import numpy as nm
import scipy as sp

#load dataset
data = sp.genfromtxt("dataset.dat",delimiter="\t");
#shuffle data ( important for this dataset)
sp.random.shuffle(data);
#convert to ndarray
data = nm.array(data);
#get the dimensions
dim = data.shape;
#print(dim);

def euclid_dist(test,train):
    sd = nm.zeros(shape = (1,len(train)));
    for i in range (0,len(test)):
        sd = sd + ((test[i]-train[:,i])**2);
    return sd;
    
def nn(trainX, trainY, testX):
	predict = [];
	for test in tqdm(range(0, len(testX))):
		distances = euclid_dist(testX[test], trainX);
		near = distances.argmin();
		predict.append(trainY[near]);
	return predict

def nn_right(actual, predicted):
	right = 0
	for i in range(0, len(actual)):
		if actual[i] == predicted[i]:
			right += 1;
	return right / len(actual);
	
#85% train data; 15% test data

div = 0.85;
data_train = data[0: int(data.shape[0]*div)];
data_test = data[int(div*data.shape[0]): data.shape[0]];

# Y is skin or non-skin index ; X is rgb
trainY = data_train[:, (len(data[0]) - 1)]; # all rows ; 4th column
trainX = data_train[:, range(0, 3)]; # all rows ; first 3 columns
testY = data_test[:, (len(data[0]) - 1)];
testX = data_test[:, range(0, 3)];

predict = nn(trainX,trainY,testX);
#print(len(predict));
accuracy = nn_right(testY,predict);

print("Accuracy achieved is = " + str(accuracy) + "%");
