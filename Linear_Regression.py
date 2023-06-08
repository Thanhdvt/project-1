import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as SkLearnLN
from functions import *

[X, y] = Loadtxt('data_linear.txt')

# Phân chia dữ liệu tập Train - Test 
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)

# Khớp mô hình LinearRegression
model = LinearRegression(epochs=200000)
theta = model.fit(X_train, y_train)

# Đánh giá mô hình của tôi
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Khớp mô hình dùng thư viện scikit-learn
sklearn_model = SkLearnLN(fit_intercept=False) # fit_intercept = False for calculating the bias
sklearn_model.fit(X_train, y_train)

# Đánh giá mô hình khi dùng thư viện scikit-learn
sk_y_pred = sklearn_model.predict(X_test)
sk_mse = mean_squared_error(y_test, sk_y_pred)

# So sánh 2 kết quả thu đươc
print('Kết quả tìm bởi mô hình của tôi           ', theta)
print('Kết quả tìm bởi mô hình của scikit-learn: ', sklearn_model.coef_)

# So sánh giá trị hàm mất mát
print('Độ lệch bình phương trung bình giữa giá trị dự đoán và giá trị thực tế khi dùng mô hình của tôi:    ', mse)
print('Độ lệch bình phương trung bình giữa giá trị dự đoán và giá trị thực tế khi dùng scikit-learn:       ', sk_mse)

# Vẽ biểu đồ
plt.plot(X_test[:, 1:], y_test, 'ro', label='Thực tế')
plt.plot(X_test[:, 1:], y_pred, label='Dự đoán')
plt.title('Dự đoán doanh thu theo chi phí quảng cáo')
plt.xlabel('Chi phí quảng cáo (triệu VND)')
plt.ylabel('Doanh thu (triệu VND)')
plt.legend()
plt.show()