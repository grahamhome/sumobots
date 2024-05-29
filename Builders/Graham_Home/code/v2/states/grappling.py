import time
from asyncio import sleep

from .breaking_grapple import BreakingGrapple
from .state import State
from ..settings import MAX_GRAPPLE_TIME


class Grappling(State):
    """
    Robot is making contact with the opponent.
    """

    async def start(self):
        await super().start()
        grapple_start = time.monotonic()
        await self.bot.drive(right_speed=1, left_speed=1)
        while True:
            if time.monotonic() - grapple_start >= MAX_GRAPPLE_TIME:
                self.switch(BreakingGrapple)
            await sleep(0)

    def stop(self):
        self.bot.stop()