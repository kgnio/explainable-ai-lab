
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Örnek eğitim verisi
data = pd.DataFrame({
    "income": [70000, 35000, 55000, 90000, 25000, 45000],
    "debt": [10000, 80000, 30000, 5000, 95000, 40000],
    "late_payments": [0, 3, 1, 0, 4, 2],
    "risk": [0, 1, 0, 0, 1, 1]
})

X = data[["income", "debt", "late_payments"]]
y = data["risk"]

model = DecisionTreeClassifier(max_depth=2, random_state=42)
model.fit(X, y)

customer = pd.DataFrame([{
    "income": 55000,
    "debt": 30000,
    "late_payments": 1
}])

print("İlk tahmin:", model.predict(customer)[0])

changed = customer.copy()
changed["debt"] = 90000

print("Yeni tahmin:", model.predict(changed)[0])

print("\nGlobal Feature Importance:")
for feature, importance in zip(
    X.columns, model.feature_importances_
):
    print(f"{feature}: {importance:.3f}")
