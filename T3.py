import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
df = pd.read_csv('data.csv')

# Проверяем данные на пропуски
print(df.isnull().sum())  # Проверяем, есть ли пропуски
df = df.dropna(subset=['salary', 'bonus', 'years_at_company'])  # Удаляем строки с пропусками

# Убедимся, что данные имеют правильный формат
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df['bonus'] = pd.to_numeric(df['bonus'], errors='coerce')
df['years_at_company'] = pd.to_numeric(df['years_at_company'], errors='coerce')

# Создаем график
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='salary', 
    y='bonus', 
    size='years_at_company', 
    data=df, 
    sizes=(20, 200),  # Настраиваем диапазон размеров точек
    alpha=0.7,  # Прозрачность точек для лучшей читаемости
    palette="viridis"  # Цветовая палитра
)

# Настройка заголовка и меток осей
plt.title('Зависимость зарплаты и бонусов от стажа', fontsize=16)
plt.xlabel('Зарплата', fontsize=12)
plt.ylabel('Бонусы', fontsize=12)
plt.grid(True)

# Легенда для размера точек
plt.legend(title='Стаж (годы)', loc='upper left', bbox_to_anchor=(1, 1))

# Отображение графика
plt.tight_layout()
plt.show()
