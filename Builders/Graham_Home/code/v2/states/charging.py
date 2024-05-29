from .grappling import Grappling
from .rotating_away_edge import RotatingAwayEdge
from .searching import Searching
from .state import State
from .targeting import Targeting


class Charging(State):
    """
    Robot is charging the opponent.
    """
    async def start(self):
        await super().start()
        await self.bot.drive(right_speed=1, left_speed=1)

    def stop(self):
        super().stop()
        self.bot.stop()

    # TODO: Consider changing direction slightly when opponent detected left/right
    #  (will need to maintain state of L & R motor speeds to adjust)

    def opponent_detected(self):
        self.logger.debug("Opponent detected")
        if self.bot.opponent_in_range_left() and self.bot.opponent_in_range_right():
            if self.bot.contacting_opponent_left() or self.bot.contacting_opponent_right():
                self.switch(Grappling)
        elif self.bot.opponent_in_range_left() or self.bot.opponent_in_range_left():
            self.switch(Targeting)
        else:
            self.switch(Searching)
        
    def edge_detected(self):
        self.logger.debug("Edge detected")
        self.switch(RotatingAwayEdge)
