from asyncio import sleep

import simpleio

from states import State


class Countdown(State):
    async def start(self):
        self.started = True
        self.bot.pixels.fill(0x00FF00)
        simpleio.tone(
            pin=self.bot.piezo,
            frequency=523.25,
            duration=0.3,
        )
        leds_on = True
        for _ in range(10):
            if leds_on:
                self.bot.pixels.fill(0x00FF00)
            else:
                self.bot.pixels.fill(0x000000)
            leds_on = not leds_on
            await sleep(0.5)
        self.bot.pixels.fill(0)
        from states import Searching
        await self.switch(Searching)