import tkinter as tk
import ScreenController as screen


class SettingsMenu(tk.Frame):

    brightness = 100

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        w = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, command=self.update_brightness)
        w.config(label='Screen Brightness', bg='#282a36', fg='#f8f8f2', troughcolor='#44475a', highlightthickness=0)
        w.config(bd=0, activebackground='#44475a')
        w.set(screen.get_actual_brightness())
        w.grid(row=0, column=0, padx=10, pady=10)

        if screen.get_max_brightness() == 0:
            w.config(state="disabled")

    def update_brightness(self, val):
        if screen.get_max_brightness() > 0:
            screen.set_brightness(int((int(val) / 100) * screen.get_max_brightness()))
