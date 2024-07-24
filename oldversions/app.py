import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os


# Funciones
def add_task():
    task = task_entry.get()
    category = category_combobox.get()
    subcategory = subcategory_combobox.get()
    if task != "":
        task_listbox.insert(tk.END, f"{task} - [{category} -> {subcategory}]")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debes ingresar una tarea.")


def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")


def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())


def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Información", "Tareas guardadas exitosamente.")


def add_category():
    new_category = category_entry.get()
    if new_category != "":
        categories[new_category] = []
        category_combobox["values"] = list(categories.keys())
        category_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debes ingresar una categoría.")


def add_subcategory():
    category = category_combobox.get()
    new_subcategory = subcategory_entry.get()
    if category != "Seleccionar Categoría" and new_subcategory != "":
        categories[category].append(new_subcategory)
        subcategory_combobox["values"] = categories[category]
        subcategory_entry.delete(0, tk.END)
    else:
        messagebox.showwarning(
            "Advertencia",
            "Debes seleccionar una categoría y ingresar una subcategoría.",
        )


def update_subcategories(event):
    category = category_combobox.get()
    subcategory_combobox["values"] = categories.get(category, [])
    subcategory_combobox.set("Seleccionar Subcategoría")


# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("500x700")
root.resizable(False, False)  # Evitar redimensionar la ventana

# Establecer un tema
style = ttk.Style(root)
style.theme_use(
    "clam"
)  # Puedes probar con otros temas: 'default', 'classic', 'vista', 'xpnative'
# Establecer el color de fondo de la ventana principal
root.configure(bg="blue")


# Diccionario de categorías y subcategorías
categories = {
    "Trabajo": ["Proyecto A", "Proyecto B"],
    "Personal": ["Hogar", "Salud"],
    "Estudio": ["Curso A", "Curso B"],
    "Otros": ["Misc"],
}

# Crear una lista de tareas
task_listbox = tk.Listbox(
    root, height=15, width=70, font=("Arial", 12), selectbackground="#cfcfcf"
)
task_listbox.pack(pady=20)

# Crear una entrada para nuevas tareas
task_label = ttk.Label(root, text="Nueva Tarea:", font=("Arial", 12))
task_label.pack(pady=5)
task_entry = ttk.Entry(root, width=50, font=("Arial", 12))
task_entry.pack(pady=10)

# Crear un combobox para las categorías
category_label = ttk.Label(root, text="Categoría:", font=("Arial", 12))
category_label.pack(pady=5)
category_combobox = ttk.Combobox(
    root, values=list(categories.keys()), font=("Arial", 12), state="readonly"
)
category_combobox.set("Seleccionar Categoría")
category_combobox.pack(pady=10)
category_combobox.bind("<<ComboboxSelected>>", update_subcategories)

# Crear un combobox para las subcategorías
subcategory_label = ttk.Label(root, text="Subcategoría:", font=("Arial", 12))
subcategory_label.pack(pady=5)
subcategory_combobox = ttk.Combobox(root, font=("Arial", 12), state="readonly")
subcategory_combobox.set("Seleccionar Subcategoría")
subcategory_combobox.pack(pady=10)

# Entrada para nuevas categorías
new_category_label = ttk.Label(root, text="Nueva Categoría:", font=("Arial", 12))
new_category_label.pack(pady=5)
category_entry = ttk.Entry(root, width=50, font=("Arial", 12))
category_entry.pack(pady=10)

# Botón para añadir nuevas categorías
add_category_button = ttk.Button(root, text="Añadir Categoría", command=add_category)
add_category_button.pack(pady=5)

# Entrada para nuevas subcategorías
new_subcategory_label = ttk.Label(root, text="Nueva Subcategoría:", font=("Arial", 12))
new_subcategory_label.pack(pady=5)
subcategory_entry = ttk.Entry(root, width=50, font=("Arial", 12))
subcategory_entry.pack(pady=10)

# Botón para añadir nuevas subcategorías
add_subcategory_button = ttk.Button(
    root, text="Añadir Subcategoría", command=add_subcategory
)
add_subcategory_button.pack(pady=5)

# Crear botones para añadir y eliminar tareas
add_task_button = ttk.Button(root, text="Añadir Tarea", command=add_task)
add_task_button.pack(pady=5)

delete_task_button = ttk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_task_button.pack(pady=5)

# Cargar tareas al iniciar la aplicación
load_tasks()

# Crear botón para guardar tareas
save_task_button = ttk.Button(root, text="Guardar Tareas", command=save_tasks)
save_task_button.pack(pady=5)


# Ajustar el color de fondo de los widgets

task_listbox.configure(background="white", foreground="black")
task_label.configure(background="blue", foreground="white")
task_entry.configure(background="white", foreground="black")
category_label.configure(background="blue", foreground="white")
category_combobox.configure(background="blue", foreground="black")
subcategory_label.configure(background="blue", foreground="white")
subcategory_combobox.configure(background="blue", foreground="black")
new_category_label.configure(background="blue", foreground="white")
category_entry.configure(background="white", foreground="black")
new_subcategory_label.configure(background="blue", foreground="white")
subcategory_entry.configure(background="white", foreground="black")
add_category_button.configure(style="TButton")
add_subcategory_button.configure(style="TButton")
add_task_button.configure(style="TButton")
delete_task_button.configure(style="TButton")
save_task_button.configure(style="TButton")

# Crear un nuevo estilo para los botones
style.configure("TButton", background="white", foreground="black")

# Ejecutar el bucle principal
root.mainloop()
