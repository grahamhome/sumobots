from asyncio import sleep

from .state import State


class BatteryLow(State):
    async def start(self):
        await super().start()
        leds_off = True
        while True:
            if leds_off:
                self.pixels.fill(0x000000)
            else:
                self.pixels.fill(0xFF0000)
            leds_off = not leds_off
            await sleep(0.5)
