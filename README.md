# Nearest-Centroid-Classifier
## Reading and Preprocessing the Data
The function load_data(csv_filename) reads in wine data from an inputted CSV file and returns a numpy ndarray in which each row represents a wine and each column represents a chemical measurement.<br><br>
The function split_data(dataset, ratio) splits the data set into a training and testing portion. The function should return a (training set, testing set) tuple of ndarrays. The ratio parameter determines how much of the data should be assigned to training and how much should be used for testing.
## Nearest Centroid classifier
The function experiment(ww_training, rw_training, ww_test, rw_test) reads in training and test data sets and performs the following steps:
- Creates a centroid for each class (red or white) by computing averages of each measurement within the class using the compute_centroid function.
- Makes a prediction for the color by measuring the euclidean distance of this data item to each of the centroids.
- Keeps track of how many correct predictions this model makes.
- Prints out the total number of predictions made, the number of correct predictions, and the accuracy of the model.
- Returns the accuracy of the model.
## Cross Validation
When working with relatively small testing sets results may not be reliable.  It is possible that a small testing set contains only input instances that are easy or difficult to predict.  Selecting a different test data set of the same size might lead to different results.  One common solution is to perform k-fold cross validation.  We perform k training/testing repetitions. In each repetition we test on one of the k partitions after training on the remaining k-1 partitions. In this way, each of the partitions will be tested on once. We can then average the accuracy we got for each of the k repetitions.<br>
The function cross_validaiton(ww_data, rw_data, k) performs k-fold cross validation and returns the average accuracy.
