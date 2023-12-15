#!/usr/bin/env python3
#2023-12-12

import sys

"""
Advent Of Code, Day 2:

Determine which games would have been possible if the bag had been loaded with only
12 red cubes
13 green cubes
14 blue cubes

What is the sum of the IDs of those games?
"""


def read_input(file):
    """
    Read the file with the game information.
    Arguments:
    file -- Path location of the file 
    """

    file = open(file, 'r')
    for line in file.readlines():
        format_line(line.strip())


def format_line(line):
    """
    Format the line to get the variables.
    Arguments:
    line -- Argument provided automatically by read_input function.
    """
    
    line_text = line.split(':')
    game_string = line_text[0].split()
    game_id = game_string[1]
    game_results = line_text[1].split(';')
    check_game(int(game_id), game_results)
    print(LIST_OF_POSSIBLE_GAMES)


def check_game(game_id, game_results):
    """
    Check game values.
    Param -- Check current game values
    """
    
    break_main_loop = False
    for game in game_results:
        if break_main_loop == True:
            break
        else:
            for single_game in game.split(','):
                game_value = single_game.split()
                cube_number = int(game_value[0])
                cube_color = game_value[1]
                result = game_is_possible(cube_color, cube_number)
                if result == False:
                    print('game {0} could not be possible'.format(game_id))
                    break_main_loop = True
                    break
                if result == True:
                    if game_id in LIST_OF_POSSIBLE_GAMES:
                        pass
                    else:
                        LIST_OF_POSSIBLE_GAMES.append(game_id)
def game_is_possible(color, number):
    possible_games = {
        'red' : 12,
        'green' : 13,
        'blue' : 14,
    }

    if color in possible_games.keys():
        if number > possible_games[color]:
            return False
        else:
            return True


LIST_OF_POSSIBLE_GAMES = []

if __name__ == '__main__':
    try:
        file = sys.argv[1]
        read_input(file)
    except IndexError:
        print('Please provide the path of the input file')