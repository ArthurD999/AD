import sqlite3
import data_analysis

db_connection = sqlite3.connect("iris.db")
cursor = db_connection.cursor()

columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

for col in columns:
    cursor.execute(f"select {col} from irisData")
    data = cursor.fetchall()

    col_list = []
    for i in data:
        col_list.append(i[0])
    print("           ",col.upper())
    average = data_analysis.calc_average(col_list)
    print(f"The average {col} is:{average}")

    median = data_analysis.calc_median(col_list)
    print(f"The median of {col} is:{median}")

    mode = data_analysis.calc_mode(col_list)
    print(f"The mode of {col} is:{mode}")

    freq_dict = data_analysis.calc_frequency(col_list)
    target = 4.3
    target_frequency = freq_dict.get(target, 0)
    print(f"The frequency of {target} in {col} is:{target_frequency}")

    col_range = data_analysis.calc_range(col_list)
    print(f"The range of {col} is:{col_range}")
    
    print()

cursor.close()
db_connection.close()