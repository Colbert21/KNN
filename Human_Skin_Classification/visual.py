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

#fourth column which is the skin or non-skin index i.e 1 or 2
sns = data[:,(len(data[0])-1)];
#print("sns= " + str(sns));

#first three columns i.e the RGB values
rgb = data[:, range(0,3)];
#print("rgb= " + str(rgb));

scx = nm.arange(0,1000);

def visual(c, index, plot):
    colors = [];
    for sorn in sns[:1000]:
        if sorn == 1:
            colors.append("yellow");
        elif index == 0:
            colors.append("red");
        elif index == 1:
            colors.append("green");
        elif index == 2:
            colors.append("blue");
            
    #print(colors);        
    c.scatter(scx,rgb[:1000,index], c=colors, marker = "d");
    if index == 0:
        c.set_xlabel("red");
        non_skin = patch.Patch(color = "red", label = "Non-Skin");
    elif index == 1:
        c.set_xlabel("green");
        non_skin = patch.Patch(color = "green", label = "Non-Skin");
    elif index == 2:
        c.set_xlabel("blue");
        non_skin = patch.Patch(color = "blue", label = "Non-Skin");
        
    c.set_ylabel("Pixel");
    skin = patch.Patch(color = "yellow", label = "Skin");
    plot.legend(handles = [skin,non_skin], loc = "upper right");

figure = plot.figure();

red = figure.add_subplot(131);
visual(red,0,plot);

green = figure.add_subplot(132);
visual(green,1,plot); 

blue = figure.add_subplot(133);
visual(blue,2,plot);
     
plot.show();     
