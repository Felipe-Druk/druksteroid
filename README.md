# Asteroids - Python Game

A classic Asteroids arcade game built with Python and Pygme. Navigate your ship through an asteroid field, shoot rocks, and survive as long as possible!

## Prerequisites

- Python 3.13 or higher
- uv (Python package manager)

## Installation

1. Clone the repository
2. Install dependencies:

```bash
uv install
```

## Running the Game

```bash
uv run main.py
```

## Controls

- **Arrow Keys** - Rotate the ship
- **Spacebar** - Fire shots
- **Movement** - Ship moves forward in the direction it's facing

## Features

- Smooth ship rotation and movement
- Asteroid splitting mechanics (large asteroids break into smaller ones)
- Collision detection between ship, asteroids, and shots
- Reset by keys "back" and "q"
- chose color from sprites

## Future Enhancement Ideas

- Add a scoring system
- Implement multiple lives and respawning
- Add an explosion effect for the asteroids
- Add acceleration to the player movement
- Make the objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Make the ship have a triangular hit box instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped

## Project Structure

- `main.py` - Game entry point and main loop
- `constants.py` - Game constants and configuration
- `logger.py` - Event and state logging utility
- `color.py` - Personal colors
- `menu_druksteroid.py` - Menu base for the game
- `sprites` - Directory from sprites
    - `player.py` - Player ship class
    - `asteroid.py` - Asteroid class with splitting mechanics
    - `asteroidfield.py` - Asteroid field manager
    - `circleshape.py` - Base class for circular game objects
    - `shot.py` - Bullet/shot class



---

## Acknowledgments

Thank you to [Boot.dev](https://www.boot.dev/courses/build-asteroids-python) for the excellent Python course that guided the development of this project!
