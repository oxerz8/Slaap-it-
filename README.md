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
#Directory Structure:
The code is designed and structed around MVC design pattern, and we made some changes on it.

### Contributors:
Sidharth
Lingxiao Liu
Anusha
Pushti
Ash
### License:

Built under GNU General Public License

You can find a copy of the License at https://github.com/oxerz8/Slaap-it-/blob/master/LICENSE
