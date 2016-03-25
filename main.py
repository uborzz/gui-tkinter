from Tkinter import *
import time
import threading

counter = 0
tAnterior = time.time()
tRefresh = time.time()

#definir el objeto para correrlo en multihilo
class gUI(threading.Thread):
    def __init__(self):

        self.vent = Tk()
        self.varDisplay = StringVar()
        self.varDisplay.set(counter)
        marco = Frame()

        def resetVar():
            global counter
            counter = 0


        def sumaVar():
            global counter
            counter+=1


        def restaVar():
            global counter
            counter-=1


        label = Label(self.vent, text = "Tr4mBolik0unt3r", fg = "Red", font=("Calibri", 18))
        display = Label(self.vent, textvariable = self.varDisplay, font=("Calibri", 50, "bold"))


        label.pack()
        display.pack()
        marco.pack()

        bReset = Button(marco, text = "Reset", command = resetVar, height = 1, width = 9, font = ("Calibri", 21))
        bSuma = Button(marco, text = "+", command = sumaVar, height = 1, width = 3, font = ("Calibri",30, "bold"))
        bResta = Button(marco, text = "-", command = restaVar, height =1, width = 3, font = ("Calibri",30, "bold"))

        label.pack()
        display.pack()

        bReset.pack(side = TOP)
        bSuma.pack(side = RIGHT)
        bResta.pack(side = LEFT)

        threading.Thread.__init__(self)

    def run(self):
        self.vent.mainloop()

#en la inicializacion lanzamos el hilo con la visu
app = gUI()
app.start()

while 1:
    #refresco del valor mostrado en la visu
    if (time.time()-tRefresh) >= 0.1:
        tRefresh = time.time()
        app.varDisplay.set(counter)

    #Para pruebas - BORRAR
    if (time.time() - tAnterior) >= 1:
         counter += 1
         tAnterior = time.time()
  #      print counter




