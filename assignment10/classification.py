import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the dataset into a Pandas DataFrame
data = pd.read_csv('your_dataset.csv', delimiter=' ', header=None, names=['variance', 'skewness', 'curtosis', 'entropy', 'target'])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('target', axis=1), data['target'], test_size=0.2)

# Create and train the SVM model
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# Create and train the KNN model
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

# Use the models to make predictions on the test set
svm_pred = svm_model.predict(X_test)
knn_pred = knn_model.predict(X_test)

# Evaluate the accuracy of the models
svm_accuracy = accuracy_score(y_test, svm_pred)
knn_accuracy = accuracy_score(y_test, knn_pred)

print(f"SVM accuracy: {svm_accuracy}")
print(f"KNN accuracy: {knn_accuracy}")
