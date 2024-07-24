import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
import math

# Función para abrir la ventana de gestión de tareas
def open_task_manager():
    task_manager_window = tk.Toplevel(root)
    task_manager_window.title("Gestión de Tareas")
    task_manager_window.geometry("600x650")
    task_manager_window.configure(bg='blue')

    # Crear una lista de tareas
    task_listbox = tk.Listbox(task_manager_window, height=15, width=70, font=("Arial", 12), selectbackground="#cfcfcf")
    task_listbox.pack(pady=20)

    # Crear una entrada para nuevas tareas
    task_label = ttk.Label(task_manager_window, text="Nueva Tarea:", font=("Arial", 12), background='blue', foreground='white')
    task_label.pack(pady=5)
    task_entry = ttk.Entry(task_manager_window, width=50, font=("Arial", 12))
    task_entry.pack(pady=10)

    # Crear botones para añadir y eliminar tareas
    add_task_button = ttk.Button(task_manager_window, text="Añadir Tarea", command=lambda: add_task(task_entry, task_listbox))
    add_task_button.pack(pady=5)

    delete_task_button = ttk.Button(task_manager_window, text="Eliminar Tarea", command=lambda: delete_task(task_listbox))
    delete_task_button.pack(pady=5)

    # Crear botón para guardar tareas
    save_task_button = ttk.Button(task_manager_window, text="Guardar Tareas", command=lambda: save_tasks(task_listbox))
    save_task_button.pack(pady=5)

    # Cargar tareas al iniciar la aplicación
    load_tasks(task_listbox)

# Funciones para la gestión de tareas
def add_task(task_entry, task_listbox):
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debes ingresar una tarea.")

def delete_task(task_listbox):
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")

def load_tasks(task_listbox):
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())

def save_tasks(task_listbox):
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Información", "Tareas guardadas exitosamente.")

# Función para abrir la calculadora
def open_calculator():
    calculator_window = tk.Toplevel(root)
    calculator_window.title("Calculadora")
    calculator_window.geometry("550x650")
    calculator_window.configure(bg='blue')

    # Configuración de la pantalla de la calculadora
    expression = ""
    def add_to_expression(symbol):
        nonlocal expression
        expression += str(symbol)
        equation.set(expression)

    def add_function(func):
        nonlocal expression
        expression += f"math.{func}("
        equation.set(expression)

    def evaluate_expression():
        nonlocal expression
        try:
            result = str(eval(expression))
            equation.set(result)
            expression = result
        except Exception as e:
            equation.set("Error")
            expression = ""

    def clear_expression():
        nonlocal expression
        expression = ""
        equation.set("")

    equation = tk.StringVar()

    display = tk.Entry(calculator_window, textvariable=equation, font=("Arial", 24), bd=10, insertwidth=4, width=14, borderwidth=4)
    display.grid(row=0, column=0, columnspan=5)

    # Botones de la calculadora
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ('C', 4, 4), ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3), ('sqrt', 5, 4),
        (')', 5, 5)
    ]

    for (text, row, col) in buttons:
        if text == '=':
            button = tk.Button(calculator_window, text=text, padx=20, pady=20, font=("Arial", 18), command=evaluate_expression)
        elif text == 'C':
            button = tk.Button(calculator_window, text=text, padx=20, pady=20, font=("Arial", 18), command=clear_expression)
        elif text in ['sin', 'cos', 'tan', 'log', 'sqrt']:
            button = tk.Button(calculator_window, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda t=text: add_function(t))
        else:
            button = tk.Button(calculator_window, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda t=text: add_to_expression(t))
        button.grid(row=row, column=col)

    # Aviso sobre el uso de funciones matemáticas
    notice = tk.Label(calculator_window, text="Si quieres usar una función matemática, recuerda cerrar el paréntesis", font=("Arial", 12), bg='blue', fg='white')
    notice.grid(row=6, column=0, columnspan=6, pady=10)

def exit_app():
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Menú Principal")
root.geometry("400x300")
root.configure(bg='blue')

# Crear un frame para centrar los botones
center_frame = tk.Frame(root, bg='blue')
center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Crear el menú principal con botones grandes
task_manager_button = tk.Button(center_frame, text="Gestión de Tareas", font=("Arial", 16), width=20, command=open_task_manager)
task_manager_button.pack(pady=10)

calculator_button = tk.Button(center_frame, text="Calculadora", font=("Arial", 16), width=20, command=open_calculator)
calculator_button.pack(pady=10)

exit_button = tk.Button(center_frame, text="Salir", font=("Arial", 16), width=20, command=exit_app)
exit_button.pack(pady=10)

# Ejecutar el bucle principal
root.mainloop()
