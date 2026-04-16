## riskai

An implementation of Risk II (2000) built for easy ML training. All a user has to do is implement a player and start the game.

### Installation

This uses pyproject.toml so installation with pip is fairly easy.

```
pip install git+https://github.com/lewhfree/riskai
```

### Usage

This documentation will not move as fast as things change so it may not be up to date. The best documentation is just to look at the implementation in the repo. 

To use this, you must implement a [class](src/riskai/players/player_class.py) that takes in an [observation](src/riskai/messages.py) (only info that matters and only info the player should have access to) and returns a [response](src/riskai/messages.py).

Hopefully there will be some simple bots later, but for now the only example implementation is the [cli player](src/riskai/players/console_player_class.py).
