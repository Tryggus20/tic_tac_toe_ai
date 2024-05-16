"""  TO PLAY THE GAME:
There are 3 types of players: 1-human, 2-random, 3-minimax
to change the settings, run: 
cd frontends
python -m console -X minimax -O minimax
change the X and 0 to the type of player you would like and have fun! 
ps: manual entry moves accepts both a1 and 1a formats"""

# tutorial I followed:
# https://realpython.com/tic-tac-toe-ai-python/#step-2-scaffold-a-generic-tic-tac-toe-game-engine

from tic_tac_toe.game.engine import TicTacToe
from tic_tac_toe.game.players import RandomComputerPlayer
from tic_tac_toe.logic.models import Mark

from console.players import ConsolePlayer
from console.renderers import ConsoleRenderer

player1 = ConsolePlayer(Mark("X"))
player2 = RandomComputerPlayer(Mark("O"))

TicTacToe(player1, player2, ConsoleRenderer()).play()
