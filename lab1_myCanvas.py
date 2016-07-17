from tkinter import*
from tkinter import messagebox

class Paint:
    __root = Tk()
    __canv = Canvas(__root, width=388, height=400,bg="blue", cursor="hand2")
    __canv.place(x=10,y=10)
    __toRight=5
    __toTop=5
    __array=[]
    __arrayStart= 0
    __arrayFinish= 0
    __arrayField = []
    __isStart=True
    __isEnd=True
    __options = ""

    def __init__(self):
        self.__root.geometry("800x600")
        self.__setUI()

    # create menu
    def __setUI(self):
        self.__canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5, sticky=E+W+S+N)  # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке, и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна

        red_btn = Button(self.__root, text="Вычислить",command=self.__buttonClick, width=10) # Создание кнопки:  Установка текста кнопки, задание ширины кнопки (10 символов)
        red_btn.grid(row=10, column=0) # Устанавливаем кнопку первый ряд, вторая колонка

    def __buttonClick(self):
       # messagebox.showinfo('',self.__options)
        self.drawPath()

    def __callback(self, e):
        item = self.__canv.find_closest(e.x, e.y)
        self.__arrayField.append(item)
        self.__canv.itemconfig(item,outline='white',width=2,fill='red')

    def __callbackByStartAndFinish(self, e):
        if self.__isStart:
            item = self.__canv.find_closest(e.x, e.y)
            self.__arrayStart=item
            self.__canv.itemconfig(item,outline='white',width=2,fill='orange')
            self.__isStart=False
        elif self.__isEnd:
            item = self.__canv.find_closest(e.x, e.y)
            self.__arrayFinish = item
            self.__canv.itemconfig(item,outline='white',width=2,fill='black')
            self.__isEnd=False

    def draw(self):
        for rectNumX in range(1,11):
            for rectNumY in range(1,19):
                self.__array.append('rect_'+str(rectNumX))
                rect = self.__canv.create_rectangle(0+self.__toRight, 2+self.__toTop, 20+self.__toRight,
                  40+self.__toTop, width=1,fill='#289d0a',outline='black',tag=self.__array[rectNumX-1])
                self.__toRight+=21
            self.__toTop+=39
            self.__toRight=5

    def drawPath(self):
        self.__toRight = 5
        self.__toTop = 5

        if self.__arrayStart!=0:
            n = self.__arrayStart
            self.__canv.itemconfig(n,outline='white',width=4,fill='#289999')
            self.__arrayStart = int(self.__arrayStart[0]+1)
            self.__canv.itemconfig(self.__arrayStart,outline='white',width=4,fill='#289999')

        if self.__arrayFinish!=0:
            self.__canv.itemconfig(self.__arrayFinish,outline='white',width=4,fill='#289999')

        for rectNumX in range(0,11):
            for rectNumY in range(0,19):
                if self.__arrayField[rectNumX]!=0:
                    self.__canv.itemconfig(self.__arrayField.pop(rectNumX),outline='white',width=4,fill='red')


    def drawWalls(self):
        for rectNum in self.__array:
            self.__canv.tag_bind(rectNum,'<ButtonPress-1>', self.__callback)

        for rectNum in self.__array:
            self.__canv.tag_bind(rectNum,'<ButtonPress-3>', self.__callbackByStartAndFinish)

def main():
    paint = Paint()
    paint.draw()
    #paint.drawPath()
    paint.drawWalls()
    mainloop()

if __name__ == "__main__":
    main()