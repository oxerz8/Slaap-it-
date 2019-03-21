# Slaap it!
The classic retro game Pong recreated using Pygame and python

## Index

### Screenshots:

![alt text](https://github.com/oxerz8/Slaap-it-/blob/master/Screenshots/Screenshot%20from%202019-03-21%2018-07-04.png)

![alt text](https://github.com/oxerz8/Slaap-it-/blob/master/Screenshots/Screenshot%20from%202019-03-19%2013-23-58.png)

### Game features:
- The start screen contains Single Player, Two Player and Quit Game buttons.
    - Click on the Single Player button to start playing the single player mode.
    - Click on the Two Player button to start playing the two player mode.
    - Click on the Quit Game to close the game screen(In this case, you cannot use "x" to close the screen).
- The main game screen contain a 500x500 screen where the actual game will take place.
    - The players need to use their own paddle to make collision with the flying ball.
    - If the ball flys through either left or right edge, the another player would get one point.
    - The game would keep running until the players click "x" on the top right corner.

### Controls:
|Button|Action|
|------|------|
|Down key|Player 2 moves down|
|Up key|Player 2 moves up|
|W key|Player 1 moves up|
|S key|Player 1 moves down|

### Installation:
#### For Windows:
Download the executable file and run it

#### For Linux:
Python3 and pygame module are required to run this game.

To install python3, run the following command:
```
sudo apt-get update
sudo apt-get install python3
```

To install pygame module run the follwing command:
```
sudo apt-get install python-pygame
```

Clone the repo and run python
```
git clone https://github.com/oxerz8/Slaap-it-
cd Slaap-it-/
python3 view.py
```

## Project Directory and Code Structure:
### Directory Structure
All the code related to the game can be found in the main directory ```Slaap-it-/```. The code is designed using Model View Controller design and Strategy design pattern. This is done in order to expand the code if required and improves the clarity of the working of the game.

### Code Structure

- The file view.py contains the main loop which initializes and updates the game screen. It is also the View component of the MVC pattern.

- The file controller.py contains the Controller component of the MVC pattern. It is responsible for sending all the data related to user input, paddle and ball initiation and game modes.

- The files ball.py, user.py and paddle.py are the Model component of the MVC pattern and are responsible for initializing the ball, the user(s) and the paddle(s) for the game. Furthermore, user.py is a parent class for computer_player.py and computer_player.py and is designed around the Strategy design pattern.

- The game is designed so that additional features are straightforward to add. 

For example: 

To add a new button "x_button" to the main menu, simply open view.py and add the following:
```
menu_options = ["Single  Player", "  Two Player", "  Quit Game", "x_button"]
button_x = pygame.draw.rect(window, (2,5,100), (150, 310, 200, 50))
```

### Contributors:
- Sidharth Khurana

- Lingxiao Liu

- Anusha Pahore

- Pushti Gandhi

- Ashir

### License:

Built under GNU General Public License

You can find a copy of the License at https://github.com/oxerz8/Slaap-it-/blob/master/LICENSE
