from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 加載數據集
iris = datasets.load_iris()
X = iris.data
y = iris.target

print(X)
print("====================================")
print(y)
print("====================================")


# 切分數據集為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(X_train)
print("====================================")
print(X_test)
print("====================================")
print(y_train)
print("====================================")
print(y_test)

# 特徵標準化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#print(X_train)
#print("====================================")
#print(X_test)

# 創建SVM分類器實例，這裡使用預設的核函數（RBF核）
model = SVC(kernel='rbf', decision_function_shape='ovo')

# 訓練模型
model.fit(X_train, y_train)

# 進行預測
y_pred = model.predict(X_test)

print(y_pred)
print("====================================")
print(y_test)
print("====================================")

# 計算準確率
accuracy = accuracy_score(y_test, y_pred)

print(f"預測準確率為: {accuracy:.2f}")


# 可視化
from matplotlib import pyplot as plt
from mlxtend.plotting import plot_decision_regions
filler_feature_values = {2: X_train[:, 2].mean(), 3: X_train[:, 3].mean()}
plot_decision_regions(X_train, y_train, clf=model, filler_feature_values=filler_feature_values)

# 標記測試集的樣本
plt.scatter(X_test[y_test == 0, 2], X_test[y_test == 0, 3], c='red', label='0')
plt.scatter(X_test[y_test == 1, 2], X_test[y_test == 1, 3], c='blue', label='1')
plt.scatter(X_test[y_test == 2, 2], X_test[y_test == 2, 3], c='green', label='2')

plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend(loc='best')

#存儲圖形
plt.savefig('decision_boundary.png')

# 顯示圖形
plt.show()