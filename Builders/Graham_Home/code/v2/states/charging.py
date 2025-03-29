from states import State


class Charging(State):
    """
    Robot is charging the opponent.
    """

    color = 0xFF0000
    async def start(self):
        await super().start()
        await self.bot.drive(right_speed=1, left_speed=1)
        self.cancelled = False

    def stop(self):
        super().stop()
        self.bot.stop()

    # TODO: Consider changing direction slightly when opponent detected left/right
    #  (will need to maintain state of L & R motor speeds to adjust)

    async def opponent_detected(self):
        if not self.cancelled:
            print("Opponent detected")
            if await self.bot.opponent_in_range_left() and await self.bot.opponent_in_range_right():
                if await self.bot.contacting_opponent_left() or await self.bot.contacting_opponent_right():
                    from states import Grappling
                    self.switch(Grappling)
            elif await self.bot.opponent_in_range_left() or await self.bot.opponent_in_range_left():
                from states import Targeting
                self.switch(Targeting)
            else:
                from states import Searching
                self.switch(Searching)
        
    async def edge_detected(self):
        self.cancelled = True
        print("Edge detected")
        self.stop()
        from states import FleeingEdge
        self.switch(FleeingEdge)
