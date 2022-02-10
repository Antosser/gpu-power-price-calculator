import tkinter as tk
import time
import datetime
from turtle import st
import threading
import gpupower

starttime = None
powerarray = []

root = tk.Tk(className=' GPU Price Calculator')
root.configure(bg='white')
root.geometry("300x300")
root.resizable(False, False)
frame = tk.Frame(root, relief = 'sunken', bd = 1, bg = 'white')
frame.pack(fill = 'both', expand = True, padx = 15, pady = 15)

powerused = tk.Label(frame, text="")
priceinput = tk.Entry(frame)
priceoutput = tk.Label(frame)

def add_and_calculate_power():
    while True:
        power = gpupower.getPower()
        powerarray.append(power)
        sum = 0
        for i in powerarray:
            sum += i
        sum /= len(powerarray)
        kWh = sum * (datetime.datetime.now() - starttime).seconds / 3600 / 1000
        powerused.config(text=str(round(kWh, 3)) + ' kWh')
        try:
            priceoutput.config(text=round(kWh * float(priceinput.get()), 3))
        except Exception:
            pass
        time.sleep(.5)

def handle_click(event):
    global starttime

    if starttime is not None:
        return
    starttime = datetime.datetime.now()
    tk.Label(frame, text=starttime.strftime("%Y-%m-%d %H:%M:%S")).pack()
    tk.Label(frame, text='Used:', background='white').pack()
    powerused.pack()
    tk.Label(frame, text='Price / kWh:', background='white').pack()
    priceinput.pack()
    tk.Label(frame, text='Price:', background='white').pack()
    priceoutput.pack()
    threading.Thread(target=add_and_calculate_power).start()

startbutton = tk.Button(frame, text='Start', padx=5, pady=5)
startbutton.bind("<Button-1>", handle_click)
startbutton.pack()

tk.Label(frame, text='Starttime:', background='white').pack()

root.mainloop()