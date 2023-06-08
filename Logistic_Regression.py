import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import log_loss
from sklearn.linear_model import LogisticRegression as SkLearnLG
from functions import *

[X, Y] = Loadtxt('data_logistic.txt')

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.3)

# Khớp mô hình LogisticRegression
model = LogisticRegression(lr=0.1, epochs=200000)
theta = model.fit(X_train, Y_train)

# Đánh giá mô hình của tôi
Y_pred = model.predict(X_test)
print("Đánh giá mô hình của tôi\n", classification_report(Y_test, Y_pred))
bce = log_loss(Y_test, Y_pred)

# Khớp mô hình dùng thư viện scikit-learn
sklearn_model = SkLearnLG(penalty=None, fit_intercept=False) 
sklearn_model.fit(X_train, Y_train)

# Đánh giá mô hình khi dùng thư viện scikit-learn
sk_y_pred = sklearn_model.predict(X_test)
print("Đánh giá mô hình khi dùng SkLearn\n", classification_report(Y_test, sk_y_pred))
sk_bce = log_loss(Y_test, sk_y_pred)

# So sánh 2 kết quả thu đươc
print('Kết quả tìm bởi mô hình của tôi           ', theta)
print('Kết quả tìm bởi mô hình của scikit-learn: ', sklearn_model.coef_)

# So sánh giá trị hàm mất mát
print('Giá trị hàm mất mát khi dùng mô hình của tôi:    ', bce)
print('Giá trị hàm mất mát khi dùng scikit-learn:       ', sk_bce)

# Vẽ biểu đồ
X0 = X_test.T[1, np.where(Y_test == 0)][0]
y0 = Y_test[np.where(Y_test == 0)]
X1 = X_test.T[1, np.where(Y_test == 1)][0]
y1 = Y_test[np.where(Y_test == 1)]

plt.plot(X0, y0, 'ro', markersize = 8, label = 'Không đạt')
plt.plot(X1, y1, 'bs', markersize = 8, label = 'Đạt')

xx = np.linspace(0, 7, 5000)
w0 = theta[0]
w1 = theta[1]
threshold = -w0/w1
yy = LogisticRegression().sigmoid(w0 + w1*xx)

plt.plot( xx, yy, 'g-', linewidth = 2, label = 'Đường dự đoán')
plt.plot(threshold, .5, 'y^', markersize = 8, label = 'Ngưỡng cứng')
plt.xlabel('Số giờ học')
plt.ylabel('Xác suất vượt qua kì thi')
plt.title('Xác suất vượt qua kì thi so với số giờ học')
plt.legend()
plt.show()