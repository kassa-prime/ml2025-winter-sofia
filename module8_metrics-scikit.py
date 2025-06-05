import numpy as np
from sklearn.metrics import precision_score, recall_score

class Metrics:
    def __init__(self, size):
        self.x = np.zeros(size)
        self.y = np.zeros(size)
        self.n = 0

    def add_point(self, x, y):
        self.x[self.n] = x
        self.y[self.n] = y
        self.n += 1

    def calculate_metrics(self):
        return precision_score(self.x, self.y), recall_score(self.x, self.y)

if __name__ == "__main__":
    print("""🔍 Metrics Tool (Scikit-Learn) 🔍

This program will use scikit-learn's precision and recall scores.

It will ask you for:
1. Number of points (N)
2. N pairs of (x,y) values

It will return the precision and recall scores.
""")

    while True:
        try:
            n = int(input("\n* Enter the number of points (N): "))
            if n > 0:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    metrics = Metrics(n)

    print("\n* Enter the points (x,y):")
    for i in range(n):
        while True:
            try:
                x = float(input(f"\n  * Point {i + 1} - x: "))
                y = float(input(f"  * Point {i + 1} - y: "))
                metrics.add_point(x, y)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    try:
        precision, recall = metrics.calculate_metrics()
        print(f"\nThe precision is: {precision:.4f}")
        print(f"The recall is: {recall:.4f}")
    except ValueError as e:
        print(f"\nError: {str(e)}")
