from asyncio import sleep

from states import State


class Idle(State):
    async def start(self):
        self.logger.info("Idle state started")
        await super().start()
        self.bot.pixels.fill(0xFF0000)
        self.battery_low = self.bot.battery_low()
        self.leds_off = False

    async def run(self):
        if self.battery_low:
            if self.leds_off:
                self.bot.pixels.fill(0x000000)
            else:
                self.bot.pixels.fill(0xFF0000)
            self.leds_off = not self.leds_off
            await sleep(0.5)
        else:
            await sleep(0)

    async def button_pressed(self, key_event):
        self.logger.debug(f"Button {key_event.key_number} press (pressed={key_event.pressed}) detected from idle state")
        if key_event.key_number == 0 and key_event.pressed:
            from states import Armed
            await self.switch(Armed)
