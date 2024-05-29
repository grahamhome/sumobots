from .searching import Searching
from .state import State

class BreakingGrapple(State):
    async def start(self):
        await super().start()
        await self.bot.drive(left_speed=-1, right_speed=-0.8, duration=0.7)
        self.switch(Searching)