from asyncio import sleep

from .armed import Armed
from .state import State
from .battery_low import BatteryLow


class Idle(State):
    async def start(self):
        await super().start()
        self.bot.pixels.fill(0xFF0000)
        while True:
            if self.bot.battery_low():
                self.switch(BatteryLow)
                break
            else:
                await sleep(0)

    async def button_pressed(self, key_event):
        self.logger.debug("Button press detected")
        if key_event.key_number == 0 and key_event.pressed:
            self.switch(Armed)
