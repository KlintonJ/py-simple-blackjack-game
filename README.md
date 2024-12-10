# Intro
Hi! :)

This is the first project in a series of projects dedicated to exploring features and conventions of the Python, C++,
C, and Zig programming languages and the development experience while using them. The code itself if inspired by a 
**Beau Carnes** video, which is linked in the NOTES below. This is also a translation series in many ways, as the base
functionality across all implementations is the same. Nonetheless, this is the version built in Python, and the 
instructions that follow are for the Python version only.
(**note that the following instructions are currently Linux and macOS specific**) 

# Installation 
## Linux and macOS users:  
- enter your preferred terminal emulator
- if using ssh:
    - enter the command: `git clone -b main --single-branch git@github.com:KlintonJ/py-simple-blackjack-game.git`
- if using https:
    - enter the command: `git clone -b main --single-branch 'https://github.com/KlintonJ/py-simple-blackjack-game.git'`
- NOTE: default to cloning the repo in your home directory. Feel free to clone it elsewhere if you know what you're doing :)

# Starting the Game 
- to play the game, first enter the game directory: `cd ~/py-simple-blackjack-game`
- then enter the command: `source play-blackjack.sh` (`source ./play-blackjack.sh` will also work, if you like to be specific)
- if you have not sourced the script before, this will source the `setup.sh` script, which will do the following:
    - create the `.game-mode-venv` with python3's venv module
    - activate said venv
- if you have sourced it before OR once `setup.sh` is finished, it will activate the venv and run `main.py` with python3

# Playing the Game 
- a menu will pop up asking what you would like to do 
    - enter `1` if you would like to play Blackjack or `2` if you would like to exit the game 
- if you chose 1, a menu will appear asking how many games you would like to play 
    - enter any number greater than 0 for this 
- the game will issue 2 cards to you and the dealer
- it will display your hand and its value, and the last card of the dealer's hand
- you will be prompted to enter Hit/Stand
    - enter `Hit`/`H`/`h` to get another card from the deck OR `Stand`/`S`/`s` to keep your current hand
- between each Hit/Stand it will show you the current composition and value of your hand
- at the end of each game a menu will appear asking if you are ready for the next game 
    - enter `1` if you'd like to go to the next game OR `2` if you'd like to exit the game 

# NOTES:
- the code and README are subject to change
- I will likely add Windows support/instructions, but there is currently no timeframe on this
- **Beau Carnes links**
    - YouTube video: https://www.youtube.com/watch?v=aryte85bt_M
    - replit for his project in the video: https://replit.com/@BeauCarnes/blackjack-python#main.py
    - YouTube Channel: https://www.youtube.com/@beau 
