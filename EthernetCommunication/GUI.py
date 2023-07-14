import tkinter
from tkinter import ttk
import ConfigData

root = tkinter.Tk()
root.geometry('512x512')
root.resizable(True, True)
root.title('Panel')
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(0, weight=3)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=50)

VehicleSpeed_GUI = tkinter.IntVar()


def slider_changed(event):
    VehicleSpeedSlider_ValueLabel.configure(text=VehicleSpeed_GUI.get())


VehicleSpeedSlider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider_changed,
    variable=VehicleSpeed_GUI
)

VehicleSpeedSlider_Label = ttk.Label(
    root,
    text='Vehicle Speed'
)

VehicleSpeedSlider_Label.grid(
    column=0,
    row=0,
    sticky=''
)

VehicleSpeedSlider.grid(
    column=1,
    row=0,
    sticky=''
)

VehicleSpeedSlider_ValueLabel = ttk.Label(
    root,
    text=VehicleSpeed_GUI.get()
)

VehicleSpeedSlider_ValueLabel.grid(
    column=1,
    row=1,
    sticky='N'
)

root.mainloop()
