import simpleio

from states import State
from melodies import note_frequencies


class Countdown(State):
    async def start(self):
        super().start()
        self.bot.pixels.fill(0x00FF00)
        simpleio.tone(
            pin=self.bot.piezo,
            frequency=note_frequencies.get("C5"),
            duration=0.3,
        )
        self.bot.pixels.fill(0)
        from states import Searching
        self.switch(Searching)