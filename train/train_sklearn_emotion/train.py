import os
import pickle

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.svm import SVC

# define models dir path
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load data from the text file
data_file = "data.txt"
data = np.loadtxt(data_file)

# Split data into features (X) and labels (y)
X = data[:, :-1]  # face data except the last one
y = data[:, -1]   # labels the last column

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42,
                                                    shuffle=True,
                                                    stratify=y)

# Initialize the Random Forest Classifier
rf_classifier = RandomForestClassifier()
svm_classifier = SVC(kernel='linear')

# Train the classifier on the training data
rf_classifier.fit(X_train, y_train)
svm_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = rf_classifier.predict(X_test)
y_pred_svm = svm_classifier.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print(confusion_matrix(y_test, y_pred))

accuracy_svm = accuracy_score(y_test, y_pred_svm)
print(f"SVM Accuracy: {accuracy_svm * 100:.2f}%")
print(confusion_matrix(y_test, y_pred_svm))

model_path = os.path.join(base_dir, '../../models/model_4.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(rf_classifier, f)

# Save the SVM model
svm_model_path = os.path.join(base_dir, '../../models/svm_model.pkl')
with open(svm_model_path, 'wb') as f:
    pickle.dump(svm_classifier, f)