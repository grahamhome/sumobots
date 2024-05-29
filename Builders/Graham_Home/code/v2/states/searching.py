from .charging import Charging
from .rotating_away_edge import RotatingAwayEdge
from .state import State
from .targeting import Targeting


class Searching(State):
    """
    Robot is searching for an opponent.
    """

    def start(self):
        super().start()
        self.bot.drive(left_speed=-1, right_speed=1)

    def stop(self):
        super().stop()
        self.bot.stop()

    def opponent_detected(self):
        self.logger.debug("Opponent detected")
        self.switch(Targeting)


    def edge_detected(self):
        self.logger.debug("Edge detected")
        self.switch(RotatingAwayEdge)

