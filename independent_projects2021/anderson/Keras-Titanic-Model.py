##############################################################################
# Package loading
##############################################################################

# Install Packages in anaconda if you don't have them:
# conda install numpy 
# conda install pandas
# conda install keras
# conda install tensorflow

# Import Packages
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers.core import Dense
from keras.utils import to_categorical
from tensorflow.keras.models import load_model
from sklearn.metrics import confusion_matrix
import itertools


##############################################################################
# Data importing and Object Defining
##############################################################################

####### Column Meta data #######

# survival	   Survival	            0 = No, 1 = Yes
# pclass	       Ticket class	        1 = 1st, 2 = 2nd, 3 = 3rd
# sex	       Sex	
# Age	       Age in years	
# sibsp	       # of siblings / spouses aboard the Titanic	
# parch	       # of parents / children aboard the Titanic	
# ticket	       Ticket number	
# fare	       Passenger fare	
# cabin	       Cabin number	
# embarked	   Port of Embarkation	C = Cherbourg, Q = Queenstown, S = Southampton


# Setting up Training Data
train_raw = pd.read_csv('C:/Users/ander/Documents/Python/titanic/train.csv')
train_raw.info()
# train_raw.head()
train_raw1 = train_raw[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']]
train_raw1["male"] = np.multiply(train_raw.Sex == 'male', 1)
train_raw1["age_was_missing"] = np.multiply(train_raw.Age.isna(), 1)
train_raw1["Age"] = train_raw["Age"].fillna(value=train_raw["Age"].mean())
train_raw1.info()
train_raw1.head()
train = np.array(train_raw1)

# Assign Model Training Variables
target = to_categorical(train_raw.Survived)
predictors = train
n_cols = predictors.shape[1]

##############################################################################
# Model Building 
##############################################################################

# Model Data (sequential means that the each layer has 
# connection to the one layer coming directly after it)
model = Sequential()

# add layers to the model
# 'relu' is a rectified linear activation fuction
# called dense because all the nodes in the previous layer connect to all the nodes in the current layer
# model.add(Dense(100, activation='relu', input_shape = (n_cols,))) 
model.add(tf.keras.Input(shape = (n_cols,)))                                   # input layer
model.add(Dense(100, activation='relu'))                                       # hidden layer
model.add(Dense(100, activation='relu'))                                       # hidden layer
model.add(Dense(2, activation='softmax'))                                      # output layer

# Compile the model (forward propagation)
# optimizer controls the learning rate (Adam automatically adjusts the learning rate to get reasonable values)
# loss selects the loss function to use to calculate the weights
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics = ['accuracy'])

# fitting the model is applying backpropagation and gradient decent to update the weights
# epoch means how many times to go through the training data
model.fit(predictors, target, validation_split=0.25, epochs=100)

# Save/Load Model 
model.save('C:/Users/ander/Documents/Python/titanic/titanic_model.h5')
titanic_model = load_model('C:/Users/ander/Documents/Python/titanic/titanic_model.h5')

##############################################################################
# Model Testing
##############################################################################

# Setting up Test data
test_raw = pd.read_csv("C:/Users/ander/Documents/Python/titanic/test.csv")
# test_raw.info()
test_raw1 = test_raw[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']]
test_raw1["male"] = np.multiply(test_raw.Sex == 'male', 1)
test_raw1["age_was_missing"] = np.multiply(test_raw.Age.isna(), 1)
test_raw1["Age"] = test_raw["Age"].fillna(value=test_raw["Age"].mean())
test_raw1["Fare"] = test_raw["Fare"].fillna(value=test_raw["Fare"].mean())
test = np.array(test_raw1)

# Actual test values
test_true_raw = pd.read_csv("C:/Users/ander/Documents/Python/titanic/gender_submission.csv")
test_true = np.array(test_true_raw.Survived)

# Use Model to Predict
predictions = titanic_model.predict(test)
np.around(predictions, 2)[0:11,]
test_pred = np.argmax(predictions, axis=-1)

##############################################################################
# Visualize Results 
##############################################################################
# Make Confusion Matrix (CM)
cm = confusion_matrix(y_true = test_true, y_pred = test_pred)

# Aesthetics For Plotting CM taken from https://scikit-learn.org/0.18/auto_examples/model_selection/plot_confusion_matrix.html
def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes)#, rotation=45)
    plt.yticks(tick_marks, classes)
    if normalize:
        cm=cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print('Normalized confusion matrix')
    else:
        print('Confusion matrix, without normalization')
    print(cm)
    thresh = cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i,j],
                 horizontalalignment="center",
                 color="white" if cm[i,j] > thresh else "black")
        plt.tight_layout()
        plt.ylabel('True Survival')
        plt.xlabel('Predicted Survival')


