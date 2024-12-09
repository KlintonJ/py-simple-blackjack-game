#!/usr/bin/env bash

# This script is intended to be sourced by "play-blackjack.sh". It will check whether the python3 command exists
# (usually: /bin/python3 OR /usr/bin/python3 exists) and redirects stdout and stderr output to "/dev/null". If 
# it does, it will check that the user's current dir is the game directory ("simple-blackjack-game") and that 
# "requirements.txt" exists. If both are true, it will create the necessary ".game-mode-venv", activate it, and 
# pip install the requirements listed in "requirements.txt". If one of them is false, it will let the user know 
# their current working dir and give instruction on how to find the game dir ("requirements.txt" will always
# exist in the game dir if it is required). In the case that the original conditional is false (python3 command
# does NOT exist), it will let the user know that Python 3 or greater is required.
# - KlintonJ 04 December 2024

echo "setting up your game of Blackjack :) ..."

if command -v python3 &>/dev/null; then
	correctdir=$(pwd | grep "simple-blackjack-game")

	if [ -e "requirements.txt" ] && [[ $correctdir != "" ]]; then
		python3 -m venv .game-mode-venv
		source .game-mode-venv/bin/activate
		python3 -m pip install -r requirements.txt &>/dev/null
	else
		currentdir = $(pwd)
		echo "current dir is $currentdir "
		echo "cd to the dir you downloaded the game into and locate the 'simple-blackjack-game' dir and cd into it, then try running this again..."
	fi

else 
	echo "Python version must be 3 or newer."
	echo "Consider upgrading or setting up a venv, then retry this..."
fi
