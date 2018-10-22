from tqdm import tqdm 
from matplotlib import pyplot as plot
from matplotlib import patches as patch
import numpy as nm
import scipy as sp
import scipy.misc as spm

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
	
img = spm.imread('Test_Images/t_1.jpg');
ori_img = img;
#print(img.shape); # will return number of row, number of columns, number of channels or colors
w,h = img.shape[0:2];
#print(img.shape[0:2]);
img = img.reshape((img.shape[0]*img.shape[1]),img.shape[2]); # multiplying number of rows and columns
# swapping r and b channels as dataset contains BGR values and image contains RGB values
img[:, [0, 2]] = img[:, [2, 0]];

#load entire dataset 
trainY = data[:, (len(data[0]) - 1)];
trainX = data[:, range(0, len(data[0]))];

predict = nm.array(nn(trainX,trainY,img));

#if skin then white else black in output image
op_img = nm.zeros(shape = (w*h,3), dtype = nm.uint8);
for i in range(0, len(img)):
    if predict[i] == 1.0:
        op_img[i] = [255, 255, 255];
        
op_img = op_img.reshape(w,h,3);
plot.subplot(121);
plot.title("Original Image");
plot.imshow(ori_img);
plot.subplot(122);
plot.title("Human Skin marked white otherwise black");
plot.imshow(op_img);
plot.show();
