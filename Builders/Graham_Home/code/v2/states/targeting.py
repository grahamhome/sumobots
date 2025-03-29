from states import State


class Targeting(State):

    color = 0xADD8E6

    async def start(self):
        await super().start()
        if self.bot.opponent_in_range_left() and self.bot.opponent_in_range_right():
            from states import Charging
            self.switch(Charging)
        if self.bot.opponent_in_range_left():
            await self.bot.drive(left_speed=-1, right_speed=1)
        elif self.bot.opponent_in_range_right():
            await self.bot.drive(left_speed=1, right_speed=-1)
        else:
            from states import Searching
            self.switch(Searching)

    def stop(self):
        super().stop()
        self.bot.stop()

    async def edge_detected(self):
        print("Edge detected")
        self.stop()
        from states import FleeingEdge
        self.switch(FleeingEdge)
