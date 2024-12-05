import pandas as pd
import random

# Генерация DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание one-hot кодирования
unique_values = data['whoAmI'].unique()  # Находим уникальные значения
one_hot = pd.DataFrame()  # Создаем пустой DataFrame для one-hot кодирования

# Генерируем столбцы для каждого уникального значения
for value in unique_values:
    one_hot[value] = (data['whoAmI'] == value).astype(int)

# Объединение one-hot кодирования с исходным DataFrame (опционально)
data = pd.concat([data, one_hot], axis=1)

# Результат
print(data.head())
