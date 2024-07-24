# notikodland
A GUI made with Tkinter, capable of taking notes and calculate mathematical operations. If you get bored, you can play either the snake or pong game.


## Running the Application

To run the application, follow these steps:

1. **Windows**:
   - Locate the `KNOTES.exe` file in the `dist` directory.
   - Double-click the executable to run the application.

2. **macOS and Linux**:
   - Locate the `KNOTES` file in the `dist` directory.
   - Open a terminal and navigate to the `dist` directory.
   - Run the executable using the following command:
     ```bash
     ./KNOTES
     ```

No additional software is required to run the application.


The main program is divided into several functions and sections to manage different features of the application, such as task management, a calculator, and games (Snake and Pong). 
Below is a summary of the code structure:

#Main Functions

#Main Menu:
open_task_manager(): Opens the task management window.
open_calculator(): Opens the calculator window.
open_games_menu(center_frame): Opens the games submenu.
back_to_main_menu(center_frame): Returns to the main menu.
exit_app(): Closes the application.

#Task Management:
add_task(task_entry, task_listbox): Adds a new task to the list.
delete_task(task_listbox): Deletes the selected task from the list.
load_tasks(task_listbox): Loads saved tasks when the application starts.
save_tasks(task_listbox): Saves tasks to a text file.

#Calculator:
add_to_expression(symbol): Adds a symbol to the expression.
add_function(func): Adds a mathematical function to the expression.
evaluate_expression(): Evaluates the mathematical expression.
clear_expression(): Clears the current expression.
Games:

#Snake:
open_snake_game(): Opens the Snake game.
move_snake(): Moves the snake and checks for collisions.
draw_snake(): Draws the snake and the food.
change_direction(new_direction): Changes the snake's direction.
game_over(): Handles the game over scenario.
key_pressed(event): Detects key presses to move the snake.


#Pong:
open_pong_game(): Opens the Pong game.
move_ball(): Moves the ball and checks for collisions.
draw_pong(): Draws the ball and paddles.
move_paddle1(event): Moves the player 1 paddle.
move_paddle2(): Moves the player 2 paddle (AI).
update_scores(): Updates the score display.
reset_ball(): Resets the ball position.

#Main Window Configuration
The main window root is created with a frame center_frame to center the buttons.
Buttons are defined to open different sections of the application:
Task Management
Calculator
Games
Exit

#Main Loop Execution
root.mainloop(): Executes the main loop of the graphical user interface.
