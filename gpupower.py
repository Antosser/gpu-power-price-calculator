import os
import tkinter as tk

def getPower():
    try:
        output = os.popen('nvidia-smi --display=power -q').read().split('\n')[11]
    except:
        tk.messagebox.showerror('Error', 'Cound not find Nvidia Smi')
    return float(output[44:49])