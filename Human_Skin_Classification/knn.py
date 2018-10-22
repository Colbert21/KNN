from tqdm import tqdm 
from collections import Counter
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

#85% train data; 15% test data

div = 0.85;
data_train = data[0: int(data.shape[0]*div)];
data_test = data[int(div*data.shape[0]): data.shape[0]];

# Y is skin or non-skin index ; X is rgb
trainY = data_train[:, (len(data[0]) - 1)]; # all rows ; 4th column
trainX = data_train[:, range(0, 3)]; # all rows ; first 3 columns
testY = data_test[:, (len(data[0]) - 1)];
testX = data_test[:, range(0, 3)];

print(len(trainX));
def euclid_dist(test,train,i):
    return nm.sum(nm.square(test-train[i:,]));
    
def kpredict(trainX,trainY,testX,k):
    dist = [];
    knearest = [];
    
    #print("kin");
    for i in tqdm(range(len(trainX))):
        d = euclid_dist(testX,trainX,i);
        dist.append([d,i]);
        #print("din"+str(i));
    
    #sort list of distances for choosing nearest neighbors
    dist = sorted(dist);
    
    # choose k neighbors and append skin or not skin index to knearest
    for i in range(k):
        index = dist[i][1];
        knearest.append(trainY[index]);
    
    # return most common answer i.e skin or non skin
    return Counter(knearest).most_common(1)[0][0]; 
    
def knn(trainX,trainY,testX,k):
    predict = [];
    #print("in");
    for i in range(len(testX)):
        #print("inin");
        predict.append(kpredict(trainX,trainY,testX[i,:],k));
    return predict;
    
def knn_right(actual, predicted):
	right = 0
	for i in range(0, len(actual)):
		if actual[i] == predicted[i]:
			right += 1;
	return right / len(actual);
	
predict = knn(trainX,trainY,testX,5);
accuracy = knn_right(testY,predict);

print("Accuracy achieved is = " + str(accuracy) + "%");


