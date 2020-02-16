# Connect 4 Project

---

### Project aims

- Implement the Connect 4 game within a GUI
- Use a genetic algorithm to train an agent which can act as an opponent
- Serve the game in a manner that is playable by the public
- Productionise the system such that algorithm updates can developed, tested and pushed remotely

---

### Progress

The game is currently playable via command line against an agent making decisions at random. The implementation is restricted to a game of 'connect-3' on a 4x4 grid.

The GUI is runnable, but only displays a board with no current game-functionality.

---

### Playing the game via command line:

1. Run Python 3

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
