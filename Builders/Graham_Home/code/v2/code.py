import asyncio
from asyncio import sleep

from base_bot import SumoBotBase
import adafruit_logging as logging

class StateManager:

    logger = logging.getLogger("SumoBot")

    def __init__(self):
        from states.idle import Idle
        self.bot = SumoBotBase()
        self.state = Idle(self.bot, self)
        self.active = True

    async def manage_state(self):
        while True:
            if self.active:
                await self.state.run()
            await sleep(0.1)

    async def check_distance_sensors(self):
        while True:
            if self.active:
                if await self.bot.opponent_in_range_left() or await self.bot.opponent_in_range_right():
                    self.logger.debug(f"Opponent in range right: {await self.bot.opponent_in_range_right()}")
                    self.logger.debug(f"Opponent in range left: {await self.bot.opponent_in_range_left()}")
                    # TODO check for min distance to left or right and call self.state.touching_opponent()
                    await self.state.opponent_detected()
            await sleep(0)

    async def check_edge_sensors(self):
        while True:
            if self.active:
                if self.bot.left_edge_detected() or self.bot.right_edge_detected():
                    await self.state.edge_detected()
            await sleep(0)

    async def check_buttons(self):
        while True:
            if self.active:
                if key_event := self.bot.keypad.events.get():
                    await self.state.button_pressed(key_event)
            await sleep(0)

async def main():
    manager = StateManager()
    await asyncio.gather(asyncio.create_task(manager.manage_state()),
                         asyncio.create_task(manager.check_distance_sensors()),
                         asyncio.create_task(manager.check_edge_sensors()),
                         asyncio.create_task(manager.check_buttons()))


# if __name__ == "__main__":
#     asyncio.run(main())

