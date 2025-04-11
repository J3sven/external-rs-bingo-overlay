#!/usr/bin/env python3
import tkinter as tk
from datetime import datetime
import sys
import signal
import platform

if sys.platform == 'win32':
    import ctypes

def update_time(time_label):
    current_time = datetime.utcnow().strftime(' %d/%m/%Y %H:%M')
    time_label.config(text=f"{current_time} UTC")
    time_label.after(1000, update_time, time_label)

def on_click(event):
    global x_offset, y_offset
    x_offset = event.x
    y_offset = event.y

def move_window(event):
    new_x = event.x_root - x_offset
    new_y = event.y_root - y_offset
    root.geometry(f'+{new_x}+{new_y}')

def handle_signal(signal_num, frame):
    print("Received SIGINT (Ctrl+C), exiting...")
    root.quit()

if len(sys.argv) > 1:
    message = sys.argv[1]
else:
    message = "Squirtle Squirt"

signal.signal(signal.SIGINT, handle_signal)

root = tk.Tk()
root.geometry("170x50+100+100")
root.attributes('-topmost', True)
root.attributes('-alpha', 0.8)
root.overrideredirect(True)
root.configure(bg='#494034')

if sys.platform == 'win32':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("squirtle.taskbar.box")
    
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    current_style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, current_style | WS_EX_APPWINDOW)

else:
    root.withdraw()
    root.after(0, root.deiconify)

outer_frame = tk.Frame(root, bg='#494034', padx=3, pady=3)
outer_frame.pack(fill='both', expand=True)

message_label = tk.Label(outer_frame, text=message, font=("Helvetica", 8), fg='#03EA62', bg='#494034')
message_label.pack()

time_label = tk.Label(outer_frame, font=("Helvetica", 8), fg='white', bg='#494034')
time_label.pack()

x_offset = 0
y_offset = 0

root.bind("<Button-1>", on_click)
root.bind("<B1-Motion>", move_window)

update_time(time_label)

try:
    root.mainloop()
except KeyboardInterrupt:
    print("Application closed via KeyboardInterrupt")

root.quit()
