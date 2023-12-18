# 📝 Description

Simple TicTacToe game class

# Prerequisites

- [`Python`](https://www.python.org/downloads/release/python-3117) 3.11.7
- [`Poetry`](https://python-poetry.org/docs/#installation) >=1.7.1

# 🧰 Installation

```bash
poetry install
```

## ⚙ Using Game class

```py
game = Game()

# adding a move
game.addMove((0, 0))

# checking if game is already over
game.gameover()

# getting next move shape("x" or "o")
game.getNextMoveShape()

# checking if game has minimum moves to have a winner
game.hasMinimumMovesToHaveWinner()

# check if move is free
game.isFreeMove((0, 0))

# check if move is valid, it will validate range [0, 2]
game.isValidMove((0, 0))

# check if move did win based in move coordinate, it will check row, column, diagonal or secondary diagonal
game.moveDidWin((0, 0))

# getting result
# Starts equals None, but when calling the addMove method and if there is a winner or draw, the variable will be rewritten
game.result
```

## 🧪 Running tests

```bash
poetry run python -m pytest ./tests/
```

With code coverage

```bash
poetry run python -m pytest --cov=src --cov-report html ./tests/
```

# ✅ TODO

- add way to test all moves
- add mypy

# 👷 Authors

- [**lucasmonstrox**](http://github.com/lucasmonstrox)([**linkedin**](https://www.linkedin.com/in/lucasmonstrox/)) - Developer

See also the list of [contributors](../../graphs/contributors) who participated
in this project.

# ❤️ Development inspiration

I was bored with nothing to do, so I created the game tictactoe to play against my friend RealGalego.

# 📝 License

Copyright © 2023 [**lucasmonstrox**](https://github.com/lucasmonstrox)  
This project is [MIT](https://opensource.org/licenses/MIT) licensed
