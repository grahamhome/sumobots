from states import State


class RotatingAwayEdge(State):

    async def start(self):
        await super().start()
        if self.bot.right_edge_detected() and self.bot.left_edge_detected():
            await self.bot.drive(left_speed=-1, right_speed=1, duration=0.4)
        elif self.bot.right_edge_detected():
            await self.bot.drive(left_speed=-0.5, right_speed=0.5, duration=0.25)
        elif self.bot.left_edge_detected():
            await self.bot.drive(left_speed=0.5, right_speed=-0.5, duration=0.25)
        from states import FleeingEdge
        self.switch(FleeingEdge)
