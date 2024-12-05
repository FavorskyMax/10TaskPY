import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных
# Предположим, у вас есть файл data.csv с необходимыми столбцами
df = pd.read_csv('data.csv')

# Проверяем наличие данных и их корректность
print(df.info())  # Проверяем пропуски и типы данных
print(df.head())  # Просматриваем первые строки

# Убедимся, что данные имеют числовые значения
df['age'] = pd.to_numeric(df['age'], errors='coerce')  # Преобразуем в числовой формат, если нужно
df['spending_score'] = pd.to_numeric(df['spending_score'], errors='coerce')

# Убираем строки с пропусками
df = df.dropna(subset=['age', 'spending_score'])

# Построение графика
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(x='age', y='spending_score', data=df, marker='o', ci=None)

# Настройка оформления графика
plt.title('Возраст и Балл по расходам', fontsize=16)
plt.xlabel('Возраст', fontsize=12)
plt.ylabel('Балл по расходам', fontsize=12)
plt.grid(True)
plt.show()

