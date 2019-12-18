from game_state import GameState


def switch_player(state: GameState):
    if state.player == 'Player 1':
        state.set_player('Player 2')
        state.set_weapon('O')
    else:
        state.set_player('Player 1')
        state.set_weapon('X')


def is_over(tiles: list):
    pass
