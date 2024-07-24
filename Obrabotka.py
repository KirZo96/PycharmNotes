#Импортируем библиотеку Pandas
import pandas as pd

#Читаем CSV-файл
data = pd.read_csv('Apple1.csv')
#Получаем информацию о DataFrame, нас интересует общее кол-во строк и кол-во пропусков(NaN) по столбцам
data.info()
#В столбце 'Battery Life (hours)' обнаружили 12 NaN . Это 14% от данных столбца, поэтому выбираем способ замены NaN. Строим гистограмму для помощи в выборе метода замены
data['Battery Life (hours)'].hist()
#На гистограмме видно, что в стобце 'Battery Life (hours)' большое число 0, поэтому замена на среднее по стоблцу не подходит. Выбираем метод замены NaN медианным значением
data['Battery Life (hours)'] = data['Battery Life (hours)'].fillna(data['Battery Life (hours)'] .median())
#Все значения в столбцах целочисленные, в формате float нет необходимости, поэтому меняем тип данных в 'Battery Life (hours)' на int
data['Battery Life (hours)'] = data['Battery Life (hours)'].astype(int)
#Ещё раз выводим информацию о DataFrame, чтобы проверить, нет ли некорректных значений
data.info()
#Сохраняем обработанный DataFrame для дальнейшей работы с данными
data.to_csv(r'Apple2.csv')
#Также для удоства сораняем в формате Excel
data.to_excel(r'Apple2.xlsx')