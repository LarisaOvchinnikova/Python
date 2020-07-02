import os
# относительный путь к файлу
print(os.getcwd()) #"D:/StudyingPython/1 - Python-2/13 - files/HW13/2. Baby Names Ranking.py"
homework = os.getcwd()
name ="\\babynamesranking2010.txt"
path = os.getcwd() + name
file = open(path)
print(file)
print(os.path.join(homework, name))

os.chdir()