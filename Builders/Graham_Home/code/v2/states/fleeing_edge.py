from states import State


class FleeingEdge(State):
    """
    Robot is fleeing the edge of the arena.
    """

    async def start(self):
        await super().start()
        # If both sensors are over the edge, drive straight backwards.
        if self.bot.left_edge_detected() and self.bot.right_edge_detected():
            print("Backing straight up and turning around")
            await self.bot.drive(left_speed=-1, right_speed=-1, duration=0.3)
            await self.bot.drive(left_speed=-1, right_speed=1, duration=0.4)

        # If only the left sensor is over the edge, turn to the right,
        # then drive straight backwards.
        elif self.bot.left_edge_detected():
            print("Backing to right and turning around")
            await self.bot.drive(left_speed=-0.5, right_speed=0.5, duration=0.25)
            await self.bot.drive(left_speed=-1, right_speed=-1, duration=0.3)
            await self.bot.drive(left_speed=-1, right_speed=1, duration=0.4)

        # If only the right sensor is over the edge, turn to the left,
        # then drive straight backwards.
        elif self.bot.right_edge_detected():
            print("Backing to left and turning around")
            await self.bot.drive(left_speed=0.5, right_speed=-0.5, duration=0.25)
            await self.bot.drive(left_speed=-1, right_speed=-1, duration=0.3)
            await self.bot.drive(left_speed=1, right_speed=-1, duration=0.4)

        from states import Searching
        self.switch(Searching)
