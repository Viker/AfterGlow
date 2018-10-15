import os 
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from skimage import data

ROOT_PATH = "c:\Data"
train_data_directory = os.path.join(ROOT_PATH, "TrafficSigns/Training")
test_data_directory = os.path.join(ROOT_PATH, "TrafficSigns/Testing")

#Load Data function ! 
def load_data(data_directory):
    directories = [d for d  in os.listdir(data_directory)
                    if os.path.isdir(os.path.join(data_directory,d))]
    labels = []
    images = []

    for d in directories:
        label_directory = os.path.join(data_directory,d)
        file_names = [os.path.join(label_directory, f)
                      for f in os.listdir(label_directory)
                      if f.endswith(".ppm")]
        for f in file_names:
            images.append(data.imread(f))
            labels.append(int(d))
    return images, labels


print ("Loading Image Data.... ")
images, labels = load_data(train_data_directory)
# print ("Size of images ndim is %s , and size od labels is %s ", images.ndim, labels.ndim)

images = np.array(images)
labels = np.array(labels)

print ("Done Loading")
print("Ndim of lables ",labels.ndim)
print("Ndim of images ",images.ndim)

print("Length of images is ", len(images))
print("Length of lables is ", len(labels))


traffic_signs = [300, 2250, 3650, 4000]

for i in range(len(traffic_signs)):
    plt.subplot(1,4,i+1)
    plt.axis('off')
    plt.imshow(images[traffic_signs[i]])
    plt.subplots_adjust(wspace=0.5)

plt.show()