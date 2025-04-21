# 🐦 Flappy Bird Clone using Pygame

This is a simple **Flappy Bird**-style game built using **Pygame**. The player controls a bird that must fly between incoming pillars without colliding. The score increases the longer you survive.

## 🚀 Features

- Pixel-perfect collision detection using masks
- Animated bird sprites
- Randomly colored and positioned pillars
- Scrolling ground and background
- Live score display
- Simple main menu screen

## 🎮 Controls

- `SPACE` - Make the bird jump (both to start the game and in-game)

## 🧠 How It Works

- The bird is animated and affected by gravity.
- Pressing space resets the upward velocity.
- Pillars spawn at intervals and scroll from right to left.
- Collision is detected using `pygame.mask` for accuracy.
- The ground and background scroll continuously for a parallax effect.
- Score is based on how long you survive.

## 📁 Assets

Make sure to include the following image files in the same directory:
- `bird1.png`, `bird2.png`, `bird3.png`
- `green_pillar.png`, `red_pillar.png`
- `background.jpg`, `ground.png`, `main_menu.png`
- `Pixeltype.ttf` (font file)

## 🛠️ Setup & Run

1. **Install Pygame** (if not already):
   ```bash
   pip install pygame
## 🧑‍💻 Author
Created by `Alex Dhami.`

Feel free to fork and modify!
