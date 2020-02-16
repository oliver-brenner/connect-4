# Connect 4 Project


---


### Project aims


- Implement the game of Connect 4 within a GUI
- Using a genetic algorithm, train an agent to act as an intelligent opponent within the game
- Serve the game in a manner that is playable by the public
- Create a productionised system which enables algorithm updates to be developed, tested and pushed remotely


---


### Progress


The game is currently playable via command line against an agent making decisions at random. The implementation is restricted to a game of 'connect-3' on a 4x4 grid.

The GUI is runnable, but only displays a board with no current game-functionality.


---


### Playing the game via command line:


1. Start running Python 3

2. Import the *classes.py* script:
```python
from classes import *
```

3. Initiate a session of the game:
```python
s = Session()
```

4. Complete moves by entering any of col1, col2, col3 or col4 in the following format:
```python
s.player.move(s, s.current_board, s.current_board.col1)
```


---


### Running the GUI


The GUI loop is initiated by calling the following module via command line:
```python
python play.py
```
