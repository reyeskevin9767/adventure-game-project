import world
from player import Player
from termcolor import colored
from colorama import init
init()

def play():
    world.load_tiles()
    player = Player()
    # Load the starting room and display the text
    room = world.tile_exists(player.location_x, player.location_y)
    print(colored(room.intro_text(), color="green"))
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check the player's state after each room
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(colored(action, color="blue"))
            action_input = input('\nAction: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break


if __name__ == "__main__":
    play()
