## Project description for certification
          Cristina Bodea


What my project does:

This is a classic Snake game implemented in Python using the Turtle module for graphics. The game offers a graphical interface in which the player controls a snake that moves around the screen.
The object of the game is to eat food and increase the length of the snake without colliding with walls or your own body.
The code consists of three classes: Snake, Food, and Scoreboard.
The Snake class represents the snake in the game. It has methods for creating the snake, adding segments to the snake, expanding the snake, moving the snake, and changing its direction. The snake is composed of individual segments.
The Food class represents the food that the snake must eat. It is a subclass of Turtle and has a method to randomly refresh its position on the screen.
The Scoreboard class manages the game score and displays it on the screen. It has methods for updating the scoreboard, displaying the game over message and increasing the score.



Characteristics:
- The game allows the player to control the movement of the snake using the arrow keys: Up, Down, Left, Right.
- The snake grows in length every time it eats food.
- The game ends if the snake collides with the walls or with its own body.
- The player's score is displayed on the screen, increasing each time the snake eats food.
- The game over screen shows the final score.

Installation:
1. Clone the repository https://github.com/Cristinaa90/Snake_game.git
2. To run this code, you must have the Turtle module installed. You can run the code in a Python environment that supports the Turtle module, such as IDLE or PyCharm.
3. Run the main.py script
4. The game window will open and you can start playing the Snake game.

How to play:
- Use the arrow keys (Up, Down, Left, Right) to control the snake's movement.
- The snake will move continuously in the direction in which it was guided.
- Every time the snake eats it will grow in length.
- Avoid collision with the walls or with the snake's own body.
- The game ends when the snake collides with a wall or with its own body.
- The final score will be displayed on the screen together with the message 'Game over'.
