"""
Напишите программу создающую .txt файл и записывающую туда строку "Я гений и стараюсь учить питон".
Выведите первые 7 символов файла на экран.
"""

with open("task_1.txt", "w") as f:
    a = f.write("Я гений и стараюсь учить питон")
with open("task_1.txt", "r") as f:
    print(f.read(7)) 
