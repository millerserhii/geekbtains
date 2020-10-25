import time
import tkinter as tk


window = tk.Tk()
window.title("Cветофор")
canvas = tk.Canvas(window, width=234, height=593, bg = "grey")
canvas.pack()

red_light = tk.PhotoImage(file="red.png")
orange_light = tk.PhotoImage(file="yellow.png")
green_light = tk.PhotoImage(file="green.png")
orange_light_1 = tk.PhotoImage(file="yellow.png")         # Знаю что костыль, но без него не отрабатывал цикл полностью
black = tk.PhotoImage(file="black.png")


class TrafficLight:
    __color = {green_light: 5, orange_light: 2, red_light: 7, orange_light_1: 1}

    def running(self):
        while True:
            for k, v in self.__color.items():
                canvas.create_image(0, 0, anchor="nw", image=k)
                canvas.update()
                if k == green_light:
                    time.sleep(v*0.7)
                    for _ in range(3):
                        canvas.create_image(0, 0, anchor="nw", image=black)
                        canvas.update()
                        time.sleep(0.5)
                        canvas.create_image(0, 0, anchor="nw", image=green_light)
                        canvas.update()
                        time.sleep(0.5)
                else:
                    time.sleep(v)


light = TrafficLight()
light.running()
window.mainloop()
