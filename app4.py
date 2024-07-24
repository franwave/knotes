import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
import math
import random

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

# Función para abrir el juego de Snake
def open_snake_game():
    snake_window = tk.Toplevel(root)
    snake_window.title("Snake")
    snake_window.geometry("400x400")
    snake_window.configure(bg='blue')

    # Configuración del juego
    game_width = 400
    game_height = 400
    snake_color = "green"
    food_color = "red"
    background_color = "black"
    cell_size = 20
    score = 0

    # Variables del juego
    direction = "right"
    snake_parts = [(0, 0), (20, 0), (40, 0)]
    food_position = (random.randint(0, (game_width // cell_size) - 1) * cell_size,
                     random.randint(0, (game_height // cell_size) - 1) * cell_size)

    def move_snake():
        nonlocal direction, food_position, snake_parts, score
        head_x, head_y = snake_parts[-1]
        if direction == "up":
            new_head = (head_x, head_y - cell_size)
        elif direction == "down":
            new_head = (head_x, head_y + cell_size)
        elif direction == "left":
            new_head = (head_x - cell_size, head_y)
        elif direction == "right":
            new_head = (head_x + cell_size, head_y)
        else:
            new_head = (head_x, head_y)

        if (new_head in snake_parts or
            new_head[0] < 0 or new_head[0] >= game_width or
            new_head[1] < 0 or new_head[1] >= game_height):
            game_over()
            return

        snake_parts.append(new_head)

        if new_head == food_position:
            score += 1
            score_label.config(text=f"Puntaje: {score}")
            food_position = (random.randint(0, (game_width // cell_size) - 1) * cell_size,
                             random.randint(0, (game_height // cell_size) - 1) * cell_size)
        else:
            snake_parts.pop(0)

        draw_snake()

    def draw_snake():
        canvas.delete("all")
        for part in snake_parts:
            canvas.create_rectangle(part[0], part[1], part[0] + cell_size, part[1] + cell_size, fill=snake_color)
        canvas.create_rectangle(food_position[0], food_position[1], food_position[0] + cell_size, food_position[1] + cell_size, fill=food_color)
        snake_window.after(100, move_snake)

    def change_direction(new_direction):
        nonlocal direction
        directions = ["up", "down", "left", "right"]
        if (new_direction == "up" and direction != "down") or \
           (new_direction == "down" and direction != "up") or \
           (new_direction == "left" and direction != "right") or \
           (new_direction == "right" and direction != "left"):
            direction = new_direction

    def game_over():
        canvas.delete("all")
        canvas.create_text(game_width // 2, game_height // 2, text=f"Game Over\nPuntaje: {score}", fill="white", font=("Arial", 24))
        canvas.update()

    def key_pressed(event):
        if event.keysym == "Up":
            change_direction("up")
        elif event.keysym == "Down":
            change_direction("down")
        elif event.keysym == "Left":
            change_direction("left")
        elif event.keysym == "Right":
            change_direction("right")

    canvas = tk.Canvas(snake_window, width=game_width, height=game_height, bg=background_color)
    canvas.pack()
    
    score_label = tk.Label(snake_window, text=f"Puntaje: {score}", font=("Arial", 12), bg='blue', fg='white')
    score_label.pack(pady=10)
    
    snake_window.bind("<KeyPress>", key_pressed)
    snake_window.focus_set()

    move_snake()

# Función para abrir el juego de Pong
def open_pong_game():
    pong_window = tk.Toplevel(root)
    pong_window.title("Pong")
    pong_window.geometry("600x400")
    pong_window.configure(bg='blue')

    # Configuración del juego
    paddle_width = 10
    paddle_height = 100
    ball_radius = 10
    paddle_color = "white"
    ball_color = "white"
    background_color = "black"

    # Variables del juego
    paddle1_pos = [10, 150]
    paddle2_pos = [580, 150]
    ball_pos = [300, 200]
    ball_speed = [4, 4]
    score1 = 0
    score2 = 0

    def move_ball():
        nonlocal ball_pos, ball_speed, score1, score2
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        if ball_pos[1] <= 0 or ball_pos[1] >= 400 - ball_radius:
            ball_speed[1] = -ball_speed[1]

        if ball_pos[0] <= paddle1_pos[0] + paddle_width and paddle1_pos[1] <= ball_pos[1] <= paddle1_pos[1] + paddle_height:
            ball_speed[0] = -ball_speed[0]
            ball_speed[0] *= 1.1
            ball_speed[1] *= 1.1
        elif ball_pos[0] >= paddle2_pos[0] - paddle_width and paddle2_pos[1] <= ball_pos[1] <= paddle2_pos[1] + paddle_height:
            ball_speed[0] = -ball_speed[0]
            ball_speed[0] *= 1.1
            ball_speed[1] *= 1.1
        elif ball_pos[0] < 0:
            score2 += 1
            update_scores()
            reset_ball()
        elif ball_pos[0] > 600:
            score1 += 1
            update_scores()
            reset_ball()

        move_paddle2()
        draw_pong()

    def draw_pong():
        canvas.delete("all")
        canvas.create_rectangle(paddle1_pos[0], paddle1_pos[1], paddle1_pos[0] + paddle_width, paddle1_pos[1] + paddle_height, fill=paddle_color)
        canvas.create_rectangle(paddle2_pos[0], paddle2_pos[1], paddle2_pos[0] + paddle_width, paddle2_pos[1] + paddle_height, fill=paddle_color)
        canvas.create_oval(ball_pos[0] - ball_radius, ball_pos[1] - ball_radius, ball_pos[0] + ball_radius, ball_pos[1] + ball_radius, fill=ball_color)
        pong_window.after(20, move_ball)

    def move_paddle1(event):
        if event.keysym == "w" and paddle1_pos[1] > 0:
            paddle1_pos[1] -= 20
        elif event.keysym == "s" and paddle1_pos[1] < 300:
            paddle1_pos[1] += 20

    def move_paddle2():
        if ball_pos[1] < paddle2_pos[1] + paddle_height / 2 and paddle2_pos[1] > 0:
            paddle2_pos[1] -= 20
        elif ball_pos[1] > paddle2_pos[1] + paddle_height / 2 and paddle2_pos[1] < 300:
            paddle2_pos[1] += 20

    def update_scores():
        score_label.config(text=f"Jugador 1: {score1}  Jugador 2: {score2}")

    def reset_ball():
        nonlocal ball_pos, ball_speed
        ball_pos = [300, 200]
        ball_speed = [4, 4]

    canvas = tk.Canvas(pong_window, width=600, height=400, bg=background_color)
    canvas.pack()

    score_label = tk.Label(pong_window, text=f"Jugador 1: {score1}  Jugador 2: {score2}", font=("Arial", 16), bg='blue', fg='white')
    score_label.pack(pady=10)

    pong_window.bind("w", move_paddle1)
    pong_window.bind("s", move_paddle1)
    pong_window.bind("<Up>", move_paddle1)
    pong_window.bind("<Down>", move_paddle1)

    move_ball()

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

games_button = tk.Button(center_frame, text="Juegos", font=("Arial", 16), width=20, command=lambda: open_games_menu(center_frame))
games_button.pack(pady=10)

exit_button = tk.Button(center_frame, text="Salir", font=("Arial", 16), width=20, command=exit_app)
exit_button.pack(pady=10)

# Función para abrir el menú de juegos
def open_games_menu(center_frame):
    for widget in center_frame.winfo_children():
        widget.destroy()

    snake_button = tk.Button(center_frame, text="Snake", font=("Arial", 16), width=20, command=open_snake_game)
    snake_button.pack(pady=10)

    pong_button = tk.Button(center_frame, text="Pong", font=("Arial", 16), width=20, command=open_pong_game)
    pong_button.pack(pady=10)

    back_button = tk.Button(center_frame, text="Volver", font=("Arial", 16), width=20, command=lambda: back_to_main_menu(center_frame))
    back_button.pack(pady=10)

# Función para volver al menú principal
def back_to_main_menu(center_frame):
    for widget in center_frame.winfo_children():
        widget.destroy()

    task_manager_button = tk.Button(center_frame, text="Gestión de Tareas", font=("Arial", 16), width=20, command=open_task_manager)
    task_manager_button.pack(pady=10)

    calculator_button = tk.Button(center_frame, text="Calculadora", font=("Arial", 16), width=20, command=open_calculator)
    calculator_button.pack(pady=10)

    games_button = tk.Button(center_frame, text="Juegos", font=("Arial", 16), width=20, command=lambda: open_games_menu(center_frame))
    games_button.pack(pady=10)

    exit_button = tk.Button(center_frame, text="Salir", font=("Arial", 16), width=20, command=exit_app)
    exit_button.pack(pady=10)

# Ejecutar el bucle principal
root.mainloop()
