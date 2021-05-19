#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import math
import scipy
from matplotlib import pyplot as plt
from sklearn.model_selection import KFold

def euclidean_distance(a,b):
    diff = a - b
    return np.sqrt(np.dot(diff, diff))

def load_data(csv_filename):
    """ 
    Returns a numpy ndarray in which each row repersents
    a wine and each column represents a measurement. There should be 11
    columns (the "quality" column cannot be used for classificaiton).
    """
    data = np.genfromtxt(csv_filename, delimiter=';', skip_header = 1, usecols = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))    #read in input except for the last column
    
    return data    #return data representation
    
def split_data(dataset, ratio = 0.9):
    """
    Return a (train, test) tuple of numpy ndarrays. 
    The ratio parameter determines how much of the data should be used for 
    training. For example, 0.9 means that the training portion should contain
    90% of the data. You do not have to randomize the rows. Make sure that 
    there is no overlap. 
    """
    num_train = int(ratio * len(dataset))   #obtain the number that you want the training data from using the ratio passed in 
    train = dataset[:num_train]             #obtain the training data in np array form
    test = dataset[num_train:]              #obtain the teesting data in np array form
 
    return(train, test)                     #return tuple of training and testing arrays
    
    pass
    
def compute_centroid(data):
    """
    Returns a 1D array (a vector), representing the centroid of the data
    set. 
    """
    
    centroid = sum(data[:,:])/len(data)     #construct 1d numpy array representing centroid
    return centroid                         #return centroid
    
    
    pass
    
def experiment(ww_train, rw_train, ww_test, rw_test):
    """
    Train a model on the training data by creating a centroid for each class.
    Then test the model on the test data. Prints the number of total 
    predictions and correct predictions. Returns the accuracy. 
    """
    ww_centroid = compute_centroid(ww_train)   #obtain the centroid for the white wine training data set
    rw_centroid = compute_centroid(rw_train)   #obtain the centroid for the red wine training data set
    
    model = {"white wine": ww_centroid, "red wine": rw_centroid}
    
    wrong = []
    correct = 0
    total = 0
    
  

    for instance in ww_test:                 #for each instance in the white wine testing data set
            white_wine_distance = euclidean_distance(model["white wine"], instance)    #obtain euclidean distance for white wine
            red_wine_distance = euclidean_distance(model["red wine"], instance)        #obtain euclidean distance for white wine
            if white_wine_distance < red_wine_distance:     #if the white wine distance is less than the red wine distance
                correct += 1
            else:
                wrong.append(instance)
            total += 1
        
    
    for instance in rw_test:              #same logic as above
            white_wine_distance = euclidean_distance(model["white wine"], instance)
            red_wine_distance = euclidean_distance(model["red wine"], instance)
            if white_wine_distance > red_wine_distance:
                correct += 1
            else:
                wrong.append(instance)
            total += 1  
    
        
    accuracy = correct/total             #take average of correct predictions to obtain accuracy
    print("Accuracy: {}, ({}/{} correct predictions)".format(accuracy, correct, total))
            
    return accuracy
    
    
    
    pass
    
def cross_validation(ww_data, rw_data, k):
    """
    Perform k-fold crossvalidation on the data and print the accuracy for each
    fold. 
    """
    accuracy = []
    num_groups = (int(len(ww_data)/k))    #split data into k groups
    counter = num_groups + 1              #even out data set
    
    for i in range(k):                    #for k-iterations
        
        ww_train = np.vstack((ww_data[0:counter*i],ww_data[counter*(i+1):]))    #construct white training data set from each iteration
        ww_test = ww_data[counter*i:counter*(i+1)]                              #construct white testing data set from each iteration
        rw_train = np.vstack((rw_data[0:counter*i],rw_data[counter*(i+1):]))    #construct red training data set from each iteration
        rw_test = rw_data[counter*i:counter*(i+1)]                              #construct red testing data set from each iteration
        accuracy.append(experiment(ww_train, rw_train, ww_test, rw_test))
        
        
    return sum(accuracy)/len(accuracy)   #return average accuracy


    pass

    
if __name__ == "__main__":
    
    ww_data = load_data('whitewine.csv')
    rw_data = load_data('redwine.csv')

    # Uncomment the following lines for step 2: 
    ww_train, ww_test = split_data(ww_data, 0.9)
    rw_train, rw_test = split_data(rw_data, 0.9)
    experiment(ww_train, rw_train, ww_test, rw_test)
    
    # Uncomment the following lines for step 3:
    k = 10
    acc = cross_validation(ww_data, rw_data, k)
    print("{}-fold cross-validation accuracy: {}".format(k,acc))
    
