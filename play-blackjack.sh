#!/usr/bin/env bash

# this script calls setup.sh and initiates the game for the user (calls main.py)

# This script will check whether the user has the correct ".game-mode-venv" in their current working directory,
# check whether they are in the game directory "simple-blackjack-game", and attempt to activate the venv. If
# the user does not have said venv, it will source the setup script, which will create it and activate it. The 
# script will then check whether the venv is active (in path) and run the game (call main.py). Note that there 
# are not currently any requirements in "requirements.txt", so this is not strictly necessary, but has been done
# as a formality in the case that requirements are added later. 
# - KlintonJ 04 December 2024

correctdir=$(pwd | grep "simple-blackjack-game")
inpath=$(echo $PATH | grep ".game-mode-venv")

if [ -e ".game-mode-venv" ] && [[ $correctdir != "" ]]; then
	source .game-mode-venv/bin/activate

	if [[ $inpath != "" ]]; then
		python3 main.py
	else
		source .game-mode-venv/bin/activate
		python3 main.py
	fi
else
	source ./utils/setup.sh

	if [[ $inpath != "" ]]; then
		python3 main.py
	else
		source .game-mode-venv/bin/activate
		python3 main.py
	fi
fi

deactivate
clear
