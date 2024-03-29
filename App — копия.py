﻿from joblib import load
# Загружаем модели и скейлер.
model_D = load('model_D.joblib')
model_W = load('model_W.joblib')
scaler = load('scaler.joblib')

# Просим пользователя ввести данные

# Делаем предсказание
X = scaler.transform(X)
W = model_W.predict(X)
D = model_D.predict(X)

# Выводим результат
print('Ширина шва', W[0])
print('Длинна шва', D[0])
