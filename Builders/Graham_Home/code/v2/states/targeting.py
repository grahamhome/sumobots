from states import State


class Targeting(State):

    async def start(self):
        await super().start()
        if self.bot.opponent_in_range_left() and self.bot.opponent_in_range_right():
            from states import Charging
            #await self.switch(Charging)
            self.logger.info("Opponent targeted, would switch to Charging now")
            from states import Idle
            await self.switch(Idle)
        if self.bot.opponent_in_range_left():
            await self.bot.drive(left_speed=-1, right_speed=1)
        elif self.bot.opponent_in_range_right():
            await self.bot.drive(left_speed=1, right_speed=-1)
        else:
            from states import Searching
            await self.switch(Searching)

    async def stop(self):
        await super().stop()
        await self.bot.stop()

    async def edge_detected(self):
        self.logger.debug("Edge detected")
        from states import RotatingAwayEdge
        await self.switch(RotatingAwayEdge)
