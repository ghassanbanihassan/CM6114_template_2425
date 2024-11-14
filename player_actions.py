"""
This file contains the functions related to the player's merchant ship.

Do not change the function definitions, only the function bodies. You may add
additional functions if you wish.
"""

# enter any imports you feel are relevant here
import setup_game


def get_user_direction():
    """
    This function should ask the user for a direction to move in
    ("N"/"E"/"S"/"W"), and return it.
    :return: The direction the user chose (a single character string).
    :rtype: string
    """

    # your code here for getting the user direction
    while True:
        direction = input("Enter your move, don't let the pirates catch you! (N = up'/north, E = right/east, S = down/south, W = left/west): ")

        if direction in{"N", "E", "S", "W"}:
            return direction
        else:
            print("Your boat can only move one space north, east, south or west each turn. Please enter the direction which you would like to move in.")

    # return the direction the user entered:


def get_new_player_position(player_position, direction, grid):
    """
    This function should calculate what will be the new position of the
    merchant ship, based on its current position and the direction the user
    chose. Note that this function shouldn't move the player, just work out
    where their new position will be (so you can use this new position to work
    out whether they will hit a rock, or the pirate etc).

    Note: most "human" coordinates read across (x axis) then up (y axis).
    Depending on how you created the grid, this may not always be the case when
    we access the 2D lists :-)

    Note2: You should handle the ship attempting to move off the edge of the
    grid. You can make the movement behave as if the grid is toroidal
    ('wraparound'), OR you can make the edges 'bounded' so the player cannot
    move off them. There's a question in the report about how you handle this.

    :param player_position: The player's current position
    :type player_position: tuple
    :param direction: The direction the player wants to move in (N/E/S/W)
    :type direction: string
    :param grid: The 2D game board
    :type grid: list
    :return: The player's updated position (tuple of two integers)
    :rtype: tuple
    """

    # your code to calculate the new position here

    x, y = player_position
    
    if direction == "N":
        new_x, new_y  = x - 1, y
        print("You Moved 1 space North!")
    elif direction == "E":
        new_x, new_y = x, y + 1
        print("You Moved 1 space East!")
    elif direction == "S":
        new_x, new_y = x + 1, y
        print("You Moved 1 space South!")
    elif direction == "W":
        new_x, new_y = x, y - 1
        print("You Moved 1 space West!")

    if 0 <= new_x < 11 and 0 <= new_y < 11:
        return (new_x, new_y) 
    else:
        print("That's out of bounds!")
        return player_position #returns original position if the new position is out of bounds


    # you should finish off this function with a return statement returning the
    # merchant ship's proposed new position


def move_player(grid, old_player_position, new_player_position):
    """
    This function should move the player; it can be done simply by removing "M"
    from the old position and putting it in the new position.

    The function doesn't need to return anything, as the grid can be updated
    "in place", but you can return the grid or anything else you need if
    you like.

    :param grid: The 2D gameboard
    :type grid: list
    :param old_player_position: the player's current position (two integers)
    :type old_player_position: tuple
    :param new_player_position: the new player position (tuple of 2 integers)
    :type new_player_position: tuple
    :return:
    """

    # your code to move the player here
    x, y = old_player_position
    new_x, new_y = new_player_position 
    grid[x][y] = ". "
    grid[new_x][new_y] = "M "
    return grid

def kill_player(grid, old_player_position, new_player_position):
    """
    This function should 'kill' the player; it's actually very similar to
    moving the player: it can be done simply by removing "M" from the old
    position and putting "X" in the new position.

    The function doesn't need to return anything, as the grid can be updated
    "in place", but you can return the grid or anything else you need if
    you like.

    :param grid: The 2D gameboard
    :type grid: list
    :param old_player_position: the player's current position
    :type old_player_position: tuple
    :param new_player_position: the new player position
    :param new_player_position: tuple
    :return:
    """

    # your code to kill the player here
    x, y = new_player_position 
    grid[x][y] = "X "
    print("Game over!")
    return grid