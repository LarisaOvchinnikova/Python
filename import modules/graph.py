import graphics
from graphics import * # импортируем библиотеку graphics
win = GraphWin("Окно для графики", 400, 400) # создаём окно для графики размером 400 на 400 пикселей
obj = Point(50, 50) # создаём точку в координатах (50, 50)
obj.draw(win) # отображаем точку в окне для графики


win.getMouse() # ждём нажатия кнопки мыши
win.close() # закрываем окно для графики