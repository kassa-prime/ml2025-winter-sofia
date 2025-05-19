import numpy as np

class KNNRegressor:
    def __init__(self):
        self.X = None  # x coordinates
        self.y = None  # y coordinates
        self.n = 0     # number of points

    # The indices will be respected to calculate the prediction efficiently
    def add_point(self, x, y):
        if self.X is None:
            self.X = np.array([x])
            self.y = np.array([y])
        else:
            self.X = np.append(self.X, x)
            self.y = np.append(self.y, y)
        self.n += 1

    def predict(self, x, k):
        if k > self.n:
            raise ValueError(f"k ({k}) cannot be greater than the number of points ({self.n})")
        
        # Calculate distances to all points (l1 or l2 is the same for 1-D)
        distances = np.abs(self.X - x)
        
        # Get indices of k nearest neighbors (used to get the y values--predictions)
        k_indices = np.argsort(distances)[:k]
        
        # Calculate the average y value of k nearest neighbors
        return np.mean(self.y[k_indices])

if __name__ == "__main__":
    print("""🔍 k-NN Regression Tool 🔍

This program will use the k-NN algorithm to predict the y value for a given x value (regression).

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
