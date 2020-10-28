# Retro_Game

This file would write some running instructions, including dependencies that might need to be installed.

In this project, we implemented Tetris Game with a simple AI to play the game. Users can choose which mode they want to play.

This project is based on Python3. And need PyQt5 and Numpy.

* `Tetris.py` is the main implementation of Tetris.
* `model.py` is the data model for this game.
* `AI_agent.py` is the AI part.
* `utils.py` includes some helpful functions and classes.
* `main.py` is the game implementation, combining other parts.
* `run.py` generates the starting UI, with some choices before starting the game.

Run `run.py` in terminal and you can play or watch AI.

```shell
$ python3 run.py
```

You also can adjust the speed of this game. You can type it like:

```shell
$ python3 run.py --value_of_speed = 200
```

Bigger number would have slower speed. And the default speed is '300'.

### Rule of Tetris

*up* key would rotate the block. *left* key and *right* key would control the moving direction. *space* key would let the block arrive the bottom straightly. *P* key can cease the game temporarily.
