# Import library yang diperlukan
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Memuat dataset iris dari scikit-learn
iris = datasets.load_iris()
X = iris.data  # Fitur-fitur dataset iris
y = iris.target  # Label kelas iris

# Memisahkan data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membangun model K-Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=3)

# Melatih model dengan data latih
knn.fit(X_train, y_train)

# Memprediksi kelas dari data uji
y_pred = knn.predict(X_test)

# Menampilkan hasil prediksi
print("Hasil prediksi:")
for i in range(len(X_test)):
    print(f"Data uji {X_test[i]} : Prediksi {y_pred[i]}")

# Menghitung akurasi model
accuracy = knn.score(X_test, y_test)
print("Akurasi model:", accuracy)
