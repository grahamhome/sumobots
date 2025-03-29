import asyncio

from states import State


class FleeingEdge(State):
    """
    Robot is fleeing the edge of the arena.
    """

    color = 0x800080  # Purple

    async def start(self):
        await super().start()
        # If both sensors are over the edge, drive straight backwards and turn around.
        if self.bot.left_edge_detected() and self.bot.right_edge_detected():
            print("Backing straight up and turning around")
            asyncio.get_event_loop().run_until_complete(self.bot.drive(left_speed=-1, right_speed=-1, duration=1.5))
            asyncio.get_event_loop().run_until_complete(self.bot.drive(left_speed=-1, right_speed=1, duration=0.8))

        # If only the left sensor is over the edge, turn to the right,
        # then drive straight backwards.
        elif self.bot.left_edge_detected():
            print("Turning to right and driving away from edge")
            asyncio.get_event_loop().run_until_complete(self.bot.drive(left_speed=0.5, right_speed=-0.5, duration=0.8))
            asyncio.get_event_loop().run_until_complete(self.bot.drive(left_speed=1, right_speed=1, duration=1))

        # If only the right sensor is over the edge, turn to the left,
        # then drive straight backwards.
        elif self.bot.right_edge_detected():
            print("Turning to left and driving away from edge")

            asyncio.get_event_loop().run_until_complete(self.bot.drive(left_speed=-0.5, right_speed=0.5, duration=0.8))
            asyncio.get_event_loop().run_until_complete(self.bot.drive(left_speed=1, right_speed=1, duration=1))

        print("About to switch to Searching")
        from states import Searching
        self.switch(Searching)
