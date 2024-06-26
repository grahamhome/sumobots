from states import State


class Searching(State):
    """
    Robot is searching for an opponent.
    """

    async def start(self):
        await super().start()
        await self.bot.drive(left_speed=-0.5, right_speed=0.5)

    async def stop(self):
        self.logger.info("Searching is stopping")
        await super().stop()
        await self.bot.stop()

    async def opponent_detected(self):
        self.logger.debug("Opponent detected")
        from states import Targeting
        await self.switch(Targeting)


    async def edge_detected(self):
        from states import RotatingAwayEdge
        await self.switch(RotatingAwayEdge)

