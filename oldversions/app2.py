import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

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

# Funciones
def add_task(task_entry, task_listbox):
    task = task_entry.get()

    if task != "":
        task_listbox.insert(tk.END, f"{task}")
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

exit_button = tk.Button(center_frame, text="Salir", font=("Arial", 16), width=20, command=exit_app)
exit_button.pack(pady=10)

# Diccionario de categorías y subcategorías
categories = {
    "Trabajo": ["Proyecto A", "Proyecto B"],
    "Personal": ["Hogar", "Salud"],
    "Estudio": ["Curso A", "Curso B"],
    "Otros": ["Misc"]
}

# Ejecutar el bucle principal
root.mainloop()
