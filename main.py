import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def run_tema1():
    run_script("/Users/didu/Desktop/proiect pi/teme pi/tema1.py")

def run_tema2():
    run_script("/Users/didu/Desktop/proiect pi/teme pi/tema2.py")

def run_tema3():
    run_script("/Users/didu/Desktop/proiect pi/teme pi/tema3.py")

def run_tema4():
    run_script("/Users/didu/Desktop/proiect pi/teme pi/tema4.py")

def run_tema5():
    run_script("/Users/didu/Desktop/proiect pi/teme pi/tema5.py")

def run_lab1():
    run_script("/Users/didu/Desktop/proiect pi/laburi pi/lab1.py")

def run_lab2():
    run_script("/Users/didu/Desktop/proiect pi/laburi pi/lab2.py")

def run_lab3():
    run_script("/Users/didu/Desktop/proiect pi/laburi pi/lab3.py")

def run_lab4():
    run_script("/Users/didu/Desktop/proiect pi/laburi pi/lab4.py")

def run_lab5():
    run_script("/Users/didu/Desktop/proiect pi/laburi pi/lab5.py")

def run_lab6():
    run_script("/Users/didu/Desktop/proiect pi/laburi pi/lab6.py")

def run_lab7():
    run_script("/Users/didu/Desktop/proiect pi/laburi pi/lab7.py")

def run_script(path):
    if os.path.exists(path):
        try:
            subprocess.run(["python3", path], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Eroare", f"Eroare la rularea scriptului:\n{e}")
    else:
        messagebox.showerror("Eroare", f"Fișierul nu există: {path}")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Proiect Prelucrarea Imaginilor")
root.geometry("800x600")
root.configure(bg="#2c3e50")  

bg_color = "#2c3e50" 
fg_color = "#ecf0f1" 
btn_bg_color = "#16a085"  
btn_fg_color = bg_color 
frame_bg_color = "#34495e"  
highlight_color = "#e74c3c"  
exit_btn_fg_color = bg_color 

tk.Label(root, text="Laboratoare și Teme Prelucrarea Imaginilor", font=("Arial", 20, "bold"), bg=bg_color, fg=fg_color).pack(pady=20)

content_frame = tk.Frame(root, bg=bg_color)
content_frame.pack(pady=10, expand=True, fill="both")

lab_frame = tk.Frame(content_frame, bg=frame_bg_color, padx=10, pady=10)
lab_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

tk.Label(lab_frame, text="Laboratoare", font=("Arial", 16, "bold"), bg=frame_bg_color, fg=fg_color).pack(pady=10)
tk.Button(lab_frame, text="Rulare Laborator 1", command=run_lab1, bg=btn_bg_color, fg=btn_fg_color, font=("Arial", 12)).pack(pady=5)
tk.Button(lab_frame, text="Rulare Laborator 2", command=run_lab2, bg=btn_bg_color, fg=btn_fg_color, font=("Arial", 12)).pack(pady=5)
tk.Button(lab_frame, text="Rulare Laborator 3", command=run_lab3, bg=btn_bg_color, fg=btn_fg_color, font=("Arial", 12)).pack(pady=5)
tk.Button(lab_frame, text="Rulare Laborator 4", command=run_lab4, bg=btn_bg_color, fg=btn_fg_color, font=("Arial", 12)).pack(pady=5)
tk.Button(lab_frame, text="Rulare Laborator 5", command=run_lab5, bg=btn_bg_color, fg=btn_fg_color, font=("Arial", 12)).pack(pady=5)
tk.Button(lab_frame, text="Rulare Laborator 6", command=run_lab6, bg=btn_bg_color, fg=btn_fg_color, font=("Arial", 12)).pack(pady=5)
tk.Button(lab_frame, text="Rulare Laborator 7", command=run_lab7, bg=btn_bg_color, fg=btn_fg_color, font=("Arial", 12)).pack(pady=5)

tema_frame = tk.Frame(content_frame, bg=frame_bg_color, padx=10, pady=10)
tema_frame.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

tk.Label(tema_frame, text="Teme", font=("Arial", 16, "bold"), bg=frame_bg_color, fg=fg_color).pack(pady=10)
tk.Button(tema_frame, text="Rulare Tema 1", command=run_tema1, bg=btn_bg_color, fg=btn_fg_color, font=("Arial", 12)).pack(pady=5)
tk.Button(tema_frame, text="Rulare Tema 2", command=run_tema2, bg=btn_bg_color, fg=btn_fg_color, font=("Arial", 12)).pack(pady=5)
tk.Button(tema_frame, text="Rulare Tema 3", command=run_tema3, bg=btn_bg_color, fg=btn_fg_color, font=("Arial", 12)).pack(pady=5)
tk.Button(tema_frame, text="Rulare Tema 4", command=run_tema4, bg=btn_bg_color, fg=btn_fg_color, font=("Arial", 12)).pack(pady=5)
tk.Button(tema_frame, text="Rulare Tema 5", command=run_tema5, bg=btn_bg_color, fg=btn_fg_color, font=("Arial", 12)).pack(pady=5)

info_frame = tk.Frame(root, bg=bg_color, pady=10)
info_frame.pack(pady=10, fill="x")

author_info = (
    "Autor: Diana-Nicoleta Sîrbu | Universitatea de Vest Timişoara | Facultatea de Matematicǎ şi Informaticǎ | Secție: Informatică | An: III | Email: diana.sirbu03@e-uvt.ro"
)
tk.Label(info_frame, text=author_info, font=("Arial", 10, "italic"), bg=bg_color, fg=fg_color).pack()

exit_btn = tk.Button(root, text="Ieșire", command=exit_app, bg=highlight_color, fg=exit_btn_fg_color, font=("Arial", 14, "bold"))
exit_btn.pack(pady=20)

content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_columnconfigure(1, weight=1)

root.mainloop()
