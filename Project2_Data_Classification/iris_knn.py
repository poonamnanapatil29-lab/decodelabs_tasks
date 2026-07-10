# iris_knn.py

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create KNN model
knn = KNeighborsClassifier(n_neighbors=3)

# Train the model
knn.fit(X_train, y_train)

# Predict on test data
y_pred = knn.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("=" * 50)
print("      IRIS FLOWER CLASSIFICATION USING KNN")
print("=" * 50)

print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

print("\nSample Predictions:")
print("-" * 50)

for i in range(5):
    actual = target_names[y_test[i]]
    predicted = target_names[y_pred[i]]
    print(f"Sample {i+1}")
    print(f"Actual    : {actual}")
    print(f"Predicted : {predicted}")
    print()

# User Prediction
print("=" * 50)
print("Predict Your Own Iris Flower")
print("=" * 50)

try:
    sepal_length = float(input("Enter Sepal Length (cm): "))
    sepal_width = float(input("Enter Sepal Width (cm): "))
    petal_length = float(input("Enter Petal Length (cm): "))
    petal_width = float(input("Enter Petal Width (cm): "))

    user_data = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]

    prediction = knn.predict(user_data)

    print("\nPredicted Flower Species:")
    print(target_names[prediction[0]].capitalize())

except ValueError:
    print("\nPlease enter valid numeric values.")