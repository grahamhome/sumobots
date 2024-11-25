import time
from asyncio import sleep

from states import State
from settings import MAX_GRAPPLE_TIME


class Grappling(State):
    """
    Robot is making contact with the opponent.
    """

    color = 0x00008B

    async def start(self):
        await super().start()
        self.grapple_start = time.monotonic()
        await self.bot.drive(right_speed=1, left_speed=1)

    async def run(self):
        await super().run()
        if time.monotonic() - self.grapple_start >= MAX_GRAPPLE_TIME:
            from states import BreakingGrapple
            await self.switch(BreakingGrapple)
        await sleep(0)

    async def stop(self):
        await self.bot.stop()

    async def edge_detected(self):
        print("Edge detected")
        await self.stop()
        from states import FleeingEdge
        await self.switch(FleeingEdge)
