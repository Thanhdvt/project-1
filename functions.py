import numpy as np
from tqdm import tqdm

# Hàm nạp dữ liệu
def Loadtxt(path):
    try:
        raw = np.loadtxt(path,delimiter = ',')
        X = np.zeros((np.size(raw,0),np.size(raw,1)))
        X[:,0] = 1
        X[:,1:] = raw[:,:-1]
        y = raw[:,-1]
        yield X
        yield y
    except:
        return 0

class LinearRegression:
    def __init__(self, lr=0.01, epochs=1000):   # lr - Learnint rate: tốc độ học, epochs: số bước lặp tối đa
        self.epochs = epochs
        self.lr = lr
        self.w = 0

    # Hàm khởi tạo tham số w
    def initialize(self, n_features):
        self.w = np.zeros((n_features))

    # Hàm tính độ dốc J'(w)
    def gradient(self, X, y, n_samples):
        y_pred = self.predict(X)
        d_w = (2 / n_samples) * np.dot(X.T, (y_pred - y))
        return d_w

    def fit(self, X, y):
        # Lấy khuôn dạng X (số hàng, số cột)
        n_samples, n_features = X.shape
        # Khởi tạo tham số
        self.initialize(n_features)
        # Tính đạo hàm sau mỗi bước 
        for _ in tqdm(range(self.epochs)):
            # Cập nhật tham số 
            d_w = self.gradient(X, y, n_samples)
            self.w -= self.lr * d_w
        return self.w

    # Hàm dự đoán kết quả
    def predict(self, X):
        return np.dot(X, self.w) 


class LogisticRegression:
    def __init__(self, lr=0.01, epochs=1000):
        self.epochs = epochs
        self.lr = lr
        self.w = 0

    def initialize(self, n_features):
        self.w = np.zeros((n_features))
        
    def sigmoid(self, s):
        return 1 / (1 + np.exp(-s))

    #   Hàm tính độ dốc J'(w)
    def gradient(self, X, y, n_samples):
        y_pred = self.sigmoid(np.dot(X, self.w))
        d_w = np.dot(X.T, y_pred - y) / n_samples
        return d_w
    
    def fit(self, X, y):
        # Lấy khuôn dạng X (số hàng, số cột)
        n_samples, n_features = X.shape
        # Khởi tạo tham số
        self.initialize(n_features)
        # TÍnh đạo hàm sau mỗi bước
        for _ in tqdm(range(self.epochs)):
            # Cập nhật tham số
            d_w = self.gradient(X, y, n_samples)
            self.w -= self.lr * d_w
        return self.w

    # Hàm dự đoán kết quả
    def predict(self, X):
        return [1 if i > 0.5 else 0 for i in self.sigmoid(np.dot(X, self.w))]

