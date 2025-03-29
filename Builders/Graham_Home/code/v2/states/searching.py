from states import State


class Searching(State):
    """
    Robot is searching for an opponent.
    """
    color = 0x90EE90
    async def start(self):
        await super().start()
        await self.bot.drive(left_speed=-0.5, right_speed=0.5)
        self.cancelled = False

    def stop(self):
        print("Searching is stopping")
        super().stop()
        self.bot.stop()

    async def opponent_detected(self):
        if not self.cancelled:
            print("Opponent detected")
            from states import Targeting
            self.switch(Targeting)

    async def edge_detected(self):
        self.cancelled = True
        from states import FleeingEdge
        self.switch(FleeingEdge)

