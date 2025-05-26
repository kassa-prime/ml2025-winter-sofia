import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class KNNRegressor:
    def __init__(self):
        self.X = []
        self.y = []
        self.n = 0
        self.model = None

    def add_point(self, x, y):
        self.X.append(x)
        self.y.append(y)
        self.n += 1

    def predict(self, x, k):
        if k > self.n:
            raise ValueError(f"k ({k}) cannot be greater than the number of points ({self.n})")
        
        X_array = np.array(self.X).reshape(-1, 1)
        y_array = np.array(self.y)
        
        self.model = KNeighborsRegressor(n_neighbors=k)
        self.model.fit(X_array, y_array)
        
        x_predict = np.array([[x]])
        return self.model.predict(x_predict)[0]

if __name__ == "__main__":
    print("""🔍 k-NN Regression Tool (Scikit-Learn) 🔍

This program will use scikit-learn's k-NN algorithm to predict the y value for a given x value (regression).

It will ask you for:
1. Number of points (N)
2. Number of neighbors (k)
3. N pairs of (x,y) coordinates
4. An x value to predict
""")

    regressor = KNNRegressor()

    while True:
        try:
            n = int(input("\n* Enter the number of points (N): "))
            if n > 0:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    while True:
        try:
            k = int(input("\n* Enter the number of neighbors (k): "))
            if k > n:
                print(f"k ({k}) cannot be greater than the number of points ({n})")
                continue
            elif k > 0:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    print("\n* Enter the points (x,y):")
    for i in range(n):
        while True:
            try:
                x = float(input(f"\n  * Point {i + 1} - x: "))
                y = float(input(f"  * Point {i + 1} - y: "))
                regressor.add_point(x, y)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    while True:
        try:
            x_predict = float(input("\n* Enter the x value to predict: "))
            break
        except ValueError:
                print("Invalid input. Please enter a number.")

    try:
        y_predicted = regressor.predict(x_predict, k)
        print(f"\nThe predicted y value is: {y_predicted:.4f}")
    except ValueError as e:
        print(f"\nError: {str(e)}")
