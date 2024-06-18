from states import State


class Charging(State):
    """
    Robot is charging the opponent.
    """
    async def start(self):
        await super().start()
        await self.bot.drive(right_speed=1, left_speed=1)

    async def stop(self):
        super().stop()
        self.bot.stop()

    # TODO: Consider changing direction slightly when opponent detected left/right
    #  (will need to maintain state of L & R motor speeds to adjust)

    async def opponent_detected(self):
        self.logger.debug("Opponent detected")
        if self.bot.opponent_in_range_left() and self.bot.opponent_in_range_right():
            if self.bot.contacting_opponent_left() or self.bot.contacting_opponent_right():
                from states import Grappling
                self.switch(Grappling)
        elif self.bot.opponent_in_range_left() or self.bot.opponent_in_range_left():
            from states import Targeting
            self.switch(Targeting)
        else:
            from states import Searching
            self.switch(Searching)
        
    async def edge_detected(self):
        self.logger.debug("Edge detected")
        from states import RotatingAwayEdge
        self.switch(RotatingAwayEdge)
