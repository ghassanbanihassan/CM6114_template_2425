import setup_game
import player_actions
import enemy_actions

# add any other imports you feel are relevant here

if __name__ == "__main__":
    # this is where the code should go that runs the game.
    # you can leave the following line in or take it out, up to you:
    print("PIRATES!")

grid_size = 10
print("-------------------")
grid = setup_game.create_grid(grid_size)
setup_game.print_grid(grid)
print("-------------------")
difficulty = int(input("choose a difficulty from 1 to 10, with 1 being the hardest. "))
print("-------------------")
setup_game.add_rocks(grid, difficulty)
grid, player_position = setup_game.place_player(grid)
grid, enemy_position = setup_game.place_enemy(grid)
setup_game.print_grid(grid)
print("-------------------")
print(player_position)
print("-------------------")

direction = player_actions.get_user_direction()
new_player_position = player_actions.get_new_player_position(player_position, direction, grid)
player_actions.move_player(grid, player_position, new_player_position)
setup_game.print_grid(grid)
print(new_player_position)


new_enemy_position = enemy_actions.get_new_enemy_position(enemy_position, player_position)



                                                    #Lines 38 to 41 i had help from the internet since new_enemy_position was stuck in this form -->  (np.int64(7), np.int64(4))
def to_python_int_tuple(np_tuple):                  ##
                                                    ##
    return (int(np_tuple[0]), int(np_tuple[1]))     ##
                                                
NEP = to_python_int_tuple(new_enemy_position)
print(NEP)

enemy_actions.move_enemy(grid, enemy_position, NEP)