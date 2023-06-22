"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""

with open("task_2.txt", "w") as file:
    file.write("но у меня не получается")

with open("task_2.txt", "r") as file1, open("task_1.txt", "r") as file2:
    content1 = file1.read() 
    content2 = file2.read()  

with open("task_2.1.txt", "w") as file3:
    file3.write(content1 + content2) 