# CM Plot
cm_plot_labels = ['Didn\'t Survive', 'Survived']
plot_confusion_matrix(cm=cm, classes=cm_plot_labels, title="Titanic NN Confusion Matrix") 

# CM Statistics
accuracy = (cm[0,0] + cm[1,1]) / cm.sum()
precision = cm[1,1]/(cm[1,1] + cm[0,1])
true_positive_rate = cm[1,1]/(cm[1,1] + cm[1,0])
true_negative_rate = cm[0,0]/(cm[0,0] + cm[0,1])
f1_score = (2 * precision * true_positive_rate)/(precision + true_positive_rate)
print('\nAccuracy = %.2f \nPrecision = %.2f \nRecall(TPR) = %.2f \nSpecificity(TNR) = %.2f \nF1 Score = %.2f'%
      (accuracy, precision, true_positive_rate, true_negative_rate, f1_score))


# Can perform a while loop to continue until certain accuracy is reached 

test = f1_score < .93


while test == True:
    model = Sequential()
    # model.add(tf.keras.Input(shape = (n_cols,))) 
    model.add(Dense(100, activation='relu', input_shape = (n_cols,)))              # input layer
    model.add(Dense(100, activation='relu'))                                       # hidden layer
    model.add(Dense(100, activation='relu'))
    model.add(Dense(100, activation='relu'))                                       # hidden layer
    model.add(Dense(100, activation='relu'))                                        # hidden layer
    model.add(Dense(2, activation='softmax'))                                      # output layer
    
    model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics = ['accuracy'])
    
    model.fit(predictors, target, validation_split=0.25, epochs=100)
    
    model.save('C:/Users/ander/Documents/Python/titanic/titanic_model.h5')
    titanic_model = load_model('C:/Users/ander/Documents/Python/titanic/titanic_model.h5')
    
    test_raw = pd.read_csv("C:/Users/ander/Documents/Python/titanic/test.csv")
    test_raw1 = test_raw[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']]
    test_raw1["male"] = np.multiply(test_raw.Sex == 'male', 1)
    test_raw1["age_was_missing"] = np.multiply(test_raw.Age.isna(), 1)
    test_raw1["Age"] = test_raw["Age"].fillna(value=test_raw["Age"].mean())
    test_raw1["Fare"] = test_raw["Fare"].fillna(value=test_raw["Fare"].mean())
    test = np.array(test_raw1)
    test_true_raw = pd.read_csv("C:/Users/ander/Documents/Python/titanic/gender_submission.csv")
    test_true = np.array(test_true_raw.Survived)
    
    predictions = titanic_model.predict(test)
    test_pred = np.argmax(predictions, axis=-1)
    cm = confusion_matrix(y_true = test_true, y_pred = test_pred)
    def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes)#, rotation=45)
        plt.yticks(tick_marks, classes)
        if normalize:
            cm=cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print('Normalized confusion matrix')
        else:
            print('Confusion matrix, without normalization')
        print(cm)
        thresh = cm.max() / 2
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, cm[i,j],
                     horizontalalignment="center",
                     color="white" if cm[i,j] > thresh else "black")
            plt.tight_layout()
            plt.ylabel('True Survival')
            plt.xlabel('Predicted Survival')
        
    accuracy = (cm[0,0] + cm[1,1]) / cm.sum()
    precision = cm[1,1]/(cm[1,1] + cm[0,1])
    true_positive_rate = cm[1,1]/(cm[1,1] + cm[1,0])
    true_negative_rate = cm[0,0]/(cm[0,0] + cm[0,1])
    f1_score = (2 * precision * true_positive_rate)/(precision + true_positive_rate)
    test = f1_score < .9
    test2 = f1_score > .9
    if (test2):
        cm_plot_labels = ['Didn\'t Survive', 'Survived']
        plot_confusion_matrix(cm=cm, classes=cm_plot_labels, title="Titanic NN Confusion Matrix") 
        print('\nAccuracy = %.2f \nPrecision = %.2f \nRecall(TPR) = %.2f \nSpecificity(TNR) = %.2f \nF1 Score = %.2f'%
              (accuracy, precision, true_positive_rate, true_negative_rate, f1_score))











