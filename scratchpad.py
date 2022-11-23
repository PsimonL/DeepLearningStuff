# Data source:
# https://www.kaggle.com/smeschke/four-shapes
#%%
import os
import cv2
import matplotlib.pyplot as plt, numpy as np, seaborn as sns
from random import randint
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
print("Libs Loaded")
#%%
# PATH = r'C:/Users/szymo/PycharmProjects/shapeRecognition/shapes' # dataset file path
# IMG_SIZE = 64 # every shape image is in resolution 64x64
# shapes = ["circle", "square", "triangle", "star"] # all tipes of shapes
# labels = [] # 0-circle, 1-square, 2-triangle, 3-star
# dataset = [] # description for single image

PATH = r'C:/Users/szymo/PycharmProjects/shapeRecognition/shapes'
IMG_SIZE = 64
shapes = ["circle", "square", "triangle", "star"]
labels = []
dataset = []
#%%
# From kernel: https://www.kaggle.com/smeschke/load-data
for shape in shapes:
    print("Getting data for: ", shape)
    #iterate through each file in the folder
    dirs = os.listdir(PATH + "/" + shape)
    for file in dirs:
        #add the image to the list of images
        image = cv2.imread(PATH + shape + '/' + file)
        image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
        image = image.reshape(12288)
        dataset.append(image)
        labels.append(shapes.index(shape))


# PATH = r'C:\Users\szymo\Desktop\ProgramingStuff'
# dirs = os.listdir(PATH)
# for file in dirs:
#     print(file)




languages = ['Python', 'Java', 'JavaScript']
enumerate_prime = enumerate(languages)
# convert enumerate object to list
print(list(enumerate_prime))
# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]


import numpy as np
print((np.array([1, 2, 3, 4])).shape)