"""
Module Name: game_stats.py
Author: Kishan Atada
Course: CSCI 1511
Date: July 15, 2026

Purpose:
This module stores game status information, such as how many ships
the player has left during the game.
"""

class GameStats():

    """Track game statistics for Alien Invasion."""
    def __init__(self, ship_limit):
        """Initialize the number of ships the player has left."""
        self.ships_left = ship_limit
