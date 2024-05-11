from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import RandomComputerPlayer
from tic_tac_toe.logic.models import Mark

from console.players import ConsolePlayer
from console.renderers import ConsoleRenderer

player1 = ConsolePlayer(Mark("X"))
player2 = RandomComputerPlayer(Mark("O"))

TicTacToe(player1, player2, ConsoleRenderer()).play()

"""  to play the game, run the program and type the location for your piece
There are 3 types of players: 1-human, 2-random, 3-minimax
to change the settings: 
cd frontends
python -m console -X minimax -0 minimax
change the X and 0 to the type of player you would like and have fun!  """