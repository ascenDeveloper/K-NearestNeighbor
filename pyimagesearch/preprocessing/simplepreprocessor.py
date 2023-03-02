# Welcome to this knn example with animals dataset(you can use it in other datasets)
# This is your start point for learn to program the knn(K-NearestNeightbord)

import cv2

class SimplePreprocessor:
    def __init__(self, width, height, inter=cv2.INTER_AREA):
        self.width = width
        self.height = height
        self.inter = inter

    def preprocess(self, image):
        return cv2.resize(image, (self.width, self.height),
                         interpolation = self.inter)
    
