from joblib import load

# Просим пользователя ввести данные

# Делаем предсказание
X = scaler.transform(X)
W = model_W.predict(X)
D = model_D.predict(X)

# Выводим результат
print('Ширина шва', W[0])
print('Длинна шва', D[0])
