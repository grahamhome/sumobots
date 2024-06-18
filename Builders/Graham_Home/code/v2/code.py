import asyncio
from asyncio import sleep

from states.idle import Idle
from base_bot import SumoBotBase
import adafruit_logging as logging

class StateManager:

    logger = logging.getLogger("SumoBot")

    def __init__(self):
        self.bot = SumoBotBase()
        self.state = Idle(self.bot)

    async def manage_state(self):
        await self.state.start()
        while True:
            if self.state.next:
                self.state = self.state.next(self.bot)
                await self.state.start()
            await self.state.run()

    async def check_distance_sensors(self):
        while True:
            if self.bot.opponent_in_range_left() or self.bot.opponent_in_range_right():
                # TODO check for min distance to left or right and call self.state.touching_opponent()
                await self.state.opponent_detected()
            await sleep(0)

    async def check_edge_sensors(self):
        while True:
            if self.bot.left_edge_detected() or self.bot.right_edge_detected():
                await self.state.edge_detected()
            await sleep(0)

    async def check_buttons(self):
        while True:
            if key_event := self.bot.keypad.events.get():
                await self.state.button_pressed(key_event)
            await sleep(0)

async def main():
    manager = StateManager()
    await asyncio.gather(asyncio.create_task(manager.manage_state()),
                         asyncio.create_task(manager.check_distance_sensors()),
                         asyncio.create_task(manager.check_edge_sensors()),
                         asyncio.create_task(manager.check_buttons()))


if __name__ == "__main__":
    asyncio.run(main())

