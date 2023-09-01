Based on the requirements, we can identify the following core classes, functions, and methods for the snake game:

1. `Game`: Responsible for managing the game state, including the game board, snake, and food.
   - `start()`: Starts the game loop.
   - `update()`: Updates the game state on each iteration of the game loop.
   - `draw()`: Renders the game board and entities on the screen.
   - `handle_input()`: Handles user input for controlling the snake.
   - `check_collision()`: Checks for collisions between the snake and the food or game boundaries.
   - `game_over()`: Handles the game over condition.

2. `Snake`: Represents the snake entity in the game.
   - `move()`: Moves the snake in the specified direction.
   - `grow()`: Increases the length of the snake when it eats food.
   - `check_self_collision()`: Checks for collisions between the snake's head and its body.

3. `Food`: Represents the food entity in the game.
   - `generate()`: Generates a new food item at a random position on the game board.

Now, let's proceed with implementing the code for each file.

**game.py**
