
def predict_risk(income, debt, late_payments):
    risk = 20 + (debt / income) * 35 + late_payments * 15
    return max(0, min(100, risk))


customer = {
    "income": 55000,
    "debt": 30000,
    "late_payments": 1
}

result = predict_risk(**customer)

print(f"Risk puanı: {result:.2f}")

# Şimdi yalnızca borç miktarını değiştiriyoruz.
customer["debt"] = 60000

new_result = predict_risk(**customer)

print(f"Yeni risk puanı: {new_result:.2f}")
print(f"Değişim: {new_result - result:+.2f}")
