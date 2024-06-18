from states import State


class Searching(State):
    """
    Robot is searching for an opponent.
    """

    async def start(self):
        super().start()
        self.bot.drive(left_speed=-1, right_speed=1)

    async def stop(self):
        await super().stop()
        self.bot.stop()

    async def opponent_detected(self):
        self.logger.debug("Opponent detected")
        from states import Targeting
        self.switch(Targeting)


    async def edge_detected(self):
        self.logger.debug("Edge detected")
        from states import RotatingAwayEdge
        self.switch(RotatingAwayEdge)

